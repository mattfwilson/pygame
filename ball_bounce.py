import pygame as pg
import pymunk as pm

pg.init()

display = pg.display.set_mode((1200, 800))
bg_color = (255, 255, 255)
clock = pg.time.Clock()
FPS = 60

bounce_sound = pg.mixer('boing-2.wav')

space = pm.Space()
space.gravity = 0, -1000
space.elasticity = 1

ball = pm.Body()
ball.position = 100, 600
shape = pm.Circle(ball, 10)
shape.density = 1
shape.elasticity = 1
space.add(ball, shape)

slope = pm.Body(body_type=pm.Body.STATIC)
segment = pm.Segment(slope, (0, 450), (800, 150), 5)
segment.elasticity = .5
space.add(segment, slope)

ramp = pm.Body(body_type=pm.Body.STATIC)
segment2 = pm.Segment(ramp, (600, 150), (850, 200), 5)
segment2.elasticity = .5
space.add(segment2, ramp)

def convert_coordinates(point):
    return point[0], 800 - point[1]

def game():
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        display.fill(bg_color)
        x, y = convert_coordinates(ball.position)
        pg.draw.circle(display, (255, 0, 0), (int(x), int(y)), 20)
        pg.draw.line(display, (0, 0, 0), (0, 350), (800, 650), 5)
        pg.draw.line(display, (0, 0, 0), (600, 650), (850, 600), 5)

        pg.display.update()
        clock.tick(FPS)
        space.step(1/FPS)

game()
pg.quit()

