import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

# Настройки FPS и цветов
FPS = 60
FramePerSec = pygame.time.Clock()

BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Параметры экрана и игры
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
SCORE_COIN = 0
COINS_COLLECTED = 0  # Счетчик собранных монет
N = 5  # Каждые N монет увеличиваем скорость врага

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Фон
background = pygame.image.load("/Users/pxn4/Desktop/lb8/AnimatedStreet.png")

DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

# Класс монеты с разным весом
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.weights = [1, 2, 3]  # Вес монет
        self.weight = random.choice(self.weights)  # Случайный вес
        self.image = pygame.image.load("/Users/pxn4/Desktop/lb8/Coin.png")
        self.image = pygame.transform.scale(self.image, (30 + self.weight*10, 30 + self.weight*10)) 
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(50, SCREEN_WIDTH - 50), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.bottom > 600:
            self.reset()

    def reset(self):
        self.weight = random.choice(self.weights)
        self.image = pygame.transform.scale(pygame.image.load("/Users/pxn4/Desktop/lb8/Coin.png"), (30 + self.weight*10, 30 + self.weight*10))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(50, SCREEN_WIDTH - 50), 0)

    def collect(self):
        global SCORE_COIN, COINS_COLLECTED, SPEED
        SCORE_COIN += self.weight  # Учитываем вес монеты
        COINS_COLLECTED += 1
        if COINS_COLLECTED % N == 0:  # Каждые N монет увеличиваем скорость
            SPEED += 1
        self.reset()

# Класс врага
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("/Users/pxn4/Desktop/lb8/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.bottom > 600:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("/Users/pxn4/Desktop/lb8/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

# Создание объектов
P1 = Player()
E1 = Enemy()
coins = pygame.sprite.Group()

# Генерация 3 монет с разным весом
for _ in range(3):
    coin = Coin()
    coins.add(coin)

enemies = pygame.sprite.Group()
enemies.add(E1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, *coins)

# Таймер для увеличения скорости со временем (дополнительно)
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

pygame.mixer.music.load('/Users/pxn4/Desktop/lb8/background.wav')
pygame.mixer.music.play(-1)

# Основной игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.2
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0, 0))

    # Отображение счета
    scores = font_small.render("Score: " + str(SCORE), True, BLACK)
    score_coins = font_small.render("Coins: " + str(SCORE_COIN), True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))
    DISPLAYSURF.blit(score_coins, (280, 10))

    # Перемещение и отрисовка объектов
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)

# Сбор монет
    for coin in coins:
        if pygame.sprite.collide_rect(P1, coin):
            coin_sound = pygame.mixer.Sound('/Users/pxn4/Desktop/lb8/coin_music.wav')
            coin_sound.set_volume(0.2)  # от 0.0 (тихо) до 1.0 (максимум)
            coin_sound.play()
            coin.collect()


    # Столкновение с врагом
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('/Users/pxn4/Desktop/lb8/crash.wav').play()
        time.sleep(1)
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    FramePerSec.tick(FPS)
