import pygame
import objects
from sys import exit
from random import randint 

BACKGROUND_COLOR = pygame.Color(60, 240, 140)
SNAKE_COLOR = pygame.Color(77, 166, 255)
FOOD_COLOR = pygame.Color(230, 80, 80)

grid = objects.Grid(50,50,10)

snake = objects.Snake(
    length = 3,
    size = grid.cell_size, 
    position = pygame.Vector2(grid.cell_size * 3, grid.cell_size * 3),
    direction = pygame.Vector2(1,0),
    color = SNAKE_COLOR 
)

snake2 = objects.Snake(
    length = 3,
    size = grid.cell_size, 
    position = pygame.Vector2(grid.cell_size * 4, grid.cell_size * 4),
    direction = pygame.Vector2(1,0),
    color = pygame.Color("red")
)

food = objects.Food(
        value = 1, 
        size = grid.cell_size,
        position = pygame.Vector2(grid.cell_size * randint(0, grid.width - 1), grid.cell_size * randint(0, grid.length - 1)), 
        color = FOOD_COLOR
)

SCREEN_SIZE = (grid.width * grid.cell_size, grid.length * grid.cell_size)

pygame.init()
pygame.display.set_caption("snake")

screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()
delta_time = 0

snake.draw(screen)

def handle_input():
    pass

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN: 
            match event.key:
                case pygame.K_UP | pygame.K_w:
                    print('up')
                case pygame.K_LEFT | pygame.K_a:
                    print('left')
                case pygame.K_DOWN | pygame.K_s:
                    print('down')
                case pygame.K_RIGHT | pygame.K_d:
                    print('right')
                    
        elif event.type == pygame.QUIT: 
            pygame.quit()
            exit()

        screen.fill(BACKGROUND_COLOR)
        
        food.draw(screen)
        # snake.move(pygame.Vector2(0,1))
        snake.draw(screen)

        pygame.display.update()

        # will use for framerate independent movement later
        delta_time = clock.tick() / 1000