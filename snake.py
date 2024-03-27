import pygame, sys

pygame.init()
pygame.display.set_caption("snake")
screen = pygame.display.set_mode((1280, 720), pygame.SCALED)
clock = pygame.time.Clock()
delta_time = 0
is_running = True

# font = pygame.font.Font(None, 50)
# fps_surface = font.render("0", False, "red")

background_color = pygame.Color(60, 240, 140)

default_snake_color = pygame.Color(60, 240, 140)
default_food_color = pygame.Color(230, 80, 80)

class Grid:
    width: int
    length: int 
    cells: any

    def __init__(self, width: int, length: int):
        self.width = width
        self.length = length
        self.cells = [width][length]

class Snake:
    body: list
    direction: tuple
    color: pygame.Color

    def __init__(self, position: tuple, direction: tuple, color: pygame.Color):
        self.body = {position}
        self.direction = direction
        self.color = color

    def move(direction: tuple): pass
    def grow(value: int): pass

class Food:
    position: tuple
    value: int 
    color: pygame.Color

    def __init__(self, position: tuple, value: int, color: pygame.Color):
        self.position = position
        self.value = value
        self.color = color

grid = Grid(30, 30)
snake = Snake((20,20), (0,1), default_snake_color)
food = Food((5,5), 1, default_food_color)

# game loop
while True:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()

        screen.fill(background_color)
        
        # rect = pygame.Rect(snake_p)
        # pygame.draw.circle()
        # fps_surface = font.render(str(clock.get_fps()), False, "red")
        # screen.blit(fps_surface, (0,0))

        pygame.display.update()

        # will use for framerate independent movement later
        delta_time = clock.tick() / 1000