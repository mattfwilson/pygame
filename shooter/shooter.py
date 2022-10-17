from glob import escape
import pygame as pg
from sys import exit
import random

pg.init() # initializes pygame
SCREEN = pg.display.set_mode((2560, 1440))
CLOCK = pg.time.Clock()
pg.display.set_caption('Shooter v1.0')
score_font = pg.font.Font(None, 60)

score = 0
score_surf = score_font.render('Score:', False, 'White')
score_num_surf = score_font.render(str(score), True, 'White')

bg_surf = pg.image.load('bg.png').convert_alpha()

bird_x_pos = 2500
bird_y_pos = 420
bird_vel = 3
bird_surf = pg.image.load('bird.png').convert_alpha()
bird_rect = bird_surf.get_rect(center = (bird_x_pos, bird_y_pos))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        if event.type ==  pg.KEYDOWN:
            pg.quit()
            exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            if bird_rect.collidepoint(event.pos):
                score += 1
                score_num_surf = score_font.render(str(score), False, 'White')
                print('Hit!')
            else:
                print('Nothing...')

    SCREEN.blit(bg_surf, (0, 0))
    SCREEN.blit(score_surf, (40, 40))
    SCREEN.blit(score_num_surf, (180, 42))

    bird_rect.x -= bird_vel
    if bird_rect.right <= 0:
        bird_vel = random.randint(5, 10)
        bird_rect.top = random.randint(300, 1200)
        bird_rect.left = 2560
    SCREEN.blit(bird_surf, bird_rect)


    pg.display.update()
    CLOCK.tick(60)