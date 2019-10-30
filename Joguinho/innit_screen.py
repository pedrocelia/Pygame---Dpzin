import pygame
from os import path

from config import img_dir, BLACK, FPS, GAME, QUIT, SELECT, WIDTH, HEIGHT


def init_screen(screen):
    clock = pygame.time.Clock()

    background = pygame.image.load(path.join(img_dir, 'inicio1.png')).convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    background_rect = background.get_rect()

    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                running = False
            if event.type == pygame.KEYUP:
                state = SELECT
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    state = QUIT
                    running  = False
                    
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        pygame.display.flip()

    return state

