import pygame
from os import path

from config import img_dir, BLACK, FPS, GAME, QUIT, WIDTH, HEIGHT


class Botao(pygame.sprite.Sprite):
    
    def __init__(self,x,e):
        
        pygame.sprite.Sprite.__init__(self)
        
        nomes = ['botao.png','botao1.png','botao2.png','botao3.png']
        
        player_img = pygame.image.load(path.join(img_dir, nomes[e])).convert()
        self.image = player_img
        
        self.image = pygame.transform.scale(player_img, (110, 90))
        
        self.image.set_colorkey(BLACK)
        
        self.rect = self.image.get_rect()
        
        self.rect.x = x
        self.rect.y = 68
        self.e = e
        
    def check_click(self, mouse):
        if self.rect.collidepoint(mouse):
            return True
        


def select_screen(screen):
    clock = pygame.time.Clock()
    
    all_sprites = pygame.sprite.Group()
    

    background = pygame.image.load(path.join(img_dir, 'select.png')).convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    background_rect = background.get_rect()
    X_ = 3
    for e in range(4):
        
        botao = Botao(X_,e)
        all_sprites.add(botao)
        X_+=120

    running = True
    click = 0
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                running = False
            if event.type == pygame.KEYUP:
                state = GAME
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    state = QUIT
                    running  = False
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                print(pos)
            if event.type == pygame.MOUSEBUTTONDOWN:
                for s in all_sprites:
                    if s.check_click(event.pos):
                        if click == 0:
                            p1 = s.e
                            click += 1
                        elif click == 1:
                            p2 = s.e
                            state = GAME
                            running = False
                    
                     
        
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)
        pygame.display.flip()
        

    return state,p1,p2

