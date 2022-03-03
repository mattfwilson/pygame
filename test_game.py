# Import and initialize the pygame library
import pygame as pg
pg.init()

# Set up the drawing window
bg = pg.display.set_mode([624 , 720])
color_inactive = pg.Color('green')
color_inactive = pg.Color('gray')

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Fill the background with white
    color = (255, 255, 255)
    bg.fill(color)

    # draws squares by row
    pg.draw.rect(bg, color_inactive, pg.Rect(80, 80, 80, 80))
    pg.draw.rect(bg, color_inactive, pg.Rect(176, 80, 80, 80))
    pg.draw.rect(bg, color_inactive, pg.Rect(272, 80, 80, 80))
    pg.draw.rect(bg, color_inactive, pg.Rect(368, 80, 80, 80))
    pg.draw.rect(bg, color_inactive, pg.Rect(462, 80, 80, 80))

    pg.draw.rect(bg, color_inactive, pg.Rect(80, 176, 80, 80))
    pg.draw.rect(bg, color_inactive, pg.Rect(176, 176, 80, 80))
    pg.draw.rect(bg, color_inactive, pg.Rect(272, 176, 80, 80))
    pg.draw.rect(bg, color_inactive, pg.Rect(368, 176, 80, 80))
    pg.draw.rect(bg, color_inactive, pg.Rect(462, 176, 80, 80))

    pg.draw.rect(bg, color_inactive, pg.Rect(80, 272, 80, 80))
    pg.draw.rect(bg, color_inactive, pg.Rect(176, 272, 80, 80))
    pg.draw.rect(bg, color_inactive, pg.Rect(272, 272, 80, 80))
    pg.draw.rect(bg, color_inactive, pg.Rect(368, 272, 80, 80))
    pg.draw.rect(bg, color_inactive, pg.Rect(462, 272, 80, 80))

    pg.draw.rect(bg, color_inactive, pg.Rect(80, 368, 80, 80))
    pg.draw.rect(bg, color_inactive, pg.Rect(176, 368, 80, 80))
    pg.draw.rect(bg, color_inactive, pg.Rect(272, 368, 80, 80))
    pg.draw.rect(bg, color_inactive, pg.Rect(368, 368, 80, 80))
    pg.draw.rect(bg, color_inactive, pg.Rect(462, 368, 80, 80))

    pg.draw.rect(bg, color_inactive, pg.Rect(80, 462, 80, 80))
    pg.draw.rect(bg, color_inactive, pg.Rect(176, 462, 80, 80))
    pg.draw.rect(bg, color_inactive, pg.Rect(272, 462, 80, 80))
    pg.draw.rect(bg, color_inactive, pg.Rect(368, 462, 80, 80))
    pg.draw.rect(bg, color_inactive, pg.Rect(462, 462, 80, 80))

    pg.draw.rect(bg, color_inactive, pg.Rect(80, 558, 80, 80))
    pg.draw.rect(bg, color_inactive, pg.Rect(176, 558, 80, 80))
    pg.draw.rect(bg, color_inactive, pg.Rect(272, 558, 80, 80))
    pg.draw.rect(bg, color_inactive, pg.Rect(368, 558, 80, 80))
    pg.draw.rect(bg, color_inactive, pg.Rect(462, 558, 80, 80))

    # Flip the display
    pg.display.flip()

# Done! Time to quit.
pg.quit()
