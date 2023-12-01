import pygame
import math
#from screeninfo import get_monitors
#import ctypes
from AppKit import NSScreen
pygame.init()

#user = ctypes.windll.user32
WIDTH = NSScreen.mainScreen().frame().size.width
HEIGHT = NSScreen.mainScreen().frame().size.height
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Planet Simulation')

color_black = (0, 0, 0)
color_white = (255, 255, 255)
color_yellow = (255, 255, 0)
color_blue = (106, 187, 218)
color_orange = (193, 108, 67)

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
        pygame.draw.circle(screen, self.color, (x, y), self.radius)

def simulation():
    running = True
    clock = pygame.time.Clock()

    sun = Planet(0, 0, 30, color_yellow, 1.98892 * 10**30)
    sun.sun = True

    earth = Planet(-1 * Planet.ASTRO_UNITS, 0, 16, color_blue, 5.9742 * 10**24 )
    mars = Planet(-1.524 * Planet.ASTRO_UNITS, 0, 12, color_orange, 6.39 * 10**23)
    planets = [sun, earth, mars]

    while running:
        clock.tick(60)
        
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        for planet in planets:
            planet.draw(SCREEN)

        pygame.display.update()

    pygame.quit()

simulation()
