
import pygame

import random
from os import path
import time

from config_fut import *


from inicio import init_screen
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
    background = pygame.image.load(path.join(img_dir, 'charselect.jpg')).convert()
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
               
                #Direita Inferior
                if 676+285 > pos[0] > 676 and 469+281 > pos[1] > 469:
                    personagem1 = Miranha
                    return personagem1
                    running = False

                #Esquerda Superior
                if 367+285 > pos[0] > 367 and 161+281 > pos[1] > 161:
                    personagem1 = Luigi
                    return personagem1    
                    running = False
                #Canto Superior Esquerdo
                if 54+289 > pos[0] > 54 and 161+286 > pos[1] > 161:
                    personagem1 = Mario
                    return personagem1
                    running = False
                if 1165+168 > pos[0] > 1165 and 107 > pos[1] > 0:
                    personagem1 = Naruto
                    return personagem1
                    running = False
        pos = pygame.mouse.get_pos()
        #Direita Inferior
        if 676+285 > pos[0] > 676 and 469+281 > pos[1] > 469:
            #Miranha
            background = pygame.image.load(path.join(img_dir, 'charselect_miranha.png')).convert()
            background_rect = background.get_rect()
        #Esquerda Superior
        elif 367+285 > pos[0] > 367 and 161+281 > pos[1] > 161:
            #Luigi
            background = pygame.image.load(path.join(img_dir, 'charselect_luigi.png')).convert()
            background_rect = background.get_rect()
        #Canto Superior Esquerdo
        elif 54+289 > pos[0] > 54 and 161+286 > pos[1] > 161:
            #Mario
            background = pygame.image.load(path.join(img_dir, 'charselect_mario.png')).convert()
            background_rect = background.get_rect()
        elif 1165+168 > pos[0] > 1165 and 107 > pos[1] > 0:
            background = pygame.image.load(path.join(img_dir, 'charselect_ee.png')).convert()
            background_rect = background.get_rect()
        else:
            background = pygame.image.load(path.join(img_dir, 'charselect.jpg')).convert()
            background_rect = background.get_rect()
            
        
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
    background = pygame.image.load(path.join(img_dir, 'charselect.jpg')).convert()
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
               
                #Direita Inferior
                if 676+285 > pos[0] > 676 and 469+281 > pos[1] > 469:
                    personagem2 = Miranha
                    running = False
                #Esquerda Superior
                if 367+285 > pos[0] > 367 and 161+281 > pos[1] > 161:
                    personagem2 = Luigi    
                    running = False
                #Canto Superior Esquerdo
                if 54+289 > pos[0] > 54 and 161+286 > pos[1] > 161:
                    personagem2 = Mario
                    running = False
                if 1165+168 > pos[0] > 1165 and 107 > pos[1] > 0:
                    personagem2 = Naruto
                    running = False
        
        pos = pygame.mouse.get_pos()
        #Direita Inferior
        if 676+285 > pos[0] > 676 and 469+281 > pos[1] > 469:
            #Miranha
            background = pygame.image.load(path.join(img_dir, 'charselect_miranha.png')).convert()
            background_rect = background.get_rect()
        #Esquerda Superior
        elif 367+285 > pos[0] > 367 and 161+281 > pos[1] > 161:
            #Luigi
            background = pygame.image.load(path.join(img_dir, 'charselect_luigi.png')).convert()
            background_rect = background.get_rect()
        #Canto Superior Esquerdo
        elif 54+289 > pos[0] > 54 and 161+286 > pos[1] > 161:
            #Mario
            background = pygame.image.load(path.join(img_dir, 'charselect_mario.png')).convert()
            background_rect = background.get_rect()
        elif 1165+168 > pos[0] > 1165 and 107 > pos[1] > 0:
            background = pygame.image.load(path.join(img_dir, 'charselect_ee.png')).convert()
            background_rect = background.get_rect()
                    
        else:
            background = pygame.image.load(path.join(img_dir, 'charselect.jpg')).convert()
            background_rect = background.get_rect()
            
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

