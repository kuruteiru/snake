import unittest
import pygame
import sys
import os

src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
music_dir = os.path.abspath(os.path.join(src_dir, 'music'))
print(src_dir)
print(music_dir)
sys.path.append(src_dir)
sys.path.append(music_dir)

import objects
import game

class TestGame(unittest.TestCase):
    def test_initialization(self):
        g = game.Game()
        self.assertEqual(g.score, 0)
        self.assertIsInstance(g.grid, objects.Grid)
        self.assertIsInstance(g.screen, pygame.Surface)
        self.assertIsInstance(g.clock, pygame.time.Clock)
        self.assertIsInstance(g.food, objects.Food)
        self.assertIsInstance(g.snake, objects.Snake)
        self.assertIsInstance(g.input_queue, list)
        self.assertIsInstance(g.update_timer_event, pygame.event.EventType)
        self.assertIsInstance(g.font, pygame.font.Font)

    def test_check_collisions(self):
        g = game.Game()

        g.snake.body[0].position = pygame.Vector2(100, 100)
        g.snake.body[1].position = pygame.Vector2(100, 100)
        self.assertTrue(g.check_collisions())  

        g.food.position = pygame.Vector2(100, 100)
        initial_length = len(g.snake.body)
        self.assertTrue(g.check_collisions())  
        self.assertNotEqual(len(g.snake.body), initial_length)
        self.assertNotEqual(g.food.position, pygame.Vector2(100, 100))

        g.snake.body[0].position = pygame.Vector2(-10, 100)
        self.assertTrue(g.check_collisions())

    def test_handle_controls(self):
        g = game.Game()
        # Test key presses
        g.handle_controls(pygame.K_UP)
        self.assertEqual(g.input_queue[-1], objects.Direction.UP)
        g.handle_controls(pygame.K_LEFT)
        self.assertEqual(g.input_queue[-1], objects.Direction.LEFT)
        g.handle_controls(pygame.K_DOWN)
        self.assertEqual(g.input_queue[-1], objects.Direction.DOWN)
        g.handle_controls(pygame.K_RIGHT)
        self.assertEqual(g.input_queue[-1], objects.Direction.RIGHT)

    def test_display_score(self):
        g = game.Game()
        g.score = 5
        g.display_score()
        self.assertEqual(g.screen.get_at((g.grid.cell_size, g.grid.cell_size))[:3], (0, 180, 75))

if __name__ == '__main__': unittest.main()
