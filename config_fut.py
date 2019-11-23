from os import path

# Estabelece a pasta que contem as figuras e sons.
img_dir = path.join(path.dirname(__file__), 'assets\img')
snd_dir = path.join(path.dirname(__file__), 'snd')
fnt_dir = path.join(path.dirname(__file__), 'font')

# Dados gerais do jogo.
WIDTH = 1333 # Largura da tela
HEIGHT = 750 # Altura da tela
FPS = 60 # Frames por segundo

# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 230, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BRIGHT_GREEN = (0,255,0)
BRIGHT_RED = (255, 0, 0)
DARK_BLUE = (33, 39, 124)
ZENO = (183,4,251)
p1_points = 0 
p2_points = 0
# Estados para controle do fluxo da aplicação
pontos = 0
INIT = 10
MAIN_MENU = 11
CHAR_SELECT = 12
#MINIGAME #Será uma variável que irá guardar qual o jogo selecionado
TIRO = 13
MAGUINHO = 14
HOCKEY = 15
PAINT = 16
#Adicionar diferentes Minigames 4-10 
QUIT = 17
P1_WIN = 18
P2_WIN = 19 

Mario = "Mario"
Luigi = "Luigi"
Deku = "Deku"
Sans = "Sans"
Link = "Link"
Skull = "Skull"
Miranha = "Miranha"
Gandalf = "Gandalf"
Naruto = "Naruto"

