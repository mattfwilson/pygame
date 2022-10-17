import pygame as pg
from sys import exit

pg.init() # initializes pygame
SCREEN = pg.display.set_mode((800, 512)) # creates main screen display dimensions
CLOCK = pg.time.Clock() # creates pygame clock
pg.display.set_caption('Platformer v1.0') # renames the title of the pygame window
score_font = pg.font.Font('resources/font/PixelOperator-Bold.ttf', 30) # creates font surface (font-family, font-size)

bg_surf = pg.image.load('resources/bg.png') # create an image surface
ground_surf = pg.image.load('resources/ground.png')
sloth_surf = pg.image.load('resources/enemy_sloth.png').convert_alpha() # creates font attributes (string, anti-aliasing, color)
sloth_x_pos = 700

score = 0
score_surf = score_font.render('Score:', False, 'White') # creates font attributes (string, anti-aliasing, color)
score_num_surf = score_font.render(str(score), False, 'White') # creates font attributes (string, anti-aliasing, color)

player_surf = pg.image.load('resources/char.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80, 420))

while True: # perpetual loop to keep the game running
    for event in pg.event.get(): # get all possible events in pg library
        if event.type == pg.QUIT: # get even to allow closing the pg window
            pg.quit() # quits out of pygame
            exit() # quits out of loop on system level (otherwise throws vid sys no initialized error)
    
    SCREEN.blit(bg_surf, (0, 0)) # placement of image along x and y
    SCREEN.blit(ground_surf, (0, 416))
    sloth_x_pos -= 3
    if sloth_x_pos < -64:
        sloth_x_pos = 800
    SCREEN.blit(score_surf, (20, 18))
    SCREEN.blit(score_num_surf, (115, 18))
    SCREEN.blit(sloth_surf, (sloth_x_pos, 358))
    SCREEN.blit(player_surf, player_rect)
    
    pg.display.update() # updates pg.display.set_mode()
    CLOCK.tick(60) # tells while loop to not run faster than 60fps 