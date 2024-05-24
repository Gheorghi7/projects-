import pygame
import sys

pygame.init()


screan_weigh, screen_height = 800, 600
screen = pygame.display.set_mode((screan_weigh, screen_height))

pygame.display.set_caption("Shooter")


rect_wight, rect_height = 75, 75
rect_x = screan_weigh/2 - rect_wight/2
rect_y = screen_height/2 - rect_height/2

STEP = 10

while True:

    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and rect_y >= STEP:
                rect_y = rect_y - STEP
            if event.key == pygame.K_DOWN and rect_y <= screen_height - rect_height - STEP:
                rect_y = rect_y + STEP
            if event.key == pygame.K_LEFT and rect_x >= STEP:
                rect_x -= STEP
            if event.key == pygame.K_RIGHT and rect_x <= screan_weigh - rect_wight - STEP:
                rect_x += STEP


    screen.fill(pygame.Color('dimgrey'))

    body = pygame.draw.rect(screen, pygame.Color('forestgreen'), (rect_x, rect_y,rect_wight,rect_height))

    pygame.display.update()


