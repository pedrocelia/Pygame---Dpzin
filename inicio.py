import pygame
import random
from os import path

from config_fut import *
screen = pygame.display.set_mode((WIDTH1, HEIGHT1))
def init_screen_(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    background = pygame.image.load(path.join(img_dir, 'inicio2.png')).convert()
    background_rect = background.get_rect()
    pygame.mixer.music.load(path.join(snd_dir, 'espera.mp3'))
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(1)
    pygame.event.wait()
    running = True
    while running:
        
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        
        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                pygame.quit()
                running = False

            if event.type == pygame.KEYUP:
                    state = FUT
                    running = False

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state