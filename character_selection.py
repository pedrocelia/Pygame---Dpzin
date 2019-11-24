
import pygame

import random
from os import path
import time

from config_fut import *
from config import *


from inicio import init_screen_
personagem1= "Luigi"
personagem2 = "Skull"
def p1_select(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    background = pygame.image.load(path.join(img_dir, 'p1.png')).convert()
    background_rect = background.get_rect()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                running = False
        pygame.display.update()
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        clock.tick(15) 

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()


def char_screen_p1(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    background = pygame.image.load(path.join(img_dir, 'charselect.png')).convert()
    background_rect = background.get_rect()

    running = True
    while running:


        
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        
        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    state = QUIT
                    running  = False
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
               
                #Direita Inferior
                if 342 > pos[0] > 54 and 703 > pos[1] > 158:
                    personagem1 = Miranha
                    return personagem1
                    running = False

                #Esquerda Superior
                if 960 > pos[0] > 674 and 703 > pos[1] > 158:
                    personagem1 = Luigi
                    return personagem1    
                    running = False
                #Canto Superior Esquerdo
                if 649 > pos[0] > 367 and 703 > pos[1] > 158:
                    personagem1 = Mario
                    return personagem1
                    running = False            
        
        # A cada loop, redesenha o fundo e os sprites
        
        pygame.display.update()
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        clock.tick(15) 

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

def char_screen_p2(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    background = pygame.image.load(path.join(img_dir, 'charselect.png')).convert()
    background_rect = background.get_rect()

    running = True
    while running:


        
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        
        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False
                pygame.quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    state = QUIT
                    running  = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print(pos)
               
                #Direita Inferior
                if 342 > pos[0] > 54 and 703 > pos[1] > 158:
                    personagem2 = Miranha
                    running = False
                #Esquerda Superior
                if 960 > pos[0] > 674 and 703 > pos[1] > 158:
                    personagem2 = Luigi    
                    running = False
                #Canto Superior Esquerdo
                if 649 > pos[0] > 367 and 703 > pos[1] > 158 :
                    personagem2 = Mario
                    running = False
                
        
#            
        # A cada loop, redesenha o fundo e os sprites
        
        pygame.display.update()
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        clock.tick(15) 

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
    return personagem2


def p2_select(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    background = pygame.image.load(path.join(img_dir, 'p2.png')).convert()
    background_rect = background.get_rect()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                running = False
        pygame.display.update()
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        clock.tick(15) 

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

