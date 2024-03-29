#region imports

import pygame
from sys import exit
from random import randint 

#endregion imports

#region game-objects

class Grid:
    width: int
    length: int
    cell_size: int
    cells: any
    surface: pygame.Surface

    def __init__(self, width: int, length: int, cell_size: int):
        self.width = width
        self.length = length
        self.cell_size = cell_size
        self.cells = [["" for x in range(width)] for y in range(length)]

class Snake:
    body: list
    direction: pygame.Vector2
    color: pygame.Color

    def __init__(self, position: pygame.Vector2, direction: pygame.Vector2, color: pygame.Color):
        self.body = [position]
        self.direction = direction.normalize()
        self.color = color

    def move(self, direction: pygame.Vector2): pass
    def grow(self, value: int): pass

class SnakeNode(pygame.sprite.Sprite):
    position: pygame.Vector2

class Food(pygame.sprite.Sprite):
    value: int
    position: pygame.Vector2
    size: pygame.Vector2
    color: pygame.Color

    def __init__(self, value: int, position: pygame.Vector2, size: pygame.Vector2, color: pygame.Color):
        self.value = value
        self.position = position
        self.size = size
        self.color = color
        super().__init__()
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft = position)

#endregion game-objects

#region global

delta_time = 0
clock = pygame.time.Clock()

background_color = pygame.Color(60, 240, 140)
snake_color = pygame.Color(60, 240, 140)
food_color = pygame.Color(230, 80, 80)

grid = Grid(50,50,10)
snake = Snake(pygame.Vector2(0,0), pygame.Vector2(0,1), snake_color)
food = pygame.sprite.GroupSingle(
    Food(
        value=1, 
        position=pygame.Vector2(grid.cell_size * randint(0, grid.width), grid.cell_size * randint(0, grid.length)), 
        size=pygame.Vector2(grid.cell_size, grid.cell_size), 
        color=food_color
    )
)

pygame.init()
pygame.display.set_caption("snake")
screen_size = (grid.width * grid.cell_size, grid.length * grid.cell_size)
screen = pygame.display.set_mode(screen_size)

#endregion global

#region game-loop

while True:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit()
            exit()

        screen.fill(background_color)
        
        food.draw(screen) 

        pygame.display.update()

        # will use for framerate independent movement later
        delta_time = clock.tick() / 1000

#endregion game-loop