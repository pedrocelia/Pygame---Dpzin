
import pygame

from os import path
from config_fut import *
from classes_fut import *
from assets_fut import *
from character_selection import *
score_font = assets_fut["score_font"]

def Gols_P1(count):
    
    text_surface = score_font.render("Gols P1:{0}".format(count), True,BLACK)
    text_rect = text_surface.get_rect()
    screen.blit(text_surface,(WIDTH1-270,10))
    

    
def Gols_P2(count):
    
    text_surface = score_font.render("Gols P2:{0}".format(count), True, BLACK)
    text_rect = text_surface.get_rect()
    screen.blit(text_surface,(12,10))
screen = pygame.display.set_mode((WIDTH1, HEIGHT1))
clock = pygame.time.Clock()



#Cria um grupo de sprites e adiciona a nave

def fut(screen,personagem1,personagem2, snd_dir):
    P1 = Player1(personagem1)
    P2 = player2(personagem2)

    
    Bola = bola(assets_fut["BOLA"])

    background = pygame.image.load(path.join(img_dir, 'campo.png')).convert()
    background_rect = background.get_rect()
    pygame.mixer.music.load(path.join(snd_dir, 'musica_fundo_hockey.mp3'))
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(1)
    pygame.event.wait()
    running = True
    #pygame.mixer.music.play(loops=-1)
    p1gol = 0
    p2gol = 0
    all_sprites = pygame.sprite.Group()
    all_sprites.add(P1)
    all_sprites.add(P2)

    bola_sprite = pygame.sprite.Group()
    bola_sprite.add(Bola)
    all_sprites.add(bola_sprite)
    while running:
        Gols_P1(p1gol)
        Gols_P2(p2gol)
        pygame.display.update()
            
            # Ajusta a velocidade do jogo.
        clock.tick(FPS)
            
        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
                
                # Verifica se foi fechado
            if event.type == pygame.QUIT:
                running = False
            #verifica se apertou alguma tecla    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    P1.left = True
                    P1.speedx = -8
                if event.key == pygame.K_RIGHT:
                    P1.right = True
                    P1.speedx = 8
                if event.key == pygame.K_UP:
                    P1.up = True
                    P1.speedy = -8
                if event.key == pygame.K_DOWN:
                    P1.down = True
                    P1.speedy = 8
                if event.key == pygame.K_a:
                    P2.left = True
                    P2.speedx = -8
                if event.key == pygame.K_d:
                    P2.right = True
                    P2.speedx = 8
                if event.key == pygame.K_w:
                    P2.up = True
                    P2.speedy = -8
                if event.key == pygame.K_s:
                    P2.down = True
                    P2.speedy = 8
               
               
                    
            if event.type == pygame.KEYUP:  
                if event.key == pygame.K_LEFT:
                    P1.left = False
                    P1.speedx = 0
                if event.key == pygame.K_RIGHT:
                    P1.right = False
                    P1.speedx = 0
                if event.key == pygame.K_UP:
                    P1.up = False
                    P1.speedy = 0
                if event.key == pygame.K_DOWN:
                    P1.down = False
                    P1.speedy = 0
                if event.key == pygame.K_a:
                    P2.speedx = 0
                    P2.left = False
                if event.key == pygame.K_d:
                    P2.speedx = 0
                    P2.right = False
                if event.key == pygame.K_w:
                    P2.speedy = 0
                    P2.up = False
                if event.key == pygame.K_s:
                    P2.speedy = 0
                    P2.down = False
               
                    
        hit1 = pygame.sprite.spritecollide(P1,bola_sprite, False)
        hit2 = pygame.sprite.spritecollide(P2,bola_sprite, False)
        
        
        if hit1:
            
            Bola.speedx = P1.speedx          
            Bola.speedy = P1.speedy
            
        if hit2: 

            Bola.speedx = P2.speedx            
            Bola.speedy = P2.speedy
        
        
        if Bola.gol1:
            Bola.gol1 = False
            p1gol +=1
                
        if Bola.gol2:
            Bola.gol2 = False
            p2gol +=1
                
            
        all_sprites.update()
        bola_sprite.update()
        if p1gol >= 4 and p2gol >= 4:
            if p1gol- p2gol >=2:
                pygame.mixer.pause()
                running = False
                state = P1_WIN
            elif p2gol- p1gol >=2:
                pygame.mixer.pause()
                running = False
                state = P2_WIN
            
        elif p1gol == 5 and p2gol <=4:
            pygame.mixer.pause()
            running = False
            state = P1_WIN
        elif p2gol == 5 and p1gol <=4:
            pygame.mixer.pause()
            running = False
            state = P2_WIN
                        
        
        if running == True:
            # A cada loop, redesenha o fundo e os sprites
            screen.fill(WHITE)
            pygame.init()
            screen.blit(background, background_rect)
            all_sprites.draw(screen)
            bola_sprite.draw(screen)
            
    
    return state