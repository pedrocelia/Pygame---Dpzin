
import pygame
from os import path
from config_fut import *
import random

from assets_fut import *


class player1(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self,personagem1):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        player_img = assets_fut["{0}_left_img".format(personagem1)]
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.image = player_img
        self.personagem1 = personagem1
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(player_img, (50, 38))
        
        # Deixando transparente.
        self.image.set_colorkey(DARK_BLUE)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Centraliza embaixo da tela.
        self.rect.centerx = 3*WIDTH1 /4
        self.rect.bottom = HEIGHT1/2
        
        # Velocidade da nave
        self.speedx = 0
        
        self.speedy = 0
        
        # Melhora a colisão estabelecendo um raio de um circulo
        self.radius = 25
    #Pontos
        self.pontos = 0
        
        #Variavel de estado 
        self.moving = False
        
        #posição x
        self.x_player1 = self.rect.centerx
        
        #posição y
        self.y_player1 = self.rect.centery  
        
    # Metodo que atualiza a posição da navinha
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.up:
            player_img = assets_fut["{0}_up_img".format(self.personagem1)]
            self.image = player_img
            self.image.set_colorkey(DARK_BLUE)
            self.image = pygame.transform.scale(player_img, (50, 38))
        elif self.down:
            player_img = assets_fut["{0}_down_img".format(self.personagem1)]
            self.image = player_img
            self.image.set_colorkey(DARK_BLUE)
            self.image = pygame.transform.scale(player_img, (50, 38))
        elif self.right:
            player_img = assets_fut["{0}_right_img".format(self.personagem1)]
            self.image = player_img
            self.image.set_colorkey(DARK_BLUE)
            self.image = pygame.transform.scale(player_img, (50, 38))
        elif self.left:
            player_img = assets_fut["{0}_left_img".format(self.personagem1)]
            self.image = player_img
            self.image.set_colorkey(DARK_BLUE)
            self.image = pygame.transform.scale(player_img, (50, 38))
        # Mantem dentro da tela
        if self.rect.left < WIDTH1/2:
            self.rect.left = WIDTH1/2
        if self.rect.right > WIDTH1:
            self.rect.right = WIDTH1
        if self.rect.bottom > HEIGHT1:
            self.rect.bottom = HEIGHT1
        if self.rect.top < 0:
            self.rect.top = 0
class player2(pygame.sprite.Sprite):
        # Construtor da classe.
    def __init__(self,personagem2):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        player_img = assets_fut["{0}_right_img".format(personagem2)]
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.image = player_img
        self.personagem2 = personagem2
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(player_img, (50, 38))
        
        # Deixando transparente.
        self.image.set_colorkey(DARK_BLUE)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Centraliza embaixo da tela.
        self.rect.centerx = WIDTH1 /4
        self.rect.bottom = HEIGHT1/2
        
        # Velocidade da nave
        self.speedx = 0
        
        self.speedy = 0
        
        # Melhora a colisão estabelecendo um raio de um circulo
        self.radius = 25
    #Pontos
        self.pontos = 0
        
        #Variavel de estado 
        self.moving = False
        
        #posição x
        self.x_player2 = self.rect.centerx
        
        #posição y
        self.y_player2 = self.rect.centery  
        
    # Metodo que atualiza a posição da navinha
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.up:
            player_img = assets_fut["{0}_up_img".format(self.personagem2)]
            self.image = player_img
            self.image.set_colorkey(DARK_BLUE)
            self.image = pygame.transform.scale(player_img, (50, 38))
        elif self.down:
            player_img = assets_fut["{0}_down_img".format(self.personagem2)]
            self.image = player_img
            self.image.set_colorkey(DARK_BLUE)
            self.image = pygame.transform.scale(player_img, (50, 38))
        elif self.right:
            player_img = assets_fut["{0}_right_img".format(self.personagem2)]
            self.image = player_img
            self.image.set_colorkey(DARK_BLUE)
            self.image = pygame.transform.scale(player_img, (50, 38))
        elif self.left:
            player_img = assets_fut["{0}_left_img".format(self.personagem2)]
            self.image = player_img
            self.image.set_colorkey(DARK_BLUE)
            self.image = pygame.transform.scale(player_img, (50, 38))
        if self.rect.right > WIDTH1/2:
            self.rect.right = WIDTH1/2
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > HEIGHT1:
            self.rect.bottom = HEIGHT1
        if self.rect.top < 0:
            self.rect.top = 0    
    
class bola(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self, player_img):
        self.gol1 = False
        self.gol2 = False
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.
        self.image = player_img
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(player_img, (25, 25))
        
        # Deixando transparente.
        self.image.set_colorkey(DARK_BLUE)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # centraliza embaixo da tela
        self.rect.centerx = WIDTH1 /2
        self.rect.bottom = HEIGHT1/2
        
        #Velocidade
        self.speedx = 0
        self.speedy = 0 
        self.radius = 10
        
        #posição x
        self.x_ball = self.rect.centerx
        
        #posição y
        self.y_ball = self.rect.centery  
        
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Mantem dentro da tela
        
        if self.rect.right >= WIDTH1:
            if 248 + 255 > self.rect.top > 248 and 248 + 255> self.rect.bottom > 248:
                self.gol2 = True
                self.speedx= 0
                self.speedy= 0
                self.rect.centerx = WIDTH1/2 + 100
                self.rect.bottom = HEIGHT1/2
                
            else:
                self.speedx=-self.speedx

        
        
        if self.rect.left <= 0:
            if 248 + 255 > self.rect.top > 248 and 248 + 255> self.rect.bottom > 248:
                self.gol1 = True
                self.speedx= 0
                self.speedy= 0
                self.rect.centerx = WIDTH1/2 - 100
                self.rect.bottom = HEIGHT1/2
            else:
                self.speedx=-self.speedx

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > HEIGHT1:

            self.speedy=-self.speedy
        if self.rect.top < 0:

            self.speedy=-self.speedy
            