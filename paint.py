import pygame
import math
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Paint")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)

colors = [RED, GREEN, BLUE, BLACK]
color = BLUE

draw_surf = pygame.Surface((WIDTH, HEIGHT))
draw_surf.fill(WHITE)

clock = pygame.time.Clock()

radius = 5
thickness = 2
mode = 'brush'  # other modes: eraser, rect, circle, rtriangle, eqtriangle, rhombus
start_pos = None
draw_on = False

def draw_line(surf, start, end, width, color):
    x1, y1 = start
    x2, y2 = end
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)

    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2

    if dx > dy:
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        for x in range(x1, x2):
            y = int((-C - A * x) / B)
            pygame.draw.circle(surf, color, (x, y), width)
    else:
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        for y in range(y1, y2):
            x = int((-C - B * y) / A)
            pygame.draw.circle(surf, color, (x, y), width)

def draw_right_triangle(surface, start, end, color):
    pygame.draw.polygon(surface, color, [start, end, (start[0], end[1])], thickness)

def draw_equilateral_triangle(surface, start, end, color):
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    pygame.draw.polygon(surface, color, [start, end, (start[0] + dx // 2, start[1] - abs(dy))], thickness)

def draw_rhombus(surface, start, end, color):
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    pygame.draw.polygon(surface, color, [
        (start[0] + dx // 2, start[1]),
        (end[0], start[1] + dy // 2),
        (start[0] + dx // 2, end[1]),
        (start[0], start[1] + dy // 2)
    ], thickness)

running = True
last_pos = (0, 0)

while running:
    screen.fill(WHITE)
    screen.blit(draw_surf, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # цвет через клавиши R/G/B
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                color = RED
            elif event.key == pygame.K_g:
                color = GREEN
            elif event.key == pygame.K_b:
                color = BLUE
            elif event.key == pygame.K_k:
                color = BLACK
            elif event.key == pygame.K_0:
                mode = 'none'
            elif event.key == pygame.K_1:
                mode = 'brush'
            elif event.key == pygame.K_2:
                mode = 'eraser'
            elif event.key == pygame.K_3:
                mode = 'rect'
            elif event.key == pygame.K_4:
                mode = 'circle'
            elif event.key == pygame.K_5:
                mode = 'rtriangle'
            elif event.key == pygame.K_6:
                mode = 'eqtriangle'
            elif event.key == pygame.K_7:
                mode = 'rhombus'
            elif event.key == pygame.K_s:
                pygame.image.save(draw_surf, "drawing.png")

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                draw_on = True
                start_pos = event.pos
                if mode == 'brush' or mode == 'eraser':
                    draw_line(draw_surf, event.pos, event.pos, radius, color if mode == 'brush' else WHITE)

            # Скролл мышки: изменение размера
            if event.button == 4:  # scroll up
                if mode in ['brush', 'eraser'] and radius < 50:
                    radius += 1
                elif mode in ['rect', 'circle', 'rtriangle', 'eqtriangle', 'rhombus'] and thickness < 10:
                    thickness += 1
            if event.button == 5:  # scroll down
                if mode in ['brush', 'eraser'] and radius > 1:
                    radius -= 1
                elif mode in ['rect', 'circle', 'rtriangle', 'eqtriangle', 'rhombus'] and thickness > 1:
                    thickness -= 1

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and start_pos:
                end_pos = event.pos
                if mode == 'rect':
                    pygame.draw.rect(draw_surf, color, pygame.Rect(
                        min(start_pos[0], end_pos[0]),
                        min(start_pos[1], end_pos[1]),
                        abs(end_pos[0] - start_pos[0]),
                        abs(end_pos[1] - start_pos[1])
                    ), thickness)
                elif mode == 'circle':
                    rad = int(math.dist(start_pos, end_pos))
                    pygame.draw.circle(draw_surf, color, start_pos, rad, thickness)
                elif mode == 'rtriangle':
                    draw_right_triangle(draw_surf, start_pos, end_pos, color)
                elif mode == 'eqtriangle':
                    draw_equilateral_triangle(draw_surf, start_pos, end_pos, color)
                elif mode == 'rhombus':
                    draw_rhombus(draw_surf, start_pos, end_pos, color)
            draw_on = False
            start_pos = None

        if event.type == pygame.MOUSEMOTION:
            if draw_on and (mode == 'brush' or mode == 'eraser'):
                draw_line(draw_surf, last_pos, event.pos, radius, color if mode == 'brush' else WHITE)

            last_pos = event.pos

    pygame.display.flip()
    clock.tick(120)

pygame.quit()
