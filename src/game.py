from random import randint 
from sys import exit
import objects
import pygame

class Game:
    grid = objects.Grid
    snake: objects.Snake
    food: objects.Food
    screen = pygame.Surface
    clock = pygame.time.Clock
    grow_for = 5

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("snake")
        self.grid = objects.Grid(30, 30, 10)
        self.screen = pygame.display.set_mode((self.grid.width * self.grid.cell_size, self.grid.length * self.grid.cell_size))
        self.clock = pygame.time.Clock()
        self.food = objects.Food(
                value = 1, 
                size = self.grid.cell_size,
                position = pygame.Vector2(self.grid.cell_size * randint(0, self.grid.width - 1), self.grid.cell_size * randint(0, self.grid.length - 1)), 
                color = pygame.Color(230, 80, 80)
        )
        self.snake = objects.Snake(
            length = 3,
            size = self.grid.cell_size, 
            position = pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() / 2),
            direction = objects.Direction.UP,
            color = pygame.Color(77, 166, 255)
        )

    def run(self):
        self.check_collisions()
        self.handle_events()
        self.update()

    def update(self):
        self.clock.tick(10)
        self.snake.move()
        self.screen.fill(pygame.Color(60, 240, 140))
        self.food.draw(self.screen)
        self.snake.draw(self.screen)
        pygame.display.update()

    def check_collisions(self):
        for i in range(1, len(self.snake.body)):
            if (self.snake.body[0].position == self.snake.body[i].position):
                self.game_over()

        if (self.snake.body[0].position == self.food.position):
            self.food.change_position(self.grid)
            self.snake.grow(self.food.value)
            return
        
        if (0 > self.snake.body[0].position.x or self.snake.body[0].position.x >= self.grid.width * self.grid.cell_size or
            0 > self.snake.body[0].position.y or self.snake.body[0].position.y >= self.grid.length * self.grid.cell_size):  
            self.game_over()

    def handle_events(self):
        for event in pygame.event.get():
            match event.type:
                case pygame.KEYDOWN: self.handle_controls(event.key)
                case pygame.QUIT: self.exit_game()

    def handle_controls(self, key: int):
        match key:
            case pygame.K_UP | pygame.K_w: 
                if (self.snake.direction != objects.Direction.DOWN):
                    self.snake.direction = objects.Direction.UP
            case pygame.K_LEFT | pygame.K_a: 
                if (self.snake.direction != objects.Direction.RIGHT):
                    self.snake.direction = objects.Direction.LEFT
            case pygame.K_DOWN | pygame.K_s: 
                if (self.snake.direction != objects.Direction.UP):
                    self.snake.direction = objects.Direction.DOWN
            case pygame.K_RIGHT | pygame.K_d: 
                if (self.snake.direction != objects.Direction.LEFT):
                    self.snake.direction = objects.Direction.RIGHT

    def game_over(self):
        pass

    def exit_game():
        pygame.quit()
        exit()