import pygame
from os import path

from config import img_dir, snd_dir, fnt_dir, WIDTH, HEIGHT, BLACK, FPS, QUIT, WHITE, FIM_1, FIM_2, DONE, RED


class Player1(pygame.sprite.Sprite):
    
    def __init__(self, player_img):
        
        pygame.sprite.Sprite.__init__(self)
        
        self.image = player_img
        
        self.image = pygame.transform.scale(player_img, (80, 48))
        
        self.image.set_colorkey(BLACK)
        
        self.rect = self.image.get_rect()
        
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        
        self.speedx = 0
        
        self.radius = 25
    
    def update(self):
        self.rect.x += self.speedx
        
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

class Player2(pygame.sprite.Sprite):
    
    def __init__(self, player_img):
        
        pygame.sprite.Sprite.__init__(self)
        
        self.image = player_img
        
        self.image = pygame.transform.scale(player_img, (80, 48))
        self.image = pygame.transform.rotate(self.image,180)
        
        self.image.set_colorkey(BLACK)
        
        self.rect = self.image.get_rect()

        self.rect.centerx = WIDTH / 2
        self.rect.top = 0
        
        self.speedx = 0

        self.radius = 25

    def update(self):
        self.rect.x += self.speedx
        
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
                                
class Bullet1(pygame.sprite.Sprite):
    
    def __init__(self, x, y, bullet_img):
        
        pygame.sprite.Sprite.__init__(self)
        
        self.image = bullet_img
        
        self.image.set_colorkey(BLACK)
        
        self.rect = self.image.get_rect()
        
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        
        if self.rect.bottom < 0:
            self.kill()


class Bullet2(pygame.sprite.Sprite):
    
    def __init__(self, x, y, bullet_img):
        
        pygame.sprite.Sprite.__init__(self)
        
        self.image = bullet_img
        
        self.image.set_colorkey(BLACK)
        
        self.rect = self.image.get_rect()
        
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = 10

    
    def update(self):
        self.rect.y += self.speedy
        
        if self.rect.bottom < 0:
            self.kill()

class Explosion(pygame.sprite.Sprite):

    def __init__(self, center, explosion_anim):
        
        pygame.sprite.Sprite.__init__(self)

        self.explosion_anim = explosion_anim

        self.frame = 0
        self.image = self.explosion_anim[self.frame]
        self.rect = self.image.get_rect()
        self.rect.center = center

        self.last_update = pygame.time.get_ticks()

        self.frame_ticks = 50

    def update(self):

        now = pygame.time.get_ticks()

        elapsed_ticks = now - self.last_update

        if elapsed_ticks > self.frame_ticks:

            self.last_update = now

            self.frame += 1

            if self.frame == len(self.explosion_anim):
                self.kill()
            else:
                
                center = self.rect.center
                self.image = self.explosion_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

def load_assets(img_dir, snd_dir, fnt_dir):
    assets = {}
    for e in range(4):
       assets["player{0}_img".format(e)] = pygame.image.load(path.join(img_dir, "nave_{0}.png".format(e))).convert()
       assets["bullet{0}_img".format(e)] = pygame.image.load(path.join(img_dir, "laser{0}.png".format(e))).convert()
    assets["background"] = pygame.image.load(path.join(img_dir, 'fundo_1.jpg')).convert()
    assets["boom_sound"] = pygame.mixer.Sound(path.join(snd_dir, 'expl3.wav'))
    assets["destroy_sound"] = pygame.mixer.Sound(path.join(snd_dir, 'expl6.wav'))
    assets["pew_sound"] = pygame.mixer.Sound(path.join(snd_dir, 'pew.wav'))
    explosion_anim = []
    for i in range(7):
        filename = 'regularExplosion0{}.png'.format(i)
        img = pygame.image.load(path.join(img_dir, filename)).convert()
        img = pygame.transform.scale(img, (32, 32))        
        img.set_colorkey(BLACK)
        explosion_anim.append(img)
    assets["explosion_anim"] = explosion_anim
    assets["score_font"] = pygame.font.Font(path.join(fnt_dir, "PressStart2P.ttf"), 28)
    return assets

def game_screen(screen,p1,p2):
    
    assets = load_assets(img_dir, snd_dir, fnt_dir)

    clock = pygame.time.Clock()
    
    background = assets["background"]
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    background_rect = background.get_rect()
    

    pygame.mixer.music.load(path.join(snd_dir, 'tgfcoder-FrozenJam-SeamlessLoop.ogg'))
    pygame.mixer.music.set_volume(0.4)
    boom_sound = assets["boom_sound"]
    destroy_sound = assets["destroy_sound"]
    pew_sound = assets["pew_sound"]

    player1 = Player1(assets["player{0}_img".format(p1)])
    player2 = Player2(assets["player{0}_img".format(p2)])
    
    score_font = assets["score_font"]
    
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player1)
    all_sprites.add(player2)
    bullets1 = pygame.sprite.Group()
    bullets2 = pygame.sprite.Group()
    pygame.mixer.music.play(loops=-1)
    
    lives1 = 3
    lives2 = 3

    PLAYING = 0
    EXPLODING1 = 1
    EXPLODING2 = 2
    

    state = PLAYING
    while state != DONE and state != FIM_1 and state!= FIM_2:
        
        clock.tick(FPS)
        
        if state == PLAYING:
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    state = DONE
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        player1.speedx = -8
                    if event.key == pygame.K_RIGHT:
                        player1.speedx = 8
                    if event.key == pygame.K_a:
                        player2.speedx = -8
                    if event.key == pygame.K_d:
                        player2.speedx = 8
                    if event.key == pygame.K_SPACE:
                        bullet = Bullet1(player1.rect.centerx, player1.rect.top, assets["bullet{0}_img".format(p1)])
                        all_sprites.add(bullet)
                        bullets1.add(bullet)
                        pew_sound.play()
                    if event.key == pygame.K_t:
                        bullet = Bullet2(player2.rect.centerx, player2.rect.top, assets["bullet{0}_img".format(p2)])
                        all_sprites.add(bullet)
                        bullets2.add(bullet)
                        pew_sound.play()
                    if event.key == pygame.K_q:
                        state = DONE
                    
                        
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        player1.speedx = 0
                    if event.key == pygame.K_RIGHT:
                        player1.speedx = 0
                    if event.key == pygame.K_a:
                        player2.speedx = 0
                    if event.key == pygame.K_d:
                        player2.speedx = 0
                    
        all_sprites.update()
        
        if state == PLAYING:
            
            hits = pygame.sprite.groupcollide(bullets1, bullets2, True, True, pygame.sprite.collide_mask)
                
            hits = pygame.sprite.spritecollide(player1, bullets2, False, pygame.sprite.collide_mask)
            if hits:
                boom_sound.play()
                player1.kill()
                lives1 -= 1
                explosao = Explosion(player1.rect.center, assets["explosion_anim"])
                all_sprites.add(explosao)
                state = EXPLODING1
                explosion_tick = pygame.time.get_ticks()
                explosion_duration = explosao.frame_ticks * len(explosao.explosion_anim) + 400
            
            hits = pygame.sprite.spritecollide(player2, bullets1, False, pygame.sprite.collide_mask)
            if hits:
                boom_sound.play()
                player2.kill()
                lives2 -= 1
                explosao = Explosion(player2.rect.center, assets["explosion_anim"])
                all_sprites.add(explosao)
                state = EXPLODING2
                explosion_tick = pygame.time.get_ticks()
                explosion_duration = explosao.frame_ticks * len(explosao.explosion_anim) + 400
                
        elif state == EXPLODING1:
            now = pygame.time.get_ticks()
            if now - explosion_tick > explosion_duration:
                if lives1 == 0:
                    return FIM_1
                else:
                    state = PLAYING
                    player1 = Player1(assets["player{0}_img".format(p1)])
                    all_sprites.add(player1)
                    
        elif state == EXPLODING2:
           now = pygame.time.get_ticks()
           if now - explosion_tick > explosion_duration:
               if lives2 == 0:
                   return  FIM_2
               else:
                   state = PLAYING
                   player2 = Player2(assets["player{0}_img".format(p2)])
                   all_sprites.add(player2)
                    
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        #all_sprites.draw(screen)
        
        text_surface = score_font.render(chr(9829) * lives1, True, RED)
        text_rect = text_surface.get_rect()
        text_rect.bottomleft = (10, HEIGHT - 10)
        screen.blit(text_surface, text_rect)
        
        text_surface = score_font.render(chr(9829) * lives2, True, RED)
        text_rect = text_surface.get_rect()
        text_rect.topright = (WIDTH-10, 10)
        screen.blit(text_surface, text_rect)
        
        all_sprites.draw(screen)
        
        pygame.display.flip()

    return QUIT