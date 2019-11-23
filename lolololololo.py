# Importando as bibliotecas necessárias.
import pygame

from config import WIDTH, HEIGHT, INIT, GAME, QUIT, FIM_1, SELECT, FIM_2, SELECAO_MINIGAME
from innit_screen import init_screen
from game_screen import game_screen
from tela_vitoria import fim1_screen
from tela_vitoria2 import fim2_screen
from selacao import select_screen
from selecao_minigame import selecao_minigame
from Fut import *
from classes_fut import *
from config_fut import *
from classes_fut import *
from assets_fut import *
from character_selection import *


# Inicialização do Pygame.
pygame.init()
pygame.mixer.init()

# Tamanho da tela.
screen = pygame.display.set_mode((WIDTH, HEIGHT),pygame.FULLSCREEN)

# Nome do jogo
pygame.display.set_caption("Battle Galaxy")

# Comando para evitar travamentos.
try:
    state = SELECAO_MINIGAME
    p1 = -1
    p2 = -1
    while state != QUIT:
        if state == INIT:
            state = init_screen(screen)
        elif state == GAME:
            state = game_screen(screen,p1,p2)
        elif state == FIM_1:
            state = fim2_screen(screen)
        elif state == FIM_2:
            state = fim1_screen(screen)
        elif state == SELECT:
            state,p1,p2 = select_screen(screen)
        elif state == SELECAO_MINIGAME:
            state = selecao_minigame(screen)
        elif state == FUT:
            state = p1_select(screen)
            state = char_screen_p1(screen)
            personagem1 = state
            state = p2_select(screen)
            state = char_screen_p2(screen)
            personagem2 = state
            state = fut(screen,personagem1,personagem2, snd_dir)
        else:
            state = QUIT
finally:
    pygame.quit()

