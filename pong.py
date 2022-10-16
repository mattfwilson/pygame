import pygame

BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
SCREEN = pygame.display.set_mode((640, 480))

pygame.init()
pygame.display.set_caption('Collision')

# create the ball and paddles rects
ball = pygame.Rect(300, 230, 15, 15)
left_pad = pygame.Rect(20, 210, 15, 80)
right_pad = pygame.Rect(600, 210, 15, 80)
pads = [left_pad, right_pad]
velocity_x = 0.1
velocity_y = 0.5
clock = pygame.time.Clock()
x = 30
y = 40

class RightPaddle(object):
    def __init__(self):
        self.rect = pygame.draw.rect(SCREEN, WHITE, pads[1])

    def handle_keys(self):
        key = pygame.key.get_pressed()
        dist = 1
        if key[pygame.K_LEFT]:
           self.rect.move(-1, 0)
        if key[pygame.K_RIGHT]:
           self.rect.move(1, 0)
        if key[pygame.K_UP]:
           self.rect.move(0, -1)
        if key[pygame.K_DOWN]:
           self.rect.move(0, 1)

while True:
    dt = clock.tick(30)

    event = pygame.event.poll()

    right = RightPaddle()

    if event.type == pygame.QUIT:
        break

    # use the move function inplace
    ball.move_ip(velocity_x * dt, 0)


    # check for collision with the pads
    if ball.collidelist(pads) >= 0:
        velocity_x = -velocity_x

    SCREEN.fill(BLACK)

    # draw using the rect
    pygame.draw.rect(SCREEN, WHITE, ball)

    # draw the pads
    for pad in pads:
        pygame.draw.rect(SCREEN, WHITE, pad)
        pygame.display.update()

    pygame.display.flip()