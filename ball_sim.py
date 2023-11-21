import pygame as pg
import pymunk as pm

pg.init()

DISPLAY = pg.display.set_mode((800, 800))
BG_COLOR = (255, 255, 255)
CLOCK = pg.time.Clock()
SPACE = pm.Space()
FPS = 60

def print_text(text, pos, color, size, family):
    font = pg.font.SysFont(family, size, True, False)
    surface = font.render(text, True, color)
    DISPLAY.blit(surface, pos)

def Ball():
    def __init__(self, x, y):
        self.body = pm.Body()
        self.body.position = x, y
        self.shape = pm.Circle(self.body, 10)
        self.shape.elasticity = 1
        self.shape.density = 1

def game():
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        DISPLAY.fill(BG_COLOR)
        print_text('Ball Simulator', (230, 350), (255, 0, 0), 50, 'Times New Roman')
        print_text('Maximize your balls', (275, 410), (96, 96, 96), 24, 'Arial')
        pg.display.update()
        CLOCK.tick(FPS)
        SPACE.step(1/FPS)

game()
pg.quit()

