# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 10:24:37 2019

@author: Tonera
"""

import pygame
from os import path
import time

from config import img_dir, BLACK, FPS, GAME, QUIT, WIDTH, HEIGHT, INIT

JOGO_NAVE = 0
JOGO_HOCKEY = 1

class Botao(pygame.sprite.Sprite):
    
    def __init__(self,y,e):
        
        pygame.sprite.Sprite.__init__(self)
        
        nomes = ['inicio1.png', 'inicio2.jpeg']
        
        img = pygame.image.load(path.join(img_dir, nomes[e])).convert()
        self.image = img
        
        self.image = pygame.transform.scale(img, (300, 210))
        
        self.image.set_colorkey(BLACK)
        
        self.rect = self.image.get_rect()
        
        self.rect.centerx = WIDTH/2
        self.rect.y = y
        self.e = e
        
        
    def check_click(self, mouse):
        if self.rect.collidepoint(mouse):
            return True
        else:
            return False
        
class Tile(pygame.sprite.Sprite):

    # Construtor da classe.
    def __init__(self, x, y, image):

        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        Player_img = pygame.image.load(path.join(img_dir, image)).convert()
        
        self.image = pygame.transform.scale(Player_img, (110, 90))

        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()

        # Posiciona o tile
        self.rect.x = x
        self.rect.y = y       


def selecao_minigame(screen):
    clock = pygame.time.Clock()
    
    all_sprites = pygame.sprite.Group()
    botoes = pygame.sprite.Group()
    

    background = pygame.image.load(path.join(img_dir, 'back.jpg')).convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    background_rect = background.get_rect()
    Y_ = 10
    for e in range(2):
        
        botao = Botao(Y_,e)
        all_sprites.add(botao)
        botoes.add(botao)
        Y_+=300

    running = True
    click = 0
    
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    state = QUIT
                    running  = False
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                print(pos)
            if event.type == pygame.MOUSEBUTTONDOWN:
                for s in botoes:
                    if s.check_click(event.pos):
                        if click == 0:
                            jogo = s.e
                            click = 1
                            if jogo == JOGO_NAVE:
                                state = INIT
                                running = False 
                        
                        
                    
                     
        
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)
        pygame.display.flip()
        if running == False:
            time.sleep(1)
        

    return state