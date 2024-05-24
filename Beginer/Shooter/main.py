import pygame
import sys
from random import randint

pygame.init()
game_font = pygame.font.Font(None, 30)
STEP = 0.3
ROCKET_STEP = 0.4
ALIAN_STEP = 0.025
alian_speed = ALIAN_STEP
# SCREEN
screen_height, screen_widht = 600, 1000
pygame.display.set_caption('Shooter')
screen = pygame.display.set_mode((screen_widht, screen_height))

# MAIN CHARACTER
fighter_image = pygame.image.load('images/fighter.png')
fighter_width, fighter_height = fighter_image.get_size()
# ROCKET
rocket_image = pygame.image.load('images/rocket.png')
rocket_width, rocket_height = rocket_image.get_size()
# ALIEN
alien_image = pygame.image.load('images/alien.png')
alien_width, alien_height = alien_image.get_size()

# ALIEN POSITION
alien_x = randint(0, screen_widht - alien_width)
alien_y = 0
# CHARACTER POSITION
fighter_y = screen_height - fighter_height
fighter_x = screen_widht / 2 - fighter_width / 2
# ROCKET POSITION
rocket_x = fighter_x + fighter_width / 2 + rocket_width / 2
rocket_y = fighter_y - rocket_height

# MOVING
character_move_left, character_move_rigt = False, False
rocked_was_fired = False

game_is_runing = True
game_score = 0
while game_is_runing:
    # TRACK MOUCE
    for event in pygame.event.get():
        # EXIT
        if event.type == pygame.QUIT:
            sys.exit()
        # MOVING
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_move_left = True
            if event.key == pygame.K_RIGHT:
                character_move_rigt = True
            if event.key == pygame.K_SPACE:
                rocked_was_fired = True
                rocket_x = fighter_x + fighter_width / 2 + rocket_width / 2
                rocket_y = fighter_y - rocket_height

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                character_move_left = False
            if event.key == pygame.K_RIGHT:
                character_move_rigt = False

    if character_move_left and fighter_x >= STEP:
        fighter_x -= STEP
    if character_move_rigt and fighter_x <= screen_widht - fighter_width - STEP:
        fighter_x += STEP
    alien_y += alian_speed
    if rocked_was_fired and rocket_y + rocket_height < 0:
        rocked_was_fired = False

    if rocked_was_fired:
        rocket_y -= ROCKET_STEP
    # SCREEN UPDATES
    screen.fill(pygame.Color('darkslategrey'))
    screen.blit(fighter_image, (fighter_x, fighter_y))
    screen.blit(alien_image, (alien_x, alien_y))
    if rocked_was_fired:
        screen.blit(rocket_image, (rocket_x, rocket_y))
    game_score_text = game_font.render(f"Your score:{game_score}", True, 'white')
    screen.blit(game_score_text, (20, 20))
    pygame.display.update()

    if alien_y + alien_height > fighter_y:
        game_is_runing = False
    if rocked_was_fired and \
            alien_x < rocket_x < alien_x + alien_width - rocket_width and \
            alien_y < rocket_y < alien_y + alien_height - rocket_height:
        rocked_was_fired = False
        alien_x = randint(0, screen_widht - alien_width)
        alien_y = 0
        alian_speed += ALIAN_STEP / 2
        game_score += 100

game_over_text = game_font.render("Game over", True, 'white')
game_over_rectangle = game_over_text.get_rect()
game_over_rectangle.center = (screen_widht / 2, screen_height / 2)
screen.blit(game_over_text, game_over_rectangle)
pygame.display.update()
pygame.time.wait(5000)
pygame.quit()
