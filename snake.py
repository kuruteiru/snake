import pygame

pygame.init()
pygame.display.set_caption("snake")
screen = pygame.display.set_mode((1280, 720), pygame.SCALED)
clock = pygame.time.Clock()
delta_time = 0
is_running = True

background_color = pygame.Color(60, 240, 140)
font = pygame.font.Font(None, 50)
fps_surface = font.render("0", False, "red")

# snake class
class Snake:
    length = 1
    color = pygame.Color(60, 240, 140)
    head = (pygame.display.get_window_size()[0] / 2, pygame.display.get_window_size()[1] / 2)
    body = list()

class Food:
    position = (0,0)
    color = pygame.Color(230, 80, 80)

snake = Snake()

# game loop
while is_running:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: is_running = False

        screen.fill(background_color)
        
        # rect = pygame.Rect(snake_p)

        pygame.draw.circle(screen, snake.color, snake.head, 15)

        fps_surface = font.render(str(clock.get_fps()), False, "red")
        screen.blit(fps_surface, (0,0))

        pygame.display.update()

        # will use for framerate independent movement later
        delta_time = clock.tick() / 1000


pygame.quit()