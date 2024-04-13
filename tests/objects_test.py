import unittest
import pygame
import sys
import os

src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.append(src_dir)

import objects 

class TestGrid(unittest.TestCase):
    def test_initialization(self):
        grid = objects.Grid(30, 30, 10)
        self.assertEqual(grid.width, 30)
        self.assertEqual(grid.length, 30)
        self.assertEqual(grid.cell_size, 10)

class TestFood(unittest.TestCase): 
    def test_initialization(self):
        food = objects.Food(1, 10, pygame.Vector2(100, 100), pygame.Color(230, 80, 80))
        self.assertEqual(food.value, 1)
        self.assertEqual(food.size, 10)
        self.assertEqual(food.position, pygame.Vector2(100, 100))
        self.assertEqual(food.color, pygame.Color(230, 80, 80))

    def test_change_position(self):
        grid = objects.Grid(30, 30, 10)
        food = objects.Food(1, 20, grid.cell_size * 2, pygame.Color(255, 0, 0))
        food.change_position(grid)
        self.assertTrue(0 <= food.position.x < grid.cell_size * grid.width)
        self.assertTrue(0 <= food.position.y < grid.cell_size * grid.length)

class TestSnakeNode(unittest.TestCase):
    def test_initialization(self):
        node = objects.SnakeNode(10, pygame.Vector2(100, 100), pygame.Color(75, 165, 255))
        self.assertEqual(node.size, 10)
        self.assertEqual(node.position, pygame.Vector2(100, 100))
        self.assertEqual(node.color, pygame.Color(75, 165, 255))

class TestSnake(unittest.TestCase):
    def test_initialization(self):
        snake = objectsSnake(3, 20, 1, pygame.Vector2(100, 100), Direction.RIGHT, pygame.Color(0, 0, 255))
        self.assertEqual(snake.length, 3)
        self.assertEqual(snake.size, 20)
        self.assertEqual(snake.speed, 1)
        self.assertEqual(snake.direction, Direction.RIGHT)
        self.assertEqual(snake.color, pygame.Color(0, 0, 255))
        self.assertEqual(len(snake.body), 3)
    def test_grow(self): pass
    def test_move(self): pass