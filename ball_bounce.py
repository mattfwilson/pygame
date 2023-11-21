import pygame as pg
import pymunk as pm

pg.init()

display = pg.display.set_mode((800, 800))
bg_color = (255, 255, 255)
clock = pg.time.Clock()
space = pm.Space()
FPS = 60
space.gravity = 0, 1000

def convert_coordinates(point):
    return point[0], 800 - point[1]

body = pm.Body()
body.position = 200, 200
shape = pm.Circle(body, 10)
shape.density = 1
space.add(body, shape)

def game():
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        display.fill(bg_color)
        x, y = convert_coordinates(body.position)
        pg.draw.circle(display, (255, 0, 0), body.position, 20)
        pg.display.update()
        clock.tick(FPS)
        space.step(1/FPS)

game()
pg.quit()

