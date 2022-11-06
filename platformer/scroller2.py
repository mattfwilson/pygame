import pygame as pg
from sys import exit

pg.init()
screen = pg.display.set_mode((800, 512))
clock = pg.time.Clock()
pg.display.set_caption('Sloth Hopper')
score_font = pg.font.Font('resources/font/PixelOperator-Bold.ttf', 30)
title_font = pg.font.Font('resources/font/PixelOperator-Bold.ttf', 64)
game_active = False
start_time = 0
gravity = 0

score = 0
score_surf = score_font.render('Score:', False, 'White')
score_rect = score_surf.get_rect(center = (90, 32))
score_num_surf = score_font.render(str(score), False, 'White')

sky_surf = pg.image.load('resources/bg.png')
ground_surf = pg.image.load('resources/ground.png')

player_surf = pg.image.load('resources/char.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (150, 420))

sloth_x_pos = 700
sloth_y_pos = 420
sloth_surf = pg.image.load('resources/enemy_sloth.png').convert_alpha()
sloth_rect = sloth_surf.get_rect(bottomright = (sloth_x_pos, sloth_y_pos))

# intro
player_stand = pg.image.load('resources/char.png').convert_alpha()
player_stand = pg.transform.scale(player_stand, (400, 600))
player_stand_rect = player_stand.get_rect(center = (120, 256))

game_name = title_font.render('Sloth Hopper', False, (112, 200, 160))
game_name_rect = game_name.get_rect(center = (550, 230))

game_instruct = score_font.render('Press Space to play', False, 'White')
game_instruct_rect = game_instruct.get_rect(center = (545, 286))

def display_score(score_font):
    current = int(pg.time.get_ticks() / 1000) - start_time
    score_surf = score_font.render(f'Score: {current}', False, 'White')
    score_rect = score_surf.get_rect(center = (400, 32))
    screen.blit(score_surf, score_rect)

while True:
    for event in pg.event.get():
        key = pg.key.get_pressed()
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        if game_active:
            if event.type == pg.MOUSEBUTTONDOWN:
                if sloth_rect.collidepoint(event.pos):
                    score += 1
                    score_num_surf = score_font.render(str(score), False, 'White')
                    print('Hit!')
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    game_active = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE and player_rect.bottom >= 300:
                    gravity = -20
                    print('jumping')
            if key[pg.K_a]:
                player_rect.x -= 15
                print('moving left')
            if key[pg.K_d]:
                player_rect.x += 15
                print('moving right')
            if event.type == pg.KEYUP:
                print('released key')
        else:
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                game_active = True
                start_time = int(pg.time.get_ticks() / 1000)

    if game_active:
        # bgs and score
        screen.blit(sky_surf, (0, 0))
        screen.blit(ground_surf, (0, 416))
        display_score(score_font)
        
        # player
        gravity += 1
        player_rect.y += gravity
        if player_rect.bottom >= 420:
            player_rect.bottom = 420
        screen.blit(player_surf, player_rect)

        # enemy
        sloth_rect.x -= 5
        if sloth_rect.right <= 0:
            sloth_rect.left = 800
        screen.blit(sloth_surf, sloth_rect)

        if sloth_rect.colliderect(player_rect):
            game_active = False
            sloth_rect.left = 800
    else:
        screen.fill((84, 129, 80))
        screen.blit(player_stand, player_stand_rect)
        screen.blit(game_name, game_name_rect)
        screen.blit(game_instruct, game_instruct_rect)

    pg.display.update()
    clock.tick(60)