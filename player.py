import pygame
import os
import numpy as np

pygame.init()

# Настройки экрана
W, H = 600, 500
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Music Visualizer")

# Загрузка музыки
music_dir = "/Users/pxn4/Downloads/music"
music_files = sorted([f for f in os.listdir(music_dir) if f.endswith(".wav")])
if not music_files:
    print("Нет WAV-файлов!")
    pygame.quit()
    exit()

track = 0
pygame.mixer.music.load(os.path.join(music_dir, music_files[track]))
pygame.mixer.music.play()

paused = False
font = pygame.font.Font(None, 28)
num_bars = 50

# Функции управления музыкой
def toggle_pause():
    global paused
    paused = not paused
    pygame.mixer.music.pause() if paused else pygame.mixer.music.unpause()

def next_track():
    global track
    track = (track + 1) % len(music_files)
    pygame.mixer.music.load(os.path.join(music_dir, music_files[track]))
    pygame.mixer.music.play()

def prev_track():
    global track
    track = (track - 1) % len(music_files)
    pygame.mixer.music.load(os.path.join(music_dir, music_files[track]))
    pygame.mixer.music.play()

# Словарь управления клавишами
key_actions = {
    pygame.K_SPACE: toggle_pause,
    pygame.K_RIGHT: next_track,
    pygame.K_LEFT: prev_track
}

# Основной цикл
running = True
while running:
    screen.fill((20, 20, 20))  # Очистка экрана

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key in key_actions:
            key_actions[event.key]()  # Вызываем соответствующую функцию

    # Визуализация
    bars = np.random.randint(10, 100, num_bars)
    for i, h in enumerate(bars):
        pygame.draw.rect(screen, (0, 255, 0), (i * (W // num_bars), H // 2 - h // 2, W // num_bars - 2, h))

    # Отображение текста
    screen.blit(font.render(f"Now Playing: {music_files[track]}", True, (255, 255, 255)), (20, 20))
    screen.blit(font.render("Space: Play/Pause | ← Prev | → Next", True, (200, 200, 200)), (20, 450))

    pygame.display.flip()
    pygame.time.delay(100)

pygame.quit()
