from random import randint 
from sys import exit
import objects
import pygame

class Game:
    score: int
    grid = objects.Grid
    snake: objects.Snake
    food: objects.Food
    input_queue: list
    screen = pygame.Surface
    clock = pygame.time.Clock
    update_timer_event: pygame.event.Event
    font: pygame.font.Font

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("snake")
        self.score = 0
        self.grid = objects.Grid(30, 30, 10)
        self.screen = pygame.display.set_mode((self.grid.width * self.grid.cell_size, self.grid.length * self.grid.cell_size))
        self.clock = pygame.time.Clock()
        self.input_queue = list()
        self.food = objects.Food(
                value = 1, 
                size = self.grid.cell_size,
                position = pygame.Vector2(self.grid.cell_size * randint(0, self.grid.width - 1), self.grid.cell_size * randint(0, self.grid.length - 1)), 
                color = pygame.Color(230, 80, 80)
        )
        self.snake = objects.Snake(
            length = 3,
            size = self.grid.cell_size, 
            speed = 1,
            position = pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() / 2),
            direction = objects.Direction.UP,
            color = pygame.Color(75, 165, 255)
        )
        self.update_timer_event = pygame.event.custom_type()
        pygame.time.set_timer(self.update_timer_event, self.snake.speed * 100)
        pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, self.update_timer_event])
        self.font = pygame.font.SysFont('Roboto', 36)

    def run(self):
        self.check_collisions()
        self.handle_events()
        self.clock.tick()

    def update(self):
        self.screen.fill(pygame.Color(60, 240, 140))
        self.food.draw(self.screen)
        self.snake.move()
        if self.input_queue: 
            self.snake.direction = self.input_queue[0]
            self.input_queue.pop(0)
        self.snake.draw(self.screen)
        self.display_score()
        pygame.display.update()

    def check_collisions(self):
        for i in range(1, len(self.snake.body)):
            if (self.snake.body[0].position == self.snake.body[i].position):
                self.game_over()

        if (self.snake.body[0].position == self.food.position):
            self.food.change_position(self.grid)
            self.snake.grow(self.food.value)
            self.score += 1
            pygame.time.set_timer(self.update_timer_event, self.snake.speed * 100 - self.score)
        
        if (0 > self.snake.body[0].position.x or self.snake.body[0].position.x >= self.grid.width * self.grid.cell_size or
            0 > self.snake.body[0].position.y or self.snake.body[0].position.y >= self.grid.length * self.grid.cell_size):
            self.game_over()

    def handle_events(self):
        for event in pygame.event.get():
            match event.type:
                case self.update_timer_event: self.update()
                case pygame.KEYDOWN: self.handle_controls(event.key)
                case pygame.QUIT: self.exit_game()

    def handle_controls(self, key: int):
        match key:
            case pygame.K_UP | pygame.K_w:
                if (self.snake.direction != objects.Direction.DOWN):
                    self.input_queue.append(objects.Direction.UP)
            case pygame.K_LEFT | pygame.K_a:
                if (self.snake.direction != objects.Direction.RIGHT):
                    self.input_queue.append(objects.Direction.LEFT)
            case pygame.K_DOWN | pygame.K_s:
                if (self.snake.direction != objects.Direction.UP):
                    self.input_queue.append(objects.Direction.DOWN)
            case pygame.K_RIGHT | pygame.K_d:
                if (self.snake.direction != objects.Direction.LEFT):
                    self.input_queue.append(objects.Direction.RIGHT)

    def display_score(self):
        font_surface = self.font.render(str(self.score), False, pygame.Color(0, 180, 75))
        font_rect = font_surface.get_rect(topleft = (self.grid.cell_size, self.grid.cell_size))
        self.screen.blit(font_surface, font_rect)

    def game_over(self):
        self.exit_game()

    def exit_game(self):
        pygame.quit()
        exit()