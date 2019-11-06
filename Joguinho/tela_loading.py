import pygame
from os import path
import time 

from config import img_dir, BLACK, GAME, WIDTH, HEIGHT

def loading_screen(screen):
    background = pygame.image.load(path.join(img_dir, 'loanding.jpg')).convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    background_rect = background.get_rect()
    
    time.sleep(3)           
    state = GAME
                
    
        
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    pygame.display.flip()

    return state