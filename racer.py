import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
SCORE_COIN = 0

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("/Users/pxn4/Desktop/lb8/AnimatedStreet.png")

DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("/Users/pxn4/Desktop/lb8/Coin.png")
        self.image = pygame.transform.scale(self.image, (100, 100)) 
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(50, SCREEN_WIDTH - 50), 0)
    def move(self):
        self.rect.move_ip(0, SPEED)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
    def collect(self): #method for collection a coin
        global SCORE_COIN
        SCORE_COIN += 1
        self.rect.top = 0
        self.rect.center = (random.randint(50, SCREEN_WIDTH - 50), 0)
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("/Users/pxn4/Desktop/lb8/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)

      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("/Users/pxn4/Desktop/lb8/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        

        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
                  

P1 = Player()
E1 = Enemy()
C1 = Coin()


enemies = pygame.sprite.Group()
coins = pygame.sprite.Group()
coins.add(C1)
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

pygame.mixer.music.load('/Users/pxn4/Desktop/lb8/background.wav')
pygame.mixer.music.play(-1)


while True:
      
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.5      
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    if pygame.sprite.spritecollideany(C1, enemies): #if collision between coin and enemy to reinitialize coin
        C1.__init__()

    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    score_coins = font_small.render(str(SCORE_COIN), True, BLACK)
    DISPLAYSURF.blit(score_coins, (380,10 ))
    DISPLAYSURF.blit(scores, (10,10))

    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)
        

    if pygame.sprite.spritecollideany(P1, coins): #if collision between player and coin
        pygame.mixer.Sound('/Users/pxn4/Desktop/lb8/coin_music.wav').play()
        for coin in coins:
            C1.collect()
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('/Users/pxn4/Desktop/lb8/crash.wav').play()
          time.sleep(1)
                   
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
          
          pygame.display.update()
          for entity in all_sprites:
                entity.kill()
          time.sleep(2)
          pygame.quit()
          sys.exit()        
    pygame.display.update()
    FramePerSec.tick(FPS)
