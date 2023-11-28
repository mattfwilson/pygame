import pygame
import pymunk
import random

pygame.init()
running = True
dimensions = (1000, 1000)
FPS = 90
display = pygame.display.set_mode(dimensions)
clock = pygame.time.Clock()
space = pymunk.Space()

border_thickness = 20
collision_thickness = 10
ball_count = 5000
ball_radius = 5
color_black = (0, 0, 0)
color_white = (255, 255, 255)
color_red = (255, 0, 0)
color_green = (0, 255, 0)
count = 0

def draw_walls():
    bottom_wall = pymunk.Body(body_type=pymunk.Body.STATIC)
    seg_left = pymunk.Segment(bottom_wall, (995, 995), (0, 995), collision_thickness)
    seg_left.elasticity = 1
    space.add(seg_left, bottom_wall)
    pygame.draw.line(display, (color_white), (0, 995), (995, 995), border_thickness) # bottom

    left_wall = pymunk.Body(body_type=pymunk.Body.STATIC)
    seg_left = pymunk.Segment(left_wall, (0, 0), (0, 995), collision_thickness)
    seg_left.elasticity = 1
    space.add(seg_left, left_wall)
    pygame.draw.line(display, (color_white), (0, 995), (0, 0), border_thickness) # left

    top_wall = pymunk.Body(body_type=pymunk.Body.STATIC)
    seg_top = pymunk.Segment(top_wall, (0, 0), (995, 0), collision_thickness)
    seg_top.elasticity = 1
    space.add(seg_top, top_wall)
    pygame.draw.line(display, (color_white), (0, 0), (995, 0), border_thickness) # top

    right_wall = pymunk.Body(body_type=pymunk.Body.STATIC)
    seg_right = pymunk.Segment(right_wall, (995, 995), (995, 0), collision_thickness)
    seg_right.elasticity = 1
    space.add(seg_right, right_wall)
    pygame.draw.line(display, (color_white), (995, 995), (995, 0), border_thickness) # right

class Ball():
    def __init__(self, x, y, collision_type):
        self.body = pymunk.Body()
        self.body.position = x, y
        self.shape = pymunk.Circle(self.body, ball_radius)
        self.shape.elasticity = 1
        self.shape.density = 1
        self.shape.collision_type = collision_type
        self.body.velocity = random.randrange(-200, 200), random.randrange(-200, 200)
        space.add(self.body, self.shape)

    def draw(self):
        if self.shape.collision_type != 2:
            pygame.draw.circle(display, color_white, self.body.position, ball_radius)
        else:
            pygame.draw.circle(display, random.choice([color_red, color_green]), self.body.position, ball_radius)

    def randomize_color(self, arbiter, space, data):
        self.shape.collision_type = 2
        print('Merry Christmas!')

    def get_handler(self):
        return self.shape.collision_type

def rand_num():
    return random.randint(dimensions[0] - 995, dimensions[1] - 50) 

def simulation():
    balls = [Ball(rand_num(), rand_num(), i + 3) for i in range(ball_count)]
    balls.append(Ball(rand_num(), rand_num(), 2))

    handlers = [space.add_collision_handler(2, i + 3) for i in range(ball_count)]
    for i, handler in enumerate(handlers):
        handler.separate = balls[i].randomize_color

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        display.fill(color_black)
        draw_walls()
        [ball.draw() for ball in balls]
        pygame.display.set_caption('Bouncing Simulator')
        pygame.display.update()
        clock.tick(FPS)
        space.step(1/FPS)

if __name__ == '__main__':
    simulation()
    pygame.quit()
