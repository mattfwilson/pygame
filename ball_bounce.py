import pygame as pg

pg.init()

DISPLAY = pg.display.set_mode((800, 800))
BG_COLOR = (255, 255, 255)
BALL_COLOR = (204, 102, 0)
GROUND_COLOR = (0, 102, 51)
CLOCK = pg.time.Clock()
FPS = 60
ACCELERATION = 1

class Ball():
    def __init__(self):
        self.y = 200
        self.velocity = 15

    def draw(self):
        pg.draw.circle(DISPLAY, BALL_COLOR, (400, int(self.y)), 40)
    
    def move(self):
        self.velocity += ACCELERATION
        self.y += self.velocity
        if self.y >= 440:
            self.velocity = -self.velocity

def game():
    ball = Ball()
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        ball.move()

        DISPLAY.fill(BG_COLOR)
        pg.draw.line(DISPLAY, GROUND_COLOR, (0, 650), (1000, 650), 300)
        ball.draw()

        pg.display.update()
        CLOCK.tick(FPS)

game()
pg.quit()

