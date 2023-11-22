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
border_thickness = 10
ball_radius = 25


bottom_wall = pymunk.Body(body_type=pymunk.Body.STATIC)
seg_bottom = pymunk.Segment(bottom_wall, (5, 5), (5, 595), border_thickness)
seg_bottom.elasticity = 1
space.add(seg_bottom, bottom_wall)

left_wall = pymunk.Body(body_type=pymunk.Body.STATIC)
seg_left = pymunk.Segment(left_wall, (595, 5), (5, 5), border_thickness)
seg_left.elasticity = 1
space.add(seg_left, left_wall)

top_wall = pymunk.Body(body_type=pymunk.Body.STATIC)
seg_top = pymunk.Segment(top_wall, (595, 595), (5, 595), border_thickness)
seg_top.elasticity = 1
space.add(seg_top, top_wall)

right_wall = pymunk.Body(body_type=pymunk.Body.STATIC)
seg_right = pymunk.Segment(right_wall, (595, 595), (595, 5), border_thickness)
seg_right.elasticity = 1
space.add(seg_right, right_wall)

def rand_spawn():
    x = random.randint(50, 550)
    y = random.randint(50, 550)
    return x, y

def convert_coords(point):
    return int(point[0]), 600 - int(point[1])

class Ball():
    def __init__(self, x, y):
        self.body = pymunk.Body()
        self.body.position = x, y
        self.shape = pymunk.Circle(self.body, ball_radius)
        self.shape.elasticity = 1
        self.shape.density = 1
        self.body.velocity = random.uniform(300, 500), random.uniform(300, 500)
        space.add(self.body, self.shape)

    def draw(self):
        pygame.draw.circle(display, (255, 0, 0), self.body.position, ball_radius)
        
def game():
    ball1 = Ball(100, 100)
    ball2 = Ball(500, 100)
    ball3 = Ball(100, 500)
    ball4 = Ball(500, 500)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        display.fill(bg_color)
        pygame.draw.line(display, (160, 160, 160), (0, 600), (600, 600), border_thickness) # bottom
        pygame.draw.line(display, (160, 160, 160), (0, 600), (0, 0), border_thickness) # left
        pygame.draw.line(display, (160, 160, 160), (0, 0), (600, 0), border_thickness) # top
        pygame.draw.line(display, (160, 160, 160), (600, 600), (600, 0), border_thickness) # right
        ball1.draw()
        ball2.draw()
        ball3.draw()
        ball4.draw()
        pygame.display.update()
        clock.tick(FPS)
        space.step(1/FPS)

game()
pygame.quit()

