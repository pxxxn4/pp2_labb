import pygame

pygame.init()

W, H = 600, 400
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Balls")

BALL_COLOR = (227, 0, 252)
x, y = W // 2, H // 2
R = 25
STEP = 20

keys = {
    pygame.K_LEFT: (-STEP, 0),
    pygame.K_RIGHT: (STEP, 0),
    pygame.K_UP: (0, -STEP),
    pygame.K_DOWN: (0, STEP),
}

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key in keys:
            dx, dy = keys[event.key]
            x = max(R, min(W - R, x + dx))
            y = max(R, min(H - R, y + dy))

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, BALL_COLOR, (x, y), R)
    pygame.display.flip()

pygame.quit()
