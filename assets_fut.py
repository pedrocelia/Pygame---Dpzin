import pygame

from os import path
from config_fut import *

#pygame.font.init()
def load_assets(img_dir, snd_dir,fnt_dir):
    assets = {}
    assets["score_font"] = pygame.font.Font(path.join(fnt_dir, "PressStart2P.ttf"), 28)
    assets["BOLA"] = pygame.image.load(path.join(img_dir,"bola.png")).convert()
    #Mario Assets
    assets["Mario_p2_TIRO_img"] = pygame.image.load(path.join(img_dir,"mario_front_tiro.png")).convert()
    assets["Mario_p1_TIRO_img"] = pygame.image.load(path.join(img_dir,"mario_back_tiro.png")).convert()
    assets["Mario_down_img"] = pygame.image.load(path.join(img_dir,"mario_down.png")).convert()
    assets["Mario_up_img"] = pygame.image.load(path.join(img_dir,"mario_up.png")).convert()
    assets["Mario_right_img"] = pygame.image.load(path.join(img_dir,"mario_right.png")).convert()
    assets["Mario_left_img"] = pygame.image.load(path.join(img_dir,"mario_left.png")).convert()
    assets["Mario_p1_Shot_img"] = pygame.image.load(path.join(img_dir,"rfire_up.png")).convert()
    assets["Mario_p2_Shot_img"] = pygame.image.load(path.join(img_dir,"rfire_down.png")).convert()
    assets["Mario_left_Shot_img"] = pygame.image.load(path.join(img_dir,"rfire_left.png")).convert()
    assets["Mario_right_Shot_img"] = pygame.image.load(path.join(img_dir,"rfire_right.png")).convert()
    #Luigi Assets
    assets["Luigi_p2_TIRO_img"] = pygame.image.load(path.join(img_dir,"luigi_front_tiro.png")).convert()
    assets["Luigi_p1_TIRO_img"] = pygame.image.load(path.join(img_dir,"luigi_back_tiro.png")).convert()
    assets["Luigi_down_img"] = pygame.image.load(path.join(img_dir,"luigi_down.png")).convert()
    assets["Luigi_up_img"] = pygame.image.load(path.join(img_dir,"luigi_up.png")).convert()
    assets["Luigi_right_img"] = pygame.image.load(path.join(img_dir,"luigi_right.png")).convert()
    assets["Luigi_left_img"] = pygame.image.load(path.join(img_dir,"luigi_left.png")).convert()
    assets["Luigi_p1_Shot_img"] = pygame.image.load(path.join(img_dir,"gfire_up.png")).convert()
    assets["Luigi_p2_Shot_img"] = pygame.image.load(path.join(img_dir,"gfire_down.png")).convert()
    assets["Luigi_left_Shot_img"] = pygame.image.load(path.join(img_dir,"gfire_left.png")).convert()
    assets["Luigi_right_Shot_img"] = pygame.image.load(path.join(img_dir,"gfire_right.png")).convert()
   
    #Miranha Assets
    assets["Miranha_p2_TIRO_img"] = pygame.image.load(path.join(img_dir,"miranha_front.png")).convert()
    assets["Miranha_p1_TIRO_img"] = pygame.image.load(path.join(img_dir,"miranha_back.png")).convert()
    assets["Miranha_down_img"] = pygame.image.load(path.join(img_dir,"miranha_down.png")).convert()
    assets["Miranha_up_img"] = pygame.image.load(path.join(img_dir,"miranha_up.png")).convert()
    assets["Miranha_right_img"] = pygame.image.load(path.join(img_dir,"miranha_right.png")).convert()
    assets["Miranha_left_img"] = pygame.image.load(path.join(img_dir,"miranha_left.png")).convert()
    assets["Miranha_p1_Shot_img"] = pygame.image.load(path.join(img_dir,"miranha_shot_up.png")).convert()
    assets["Miranha_p2_Shot_img"] = pygame.image.load(path.join(img_dir,"miranha_shot_down.png")).convert()
    assets["Miranha_left_Shot_img"] = pygame.image.load(path.join(img_dir,"miranha_shot_left.png")).convert()
    assets["Miranha_right_Shot_img"] = pygame.image.load(path.join(img_dir,"miranha_shot_right.png")).convert()
      
    #Naruto Assets
    assets["Naruto_p2_TIRO_img"] = pygame.image.load(path.join(img_dir,"naruto_front.png")).convert()
    assets["Naruto_p1_TIRO_img"] = pygame.image.load(path.join(img_dir,"naruto_back.png")).convert()
    assets["Naruto_down_img"] = pygame.image.load(path.join(img_dir,"naruto_down.png")).convert()
    assets["Naruto_up_img"] = pygame.image.load(path.join(img_dir,"naruto_up.png")).convert()
    assets["Naruto_right_img"] = pygame.image.load(path.join(img_dir,"naruto_right.png")).convert()
    assets["Naruto_left_img"] = pygame.image.load(path.join(img_dir,"naruto_left.png")).convert()
    assets["Naruto_p1_Shot_img"] = pygame.image.load(path.join(img_dir,"rasengan_up.png")).convert()
    assets["Naruto_p2_Shot_img"] = pygame.image.load(path.join(img_dir,"rasengan_down.png")).convert()
    assets["Naruto_left_Shot_img"] = pygame.image.load(path.join(img_dir,"rasengan_left.png")).convert()
    assets["Naruto_right_Shot_img"] = pygame.image.load(path.join(img_dir,"rasengan_right.png")).convert()
    
    return assets_fut
    
assets_fut = load_assets(img_dir, snd_dir,fnt_dir)