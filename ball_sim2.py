import pygame
import pymunk
import random

running = True
dimensions = (600, 600)
bg_color = (255, 255, 255)
FPS = 120
border_thickness = 20
collision_thickness = 10
ball_count = 25
ball_radius = 10

pygame.init()
display = pygame.display.set_mode(dimensions)
clock = pygame.time.Clock()
space = pymunk.Space()

def draw_walls():
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

    pygame.draw.line(display, (160, 160, 160), (0, 600), (600, 600), border_thickness) # bottom
    pygame.draw.line(display, (160, 160, 160), (0, 600), (0, 0), border_thickness) # left
    pygame.draw.line(display, (160, 160, 160), (0, 0), (600, 0), border_thickness) # top
    pygame.draw.line(display, (160, 160, 160), (600, 600), (600, 0), border_thickness) # right

class Ball():
    def __init__(self, x, y, collision_type):
        self.body = pymunk.Body()
        self.body.position = x, y
        self.shape = pymunk.Circle(self.body, ball_radius)
        self.shape.elasticity = 1
        self.shape.density = 1
        self.shape.collision_type = 1
        self.body.velocity = random.randrange(-200, 200), random.randrange(-200, 200)
        space.add(self.body, self.shape)

    def draw(self):
        pygame.draw.circle(display, (0, 0, 255), self.body.position, ball_radius)

def rand_num():
    return random.randint(dimensions[0] - 550, dimensions[1] - 50) 
    
def collide():
    print('collision occurred')
    return True

def simulation():
    balls = [Ball(rand_num(), rand_num(), 1) for i in range(ball_count)]
    balls.append(Ball(rand_num(), rand_num(), 2))

    handler = space.add_collision_handler(1, 2)
    handler.begin = collide()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        display.fill(bg_color)
        draw_walls()
        [ball.draw() for ball in balls]
        pygame.display.set_caption('Bouncing Simulator')
        pygame.display.update()
        clock.tick(FPS)
        space.step(1/FPS)

if __name__ == '__main__':
    simulation()
    pygame.quit()
