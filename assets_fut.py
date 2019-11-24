import pygame

from os import path
from config_fut import *

pygame.font.init()
pygame.init()
screen = pygame.display.set_mode((WIDTH1, HEIGHT1))
def load_assets(img_dir, snd_dir,fnt_dir):
    assets_fut = {}
    assets_fut["score_font"] = pygame.font.Font(path.join(fnt_dir, "PressStart2P.ttf"), 28)
    assets_fut["BOLA"] = pygame.image.load(path.join(img_dir,"bola.png")).convert()
    #Mario Assets
    assets_fut["Mario_down_img"] = pygame.image.load(path.join(img_dir,"mario_down.png")).convert()
    assets_fut["Mario_up_img"] = pygame.image.load(path.join(img_dir,"mario_up.png")).convert()
    assets_fut["Mario_right_img"] = pygame.image.load(path.join(img_dir,"mario_right.png")).convert()
    assets_fut["Mario_left_img"] = pygame.image.load(path.join(img_dir,"mario_left.png")).convert()
    
    #Luigi Assets
    assets_fut["Luigi_down_img"] = pygame.image.load(path.join(img_dir,"luigi_down.png")).convert()
    assets_fut["Luigi_up_img"] = pygame.image.load(path.join(img_dir,"luigi_up.png")).convert()
    assets_fut["Luigi_right_img"] = pygame.image.load(path.join(img_dir,"luigi_right.png")).convert()
    assets_fut["Luigi_left_img"] = pygame.image.load(path.join(img_dir,"luigi_left.png")).convert()
   
    #Miranha Assets
    assets_fut["Miranha_down_img"] = pygame.image.load(path.join(img_dir,"miranha_down.png")).convert()
    assets_fut["Miranha_up_img"] = pygame.image.load(path.join(img_dir,"miranha_up.png")).convert()
    assets_fut["Miranha_right_img"] = pygame.image.load(path.join(img_dir,"miranha_right.png")).convert()
    assets_fut["Miranha_left_img"] = pygame.image.load(path.join(img_dir,"miranha_left.png")).convert()
   
    return assets_fut
    
assets_fut = load_assets(img_dir, snd_dir,fnt_dir)