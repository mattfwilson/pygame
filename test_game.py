# Import and initialize the pygame library
import pygame as pg
pg.init()

# Set up the drawing window
def main():
    clock = pg.time.Clock()
    bg = pg.display.set_mode([624 , 720])
    color_inactive = pg.Color('gray')
    color_active = pg.Color('green')
    color = color_inactive
    active = False
    done = False

# Run until the user asks to quit
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if color_inactive.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive

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

if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()