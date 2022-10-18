from glob import escape
import pygame
import sys
import random

SCREEN = pygame.display.set_mode((2560, 1440))
CLOCK = pygame.time.Clock()
GRAVITY = 1
main = True
pygame.init() # initializes pygame
pygame.display.set_caption('Bop\'em v1.0')
score_font = pygame.font.Font(None, 60)

juh_score = 0
juh_score_surf = score_font.render('Janelles:', False, 'Black')
juh_score_num_surf = score_font.render(str(juh_score), True, 'Black')

matt_score = 0
matt_score_surf = score_font.render('Matts:', False, 'Black')
matt_score_num_surf = score_font.render(str(matt_score), True, 'Black')

escapes = 0
esc_surf = score_font.render('Escapes:', False, 'Black')
esc_num_surf = score_font.render(str(escapes), True, 'Black')

bg_surf = pygame.image.load('bg.png').convert_alpha()

juh_pos = (2500, 520)
juh_vel = random.randint(12, 25)
juh_surf = pygame.image.load('janelle.png').convert_alpha()
juh_rect = juh_surf.get_rect(center=juh_pos)

matt_pos = (2500, 200)
matt_vel = random.randint(12, 25)
matt_surf = pygame.image.load('matt.png').convert_alpha()
matt_rect = matt_surf.get_rect(center=matt_pos)

def respawn(enemy, vel):
    vel = random.randint(10, 25)
    enemy.top = random.randint(300, 1200)
    enemy.left = 2560
    return vel

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
            if juh_rect.collidepoint(event.pos):
                respawn(juh_rect, juh_vel)
                juh_score += 1
                juh_score_num_surf = score_font.render(str(juh_score), False, 'Black')
                print('You bopped Janelle!')
            elif matt_rect.collidepoint(event.pos):
                respawn(matt_rect, matt_vel)
                matt_score += 1
                matt_score_num_surf = score_font.render(str(matt_score), False, 'Black')
                print('You bopped Matt!')
            else:
                print('Nothing...')

    SCREEN.blit(bg_surf, (0, 0))
    SCREEN.blit(juh_score_surf, (40, 40))
    SCREEN.blit(juh_score_num_surf, (240, 42))
    SCREEN.blit(matt_score_surf, (1000, 40))
    SCREEN.blit(matt_score_num_surf, (1150, 42))

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