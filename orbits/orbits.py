import pygame
import math
import pyautogui
import random

pygame.init()

WIDTH, HEIGHT = pyautogui.size()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Planet Sim')

color_black = (0, 0, 0)
color_white = (255, 255, 255)
color_yellow = (244, 219, 72)
color_blue = (120, 196, 242)
color_orange = (225, 181, 91)
color_red = (212, 114, 93)
color_grey = (80, 70, 80)

class Planet:
    AU = 149.6e6 * 1000
    GRAVITY = 6.67428e-11
    SCALE = 125 / AU # 1 astronomical units = 100 pixels
    TIMESTEP = 10800 * 24 # represents 1 day
    
    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass
        self.x_vel = 0
        self.y_vel = 0
        self.is_sun = False
        self.dist_to_sun = 0
        self.orbit = []

    def draw(self, screen):
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT / 2
        pygame.draw.circle(screen, self.color, (x, y), self.radius)

    def attraction(self, other):
        # calculate distance between objects
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

        # check if other object is sun or not
        if other.is_sun:
            self.distance_to_sun = distance

        # calculate force of attraction
        force = self.GRAVITY * self.mass * other.mass / distance**2
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force
        return force_x, force_y

    def update_pos(self, planets):
        # get total force of all planet except for itself
        total_fx = total_fy = 0

        for planet in planets:
            if self == planet:
                continue

            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy

        # figure x and y velocities against sun gravity
        self.x_vel += total_fx / self.mass * self.TIMESTEP
        self.y_vel += total_fy / self.mass * self.TIMESTEP
        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP
        self.orbit.append((self.x, self.y))

    def rand_vel(self):
        self.vel_y = random.uniform(-30, -10)
        return self.vel_y

def simulation():
    running = True
    clock = pygame.time.Clock()
    
    # define planet stats
    sun = Planet(0, 0, 30, color_yellow, 1.98892 * 10**30)
    sun.is_sun = True

    earth = Planet(-1 * Planet.AU, 0, 16, color_blue, 5.9742 * 10**24 )
    earth.y_vel = 29.783 * 1000
    
    mars = Planet(-1.524 * Planet.AU, 0, 12, color_red, 6.39 * 10**23)
    mars.y_vel = 24.077 * 1000
    
    mercury = Planet(0.387 * Planet.AU, 0, 8, color_grey, 3.30 * 10**23)
    mercury.y_vel = -47.4 * 1000

    venus = Planet(0.723 * Planet.AU, 0, 14, color_white, 4.8685 * 10**24)
    venus.y_vel = -35.02 * 1000

    jupiter = Planet(5.2 * Planet.AU, 0, 20, color_orange, 1.89813 * 10**27)
    jupiter.y_vel = 13.06 * 1000

    planets = [sun, earth, mars, mercury, venus, jupiter]

    while running:
        clock.tick(60)
        SCREEN.fill((0, 0, 0))
        
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_j:
                    jupiter.y_vel = random.uniform(0, 13.06) * 1000
                if event.key == pygame.K_c:
                    mercury.y_vel = random.uniform(-40, -47.4) * 1000
                if event.key == pygame.K_e:
                    earth.y_vel = random.uniform(15, 29.783) * 1000
                if event.key == pygame.K_v:
                    venus.y_vel = random.uniform(-25, -35.02) * 10800
                if event.key == pygame.K_m:
                    mars.y_vel = random.uniform(10, 24.077) * 1000
                if event.key == pygame.K_s:
                    sun.x_vel = random.uniform(0, 7) * 1000

        for planet in planets:
            planet.update_pos(planets)
            planet.draw(SCREEN)

        pygame.display.update()

    pygame.quit()

simulation()
