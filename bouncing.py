import pygame as pg

pg.init()

DISPLAY = pg.display.set_mode((800, 800))
BG_COLOR = (255, 255, 255)
ORANGE_COLOR = (204, 102, 0)
BLUE_COLOR = (0, 76, 153)
RED_COLOR = (102, 0, 0)
GREEN_COLOR = (0, 102, 51)
CLOCK = pg.time.Clock()
FPS = 60
ACCELERATION = .5

class Ball():
    def __init__(self):
        self.y = 250
        self.velocity = 10

    def draw(self):
        pg.draw.circle(DISPLAY, ORANGE_COLOR, (400, int(self.y)), 30)
    
    def move(self):
        self.velocity += ACCELERATION
        self.y += self.velocity
        if self.y >= 450:
            self.velocity = -self.velocity

class Square():
    def __init__(self):
        self.y = 250
        self.velocity = 10

    def draw(self):
        pg.draw.rect(DISPLAY, BLUE_COLOR, [200, int(self.y), 50, 50])
    
    def move(self):
        self.velocity += ACCELERATION
        self.y += self.velocity
        if self.y >= 450:
            self.velocity = -self.velocity

class Triangle():
    def __init__(self):
        self.y = 250
        self.velocity = 10

    def draw(self):
        pg.draw.polygon(DISPLAY, RED_COLOR, [[550, self.y], [600, self.y], [575, self.y-50]])
    
    def move(self):
        self.velocity += ACCELERATION
        self.y += self.velocity
        if self.y >= 450:
            self.velocity = -self.velocity

def game():
    ball = Ball()
    square = Square()
    triangle = Triangle()
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        ball.move()
        square.move()
        triangle.move()
        DISPLAY.fill(BG_COLOR)
        pg.draw.line(DISPLAY, GREEN_COLOR, (0, 650), (1000, 650), 300)
        ball.draw()
        square.draw()
        triangle.draw()

        pg.display.update()
        CLOCK.tick(FPS)

game()
pg.quit()

