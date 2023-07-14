# test
import pygame
import sys
import random
import itertools

SCREEN = pygame.display.set_mode((1440, 960))
CLOCK = pygame.time.Clock()
GRAVITY = 1
main = True
pygame.init() # initializes pygame
pygame.display.set_caption('Bop\'em v1.0')
gravity = 0

score_font = pygame.font.Font(None, 60)
bg_surf = pygame.image.load('bg.png').convert_alpha()

juh_score = 0
juh_score_surf = score_font.render('Janelles:', False, 'Black')
juh_score_num_surf = score_font.render(str(juh_score), True, 'Black')

matt_score = 0
matt_score_surf = score_font.render('Matts:', False, 'Black')
matt_score_num_surf = score_font.render(str(matt_score), True, 'Black')

escapes = 0
esc_surf = score_font.render('Escapes:', False, 'Black')
esc_num_surf = score_font.render(str(escapes), True, 'Black')

juh_pos = (1440, 520)
juh_vel = random.randint(5, 8)
juh_surf = pygame.image.load('janelle.png').convert_alpha()
juh_rect = juh_surf.get_rect(center=juh_pos)

matt_pos = (1440, 200)
matt_vel = random.randint(5, 8)
matt_surf = pygame.image.load('matt.png').convert_alpha()
matt_rect = matt_surf.get_rect(center=matt_pos)

class Enemy():
    id = itertools.count(0)
    def __init__(self):
        self.id = next(Enemy.id)

class Janelle(Enemy):
    def __init__(self):
        super().__init__()
        self.name = 'Janelle'

    def __repr__(self):
        return f'{self.name}, id: {self.id}'

def respawn(enemy, vel):
    vel = random.randint(10, 25)
    enemy.top = random.randint(300, 900)
    enemy.left = 1440
    return vel

def enemy_downed(enemy, gravity):
    gravity += 50
    enemy.y += gravity
    return enemy, gravity

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            try:
                sys.exit()
            finally:
                main = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if juh_rect.collidepoint(event.pos):
                juh_vel = respawn(juh_rect, gravity)
                juh_score += 1
                juh_score_num_surf = score_font.render(str(juh_score), False, 'Black')
                print('You bopped Janelle!')
            elif matt_rect.collidepoint(event.pos):
                matt_vel = respawn(matt_rect, matt_vel)
                matt_score += 1
                matt_score_num_surf = score_font.render(str(matt_score), False, 'Black')
                print('You bopped Matt!')
        if event.type ==  pygame.KEYDOWN:
            pygame.quit()
            exit()

    SCREEN.blit(bg_surf, (0, 0))
    SCREEN.blit(juh_score_surf, (40, 40))
    SCREEN.blit(juh_score_num_surf, (240, 42))
    SCREEN.blit(matt_score_surf, (1200, 40))
    SCREEN.blit(matt_score_num_surf, (1350, 42))

    print(Janelle())

    juh_rect.x -= juh_vel
    if juh_rect.right <= 0:
        respawn(juh_rect, juh_vel)
    SCREEN.blit(juh_surf, juh_rect)

    matt_rect.x -= matt_vel
    if matt_rect.right <= 0:
        respawn(matt_rect, matt_vel)
    SCREEN.blit(matt_surf, matt_rect)

    pygame.display.update()
    CLOCK.tick(60)
