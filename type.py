import pygame, sys, keyboard

pygame.init()
screen = pygame.display.set_mode((512, 256))
clock = pygame.time.Clock()
pygame.display.set_caption('Typer')
game_active = True
word = 'Hello world. I am here.'
spaces = 0

word_font = pygame.font.Font('platformer/resources/font/PixelOperator-Bold.ttf', 30)
word_text = word_font.render(str(word), False, 'Black')
word_rect = word_text.get_rect(center = (256, 128))

keys = {'space': pygame.K_SPACE, 'a': pygame.K_a, 'e': pygame.K_e}

for i in word:
    if i == ' ':
        spaces += 1

print(spaces)

while game_active:
    for event in pygame.event.get():
        key = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        for i in word:
            if keyboard.is_pressed(i):
                print(i)
    
    screen.fill(pygame.Color('White'))
    screen.blit(word_text, word_rect)

    pygame.display.update()
    clock.tick(60)