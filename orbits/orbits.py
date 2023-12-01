import pygame
import math

pygame.init()

WIDTH, HEIGHT = 1000, 1000
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Planet Simulation')
color_black = (0, 0, 0)
color_white = (255, 255, 255)

class Planet:
    ASTRO_UNITS = 149.6e6 * 1000
    GRAVITY = 6.67428e-11
    SCALE = 250 / ASTRO_UNITS # 1 astronomical units = 100 pixels
    TIMESTEP = 3600 * 24 # represents 1 day
    
    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass
        self.x_vel = 0
        self.y_vel = 0
        self.sun = False
        self.dist_to_sun = 0
        self.orbit = []

    def draw(self, screen):
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT / 2

def simulation():
    running = True
    clock = pygame.time.Clock()

    while running:
        clock.tick(60)
        SCREEN.fill(color_black)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

simulation()
