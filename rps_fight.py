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
border_thickness = 20
collision_thickness = 10
ball_radius = 10

# define walls
bottom_wall = pymunk.Body(body_type=pymunk.Body.STATIC)
seg_bottom = pymunk.Segment(bottom_wall, (5, 5), (5, 595), collision_thickness)
seg_bottom.elasticity = 1
space.add(seg_bottom, bottom_wall)

left_wall = pymunk.Body(body_type=pymunk.Body.STATIC)
seg_left = pymunk.Segment(left_wall, (595, 5), (0, 0), collision_thickness)
seg_left.elasticity = 1
space.add(seg_left, left_wall)

top_wall = pymunk.Body(body_type=pymunk.Body.STATIC)
seg_top = pymunk.Segment(top_wall, (595, 595), (5, 595), collision_thickness)
seg_top.elasticity = 1
space.add(seg_top, top_wall)

right_wall = pymunk.Body(body_type=pymunk.Body.STATIC)
seg_right = pymunk.Segment(right_wall, (600, 600), (595, 5), collision_thickness)
seg_right.elasticity = 1
space.add(seg_right, right_wall)

class Ball():
    def __init__(self, x, y, collision_type):
        self.body = pymunk.Body()
        self.body.position = x, y
        self.shape = pymunk.Circle(self.body, ball_radius)
        self.shape.elasticity = 1
        self.shape.density = 1
        self.shape.collision_type = 1
        self.body.velocity = random.uniform(300, 500), random.uniform(300, 500)
        space.add(self.body, self.shape)

    def draw(self):
        if self.shape.collision_type != 2:
            pygame.draw.circle(display, (255, 0, 0), self.body.position, ball_radius)
        else:
            pygame.draw.circle(display, (0, 0, 255), self.body.position, ball_radius)

    def change_color():
        self.shape.collision_type = 2

def collide():
    print('collision occurred')
    return True

def game():
    balls = [Ball(random.randint(50, 550), random.randint(500, 550), i+3) for i in range(50)]
    balls.append(Ball(400, 400, 2))

    handler = space.add_collision_handler(1, 2)
    handler.begin = collide()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # render shapes on display surface
        display.fill(bg_color)
        pygame.draw.line(display, (160, 160, 160), (0, 600), (600, 600), border_thickness) # bottom
        pygame.draw.line(display, (160, 160, 160), (0, 600), (0, 0), border_thickness) # left
        pygame.draw.line(display, (160, 160, 160), (0, 0), (600, 0), border_thickness) # top
        pygame.draw.line(display, (160, 160, 160), (600, 600), (600, 0), border_thickness) # right
        [ball.draw() for ball in balls]
        pygame.display.set_caption('Circle Simulator')
        pygame.display.update()
        clock.tick(FPS)
        space.step(1/FPS)

game()
pygame.quit()

