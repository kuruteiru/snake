from random import randint 
from sys import exit
import objects
import pygame

grid = objects.Grid(50, 50, 10)

SCREEN_SIZE = (grid.width * grid.cell_size, grid.length * grid.cell_size)
BACKGROUND_COLOR = pygame.Color(60, 240, 140)
SNAKE_COLOR = pygame.Color(77, 166, 255)
FOOD_COLOR = pygame.Color(230, 80, 80)

screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

food = objects.Food(
        value = 1, 
        size = grid.cell_size,
        position = pygame.Vector2(grid.cell_size * randint(0, grid.width - 1), grid.cell_size * randint(0, grid.length - 1)), 
        color = FOOD_COLOR
)

snake = objects.Snake(
    length = 5,
    size = grid.cell_size, 
    position = pygame.Vector2(grid.cell_size * 3, grid.cell_size * 3),
    direction = objects.Direction.RIGHT,
    color = SNAKE_COLOR 
)

pygame.init()
pygame.display.set_caption("snake")

def handle_events():
    for event in pygame.event.get():
        match event.type:
            case pygame.KEYDOWN: handle_controls(event.key)
            case pygame.QUIT: exit_game()

def handle_controls(key: int):
    match key:
        case pygame.K_UP | pygame.K_w: 
            if (snake.direction != objects.Direction.DOWN):
                snake.direction = objects.Direction.UP
        case pygame.K_LEFT | pygame.K_a: 
            if (snake.direction != objects.Direction.RIGHT):
                snake.direction = objects.Direction.LEFT
        case pygame.K_DOWN | pygame.K_s: 
            if (snake.direction != objects.Direction.UP):
                snake.direction = objects.Direction.DOWN
        case pygame.K_RIGHT | pygame.K_d: 
            if (snake.direction != objects.Direction.LEFT):
                snake.direction = objects.Direction.RIGHT

def exit_game():
    pygame.quit()
    exit()
    
while True:
    handle_events()

    screen.fill(BACKGROUND_COLOR)
        
    snake.move()
    snake.draw(screen)
    food.draw(screen)

    pygame.display.update()

    clock.tick(10)