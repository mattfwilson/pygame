import pygame as pg
from sys import exit

pg.init() # initializes pygame
SCREEN = pg.display.set_mode((800, 512)) # creates main screen display dimensions
CLOCK = pg.time.Clock() # creates pygame clock
pg.display.set_caption('Platformer v1.0') # renames the title of the pygame window
score_font = pg.font.Font('resources/font/PixelOperator-Bold.ttf', 30) # creates font surface (font-family, font-size)

score = 0
score_surf = score_font.render('Score:', False, 'White') # creates font attributes (string, anti-aliasing, color)
score_num_surf = score_font.render(str(score), False, 'White') # creates font attributes (string, anti-aliasing, color)

bg_surf = pg.image.load('resources/bg.png') # create an image surface
ground_surf = pg.image.load('resources/ground.png')

player_surf = pg.image.load('resources/char.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80, 420))

sloth_x_pos = 700
sloth_y_pos = 420
sloth_surf = pg.image.load('resources/enemy_sloth.png').convert_alpha() # creates font attributes (string, anti-aliasing, color)
sloth_rect = sloth_surf.get_rect(bottomright = (sloth_x_pos, sloth_y_pos))

while True: # perpetual loop to keep the game running
    for event in pg.event.get(): # get all possible events in pg library
        if event.type == pg.QUIT: # get even to allow closing the pg window
            pg.quit() # quits out of pygame
            exit() # quits out of loop on system level (otherwise throws vid sys no initialized error)
        if event.type == pg.MOUSEMOTION:
            if sloth_rect.collidepoint(event.pos):
                score += 1
                score_num_surf = score_font.render(str(score), False, 'White')
                print('Hit!')
        else:
            print('Nothing...')

    SCREEN.blit(bg_surf, (0, 0)) # placement of image along x and y
    SCREEN.blit(ground_surf, (0, 416))

    SCREEN.blit(score_surf, (20, 18))
    SCREEN.blit(score_num_surf, (115, 18))

    SCREEN.blit(player_surf, player_rect)

    sloth_rect.x -= 3
    if sloth_rect.right <= 0: # checks if right side of surf meets conditional
        sloth_rect.left = 800 # repositions surf based on the left side of rect
    SCREEN.blit(sloth_surf, sloth_rect)

    # if player_rect.colliderect(sloth_rect): # check if one rect collides with another rect
    #     print(f'You are getting pwned!')

    pg.display.update() # updates pg.display.set_mode()
    CLOCK.tick(60) # tells while loop to not run faster than 60fps 