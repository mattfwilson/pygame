import pygame as pg
from sys import exit

pg.init() # initializes pygame
SCREEN = pg.display.set_mode((800, 600)) # creates main screen display dimensions

while True:
    for event in pg.event.get(): # get all possible events in pg library
        if event.type == pg.QUIT: # get even to allow closing the pg window
            pg.quit() # quits out of pygame
            exit() # quits/break out of loop on system level (otherwise will throw video system no initialized error)
    pg.display.update() # updates pg.display.set_mode()