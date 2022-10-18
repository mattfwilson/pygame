from glob import escape
import pygame
import sys
import random

main = True
pygame.init() # initializes pygame
SCREEN = pygame.display.set_mode((2560, 1440))
CLOCK = pygame.time.Clock()
GRAVITY = 1
pygame.display.set_caption('Shooter v1.0')
score_font = pygame.font.Font(None, 60)

score = 0
score_surf = score_font.render('Score:', False, 'Black')
score_num_surf = score_font.render(str(score), True, 'Black')

bg_surf = pygame.image.load('bg.png').convert_alpha()

bird_pos = (2500, 520)
bird_vel = random.randint(10, 20)
bird_surf = pygame.image.load('bird.png').convert_alpha()
bird_rect = bird_surf.get_rect(center=bird_pos)

def respawn(vel):
    vel = random.randint(10, 20)
    bird_rect.top = random.randint(300, 1200)
    bird_rect.left = 2560
    return vel

class Enemy():

    def __init__(self, screen, pos):
        super().__init__()
        self.screen = screen
        pygame.image.load('bird.png').convert_alpha()
        self.bird_surf.get_rect(center=bird_pos)
        self.rect = self.image.get_rect(center=pos)
        self.pos_y = pos[1]
        self.speed_y = 0

    def update(self):
        self.speed_y += GRAVITY
        self.pos_y += self.speed_y
        self.rect.y = self.pos_y

        if self.pos_y > self.screen.get_height():
            self.kill()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            try:
                sys.exit()
            finally:
                main = False
        if event.type ==  pygame.KEYDOWN:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if bird_rect.collidepoint(event.pos):
                respawn(bird_vel)
                score += 1
                score_num_surf = score_font.render(str(score), False, 'Black')
                print('Hit!')
            else:
                print('Nothing...')

    SCREEN.blit(bg_surf, (0, 0))
    SCREEN.blit(score_surf, (40, 40))
    SCREEN.blit(score_num_surf, (180, 42))

    bird_rect.x -= bird_vel
    if bird_rect.right <= 0:
        respawn(bird_vel)
    SCREEN.blit(bird_surf, bird_rect)

    pygame.display.update()
    CLOCK.tick(60)