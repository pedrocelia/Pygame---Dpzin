from os import path

# Estabelece a pasta que contem as figuras e sons.
img_dir = path.join(path.dirname(__file__), 'assets\img')
snd_dir = path.join(path.dirname(__file__), 'assets\sound')
fnt_dir = path.join(path.dirname(__file__), 'font')

# Dados gerais do jogo.
WIDTH = 480 # Largura da tela
HEIGHT = 600 # Altura da tela
FPS = 60 # Frames por segundo
# Dados gerais do jogo FUT.
WIDTH1 = 1333 # Largura da tela
HEIGHT1 = 750 # Altura da tela

# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BRIGHT_GREEN = (0,255,0)
BRIGHT_RED = (255, 0, 0)
DARK_BLUE = (33, 39, 124)
ZENO = (183,4,251)
p1_points = 0 
p2_points = 0
pontos = 0
# Estados para controle do fluxo da aplicação
INIT = 0
GAME = 1
QUIT = 2
FIM_1 = 3
DONE = 4
SELECT = 5
FIM_2 = 6
SELECAO_MINIGAME = 7
