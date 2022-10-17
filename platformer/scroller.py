import pygame as pg
from sys import exit

pg.init() # initializes pygame
SCREEN = pg.display.set_mode((800, 512)) # creates main screen display dimensions
CLOCK = pg.time.Clock() # creates pygame clock
pg.display.set_caption('Platformer v1.0') # renames the title of the pygame window
test_font = pg.font.Font(None, 30) # creates font surface (font-family, font-size)

surf_color = pg.Surface((50, 50)) # create simple surface with color
surf_color.fill('White') # create color for suface var
surf_bg = pg.image.load('resources/bg.png') # create an image surface
surf_ground = pg.image.load('resources/ground.png')
surf_font = test_font.render('Score:', False, 'White') # creates font attributes (string, anti-aliasing, color)

while True: # perpetual loop to keep the game running
    for event in pg.event.get(): # get all possible events in pg library
        if event.type == pg.QUIT: # get even to allow closing the pg window
            pg.quit() # quits out of pygame
            exit() # quits out of loop on system level (otherwise throws vid sys no initialized error)
    
    SCREEN.blit(surf_color, (200, 100)) # blit = block image transfer (renders in call order)
    SCREEN.blit(surf_bg, (0, 0)) # placement of image along x and y
    SCREEN.blit(surf_ground, (0, 416))
    SCREEN.blit(surf_font, (20, 18)) # placement of font along x and y
    
    pg.display.update() # updates pg.display.set_mode()
    CLOCK.tick(60) # tells while loop to not run faster than 60fps 