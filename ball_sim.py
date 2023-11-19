import pygame as pg
import pymunk as pm

pg.init()

display = pg.display.set_mode((800, 800))
clock = pg.time.Clock()
space = pm.Space()
FPS = 60

def game():
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        pg.display.update()
        clock.tick(FPS)
        space.step(1/FPS)

game()
pg.quit()

