import pygame
import pymunk
import random

pygame.init()

running = True
display = pygame.display.set_mode((600, 600))
bg_color = (255, 255, 255)
clock = pygame.time.Clock()
space = pymunk.Space()
FPS = 50
radius = 10

def convert_coordinates(point):
    return int(point[0]), 600 - int(point[1])

class Ball():
    def __init__(self, x, y):
        self.body = pymunk.Body()
        self.body.position = x, y
        self.shape = pymunk.Circle(self.body, radius)
        self.shape.elasticity = 1
        self.shape.density = 1
        self.body.velocity = random.uniform(-400, 400), random.uniform(-400, 400)
        space.add(self.body, self.shape)

    def draw(self):
        pygame.draw.circle(display, (255, 0, 0), convert_coordinates(self.body.position), radius)
        
def game():
    ball1 = Ball(100, 100)
    ball2 = Ball(100, 500)

    handler = space.add_collision_handler()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        display.fill(bg_color)
        ball1.draw()
        ball2.draw()
        pygame.display.update()
        clock.tick(FPS)
        space.step(1/FPS)

game()
pygame.quit()

