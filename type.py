import pygame, sys, keyboard

pygame.init()
screen = pygame.display.set_mode((512, 256))
clock = pygame.time.Clock()
pygame.display.set_caption('Typer')
game_active = True
word = 'hello'
mistakes = 0

word_font = pygame.font.Font('platformer/resources/font/PixelOperator-Bold.ttf', 30)
word_text = word_font.render(str(word), False, 'Black')
word_rect = word_text.get_rect(center = (256, 128))

while game_active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    for letter in word:
        if keyboard.press(letter) == keyboard.read_key():
            print(f'You pressed "{letter}" in the word!')
        else:
            print('Nothing...')
    break
    
    screen.fill(pygame.Color('White'))
    screen.blit(word_text, word_rect)

    pygame.display.update()
    clock.tick(60)