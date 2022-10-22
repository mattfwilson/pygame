import pygame, sys

pygame.init()
screen = pygame.display.set_mode((1200, 768))
clock = pygame.time.Clock()
pygame.display.set_caption('Typer')
game_active = True
word = 'Hello'

word_font = pygame.font.Font('platformer/resources/font/PixelOperator-Bold.ttf', 30)
word_text = word_font.render(str(word), False, 'Black')
word_rect = word_text.get_rect()

while game_active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(pygame.Color('White'))
    screen.blit(word_text, word_rect)
    pygame.draw.rect(screen, 'Red', [50, 100, 50, 50], 0)

    pygame.display.update()
    clock.tick(60)