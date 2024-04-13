from random import randint 
from enum import Enum
import pygame

class Direction(Enum): 
    UP = pygame.Vector2(0, -1)
    DOWN = pygame.Vector2(0, 1)
    LEFT = pygame.Vector2(-1, 0)
    RIGHT = pygame.Vector2(1, 0)

class Grid:
    width: int
    length: int
    cell_size: int

    def __init__(self, width: int, length: int, cell_size: int):
        self.width = width
        self.length = length
        self.cell_size = cell_size

class Food:
    value: int
    size: int
    position: pygame.Vector2
    color: pygame.Color
    image: pygame.Surface
    rect: pygame.Rect

    def __init__(self, value: int, size: int, position: pygame.Vector2, color: pygame.Color):
        self.value = value
        self.size = size
        self.position = position
        self.color = color
        self.image = pygame.Surface((size, size))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft = position)

    def draw(self, surface): surface.blit(self.image, self.rect)

    def change_position(self, grid: Grid):
        self.position = pygame.Vector2(grid.cell_size * randint(0, grid.width - 1), grid.cell_size * randint(0, grid.length - 1))
        self.rect.topleft = self.position

class SnakeNode:
    size: int
    position: pygame.Vector2
    color: pygame.Color
    image: pygame.Surface
    rect: pygame.Rect

    def __init__(self, size: int, position: pygame.Vector2, color: pygame.Color):
        self.position = position
        self.size = size
        self.color = color
        self.image = pygame.Surface((size, size))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft = position)

    def draw(self, surface): surface.blit(self.image, self.rect)

class Snake:
    length: int
    size: int
    speed: int
    body: list
    direction: Direction
    color: pygame.Color

    def __init__(self, length: int, size: int, speed: int, position: pygame.Vector2, direction: Direction, color: pygame.Color):
        self.length = length
        self.size = size
        self.speed = speed
        self.direction = direction
        self.color = color
        self.body = list()
        for i in range(length):
            self.body.append(SnakeNode(size, position - direction.value * size * i, color))

    def draw(self, surface: pygame.Surface):
        for node in self.body: surface.blit(node.image, node.rect)

    def grow(self, value: int): 
        for i in range(value):
            direction = self.direction.value if self.length < 2 else self.body[-2].position - self.body[-1].position
            self.body.append(SnakeNode(self.size, self.body[-1].position - direction.normalize() * self.size, self.color))

    def move(self):
        self.body.insert(0, SnakeNode(self.size, self.body[0].position + self.direction.value * self.size, self.color))
        self.body.pop()