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
        food = objects.Food(1, 20, pygame.Vector2(grid.cell_size * 2, grid.cell_size * 2), pygame.Color(230, 80, 80))
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
        snake = objects.Snake(3, 10, 1, pygame.Vector2(100, 100), objects.Direction.UP, pygame.Color(75, 165, 255))
        self.assertEqual(snake.length, 3)
        self.assertEqual(snake.size, 10)
        self.assertEqual(snake.speed, 1)
        self.assertEqual(snake.direction, objects.Direction.UP)
        self.assertEqual(snake.color, pygame.Color(75, 165, 255))
        self.assertEqual(len(snake.body), 3)
        # add test for individual snake nodes

    def test_grow(self):
        snake = objects.Snake(3, 10, 1, pygame.Vector2(100, 100), objects.Direction.UP, pygame.Color(75, 165, 255))
        snake.grow(1)
        self.assertEqual(len(snake.body), 4)
        # add test for individual snake nodes
    
    def test_move(self):
        snake = objects.Snake(3, 10, 1, pygame.Vector2(100, 100), objects.Direction.UP, pygame.Color(75, 165, 255))
        snake.move()
        self.assertEqual(snake.body[0].position, pygame.Vector2(100, 90))
        # add test for individual snake nodes

if __name__ == '__main__':
    unittest.main()