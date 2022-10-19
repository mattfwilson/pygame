from asyncio.windows_events import NULL
from multiprocessing import Event
import pygame as pg
from sys import exit

pg.init() # initializes pygame
SCREEN = pg.display.set_mode((800, 512)) # creates main screen display dimensions
CLOCK = pg.time.Clock() # creates pygame clock
pg.display.set_caption('Platformer v1.0') # renames the title of the pygame window
score_font = pg.font.Font('resources/font/PixelOperator-Bold.ttf', 30) # creates font surface (font-family, font-size)

score = 0
score_surf = score_font.render('Score:', False, 'White') # creates font attributes (string, anti-aliasing, color)
score_rect = score_surf.get_rect(center = (90, 32))
score_num_surf = score_font.render(str(score), False, 'White') # creates font attributes (string, anti-aliasing, color)

sky_surf = pg.image.load('resources/bg.png') # create an image surface
ground_surf = pg.image.load('resources/ground.png')

player_surf = pg.image.load('resources/char.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (150, 420))
gravity = 0

sloth_x_pos = 700
sloth_y_pos = 420
sloth_surf = pg.image.load('resources/enemy_sloth.png').convert_alpha() # creates font attributes (string, anti-aliasing, color)
sloth_rect = sloth_surf.get_rect(bottomright = (sloth_x_pos, sloth_y_pos))


while True: # perpetual loop to keep the game running
    for event in pg.event.get(): # get all possible events in pg library
        key = pg.key.get_pressed()
        if event.type == pg.QUIT: # get event to allow closing the pg window
            pg.quit() # quits out of pygame
            exit() # quits out of loop on system level (otherwise throws vid sys no initialized error)
        if event.type == pg.MOUSEBUTTONDOWN:
            if sloth_rect.collidepoint(event.pos):
                score += 1
                score_num_surf = score_font.render(str(score), False, 'White')
                print('Hit!')
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE and player_rect.bottom >= 300:
                gravity = -20
                print('jumping')
        if key[pg.K_a]:
            player_rect.x -= 15
            print('moving right')
        if key[pg.K_d]:
            player_rect.x += 15
            print('moving left')
        if event.type == pg.KEYUP:
            print('released key')

    # bgs and score
    SCREEN.blit(sky_surf, (0, 0)) # placement of image along x and y
    SCREEN.blit(ground_surf, (0, 416))
    score_bg = pg.draw.line(SCREEN, '#000000', (0, 30), (800, 30), 60) # (display surface, color, start point, end point)
    SCREEN.blit(score_num_surf, (110, 13))
    SCREEN.blit(score_surf, (20, 12)) # (display surface, color of rect, rect to be created)
     
    # player
    gravity += 1
    player_rect.y += gravity
    if player_rect.bottom >= 420:
        player_rect.bottom = 420
    SCREEN.blit(player_surf, player_rect)
    
    # collision
    # if sloth_rect.colliderect(player_rect):
    #     pg.quit()
    #     exit()
    
    # enemy
    sloth_rect.x -= 3 # tells rect to move designated amount on x axis
    if sloth_rect.right <= 0: # checks if right side of surface meets conditional
        sloth_rect.left = 800 # repositions surface based on the left side of rect
    SCREEN.blit(sloth_surf, sloth_rect)

    pg.display.update() # updates pg.display.set_mode()
    CLOCK.tick(60) # tells while loop to not run faster than 60fps 