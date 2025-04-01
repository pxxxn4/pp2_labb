import pygame
import math

pygame.init()

WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

radius = 5
color = (0, 0, 255)
shape = None
start_pos = None
end_pos = None
rectangles = []
circles = []
points = []

running = True
while running:
    screen.fill((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                color = (255, 0, 0)
            elif event.key == pygame.K_g:
                color = (0, 255, 0)
            elif event.key == pygame.K_b:
                color = (0, 0, 255)
            elif event.key == pygame.K_1:
                shape = 'rectangle'
            elif event.key == pygame.K_2:
                shape = 'circle'
            elif event.key == pygame.K_0:
                shape = None
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            start_pos = event.pos
            end_pos = event.pos
            if shape is None:
                points.append(event.pos)
        
        if event.type == pygame.MOUSEMOTION and event.buttons[0]:
            end_pos = event.pos
            if shape is None:
                points.append(event.pos)
        
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if shape == 'rectangle' and start_pos:
                rectangles.append((start_pos, end_pos, color))
            elif shape == 'circle' and start_pos:
                circles.append((start_pos, end_pos, color))
            start_pos = None
            end_pos = None
    
    for i in range(1, len(points)):
        pygame.draw.line(screen, color, points[i - 1], points[i], radius)
    
    for rect in rectangles:
        pygame.draw.rect(screen, rect[2], pygame.Rect(
            min(rect[0][0], rect[1][0]),
            min(rect[0][1], rect[1][1]),
            abs(rect[1][0] - rect[0][0]),
            abs(rect[1][1] - rect[0][1])
        ), 2)
    
    for circ in circles:
        center, edge, color = circ
        radius = int(math.dist(center, edge))
        pygame.draw.circle(screen, color, center, radius, 2)
    
    if start_pos and end_pos:
        if shape == 'rectangle':
            pygame.draw.rect(screen, color, pygame.Rect(
                min(start_pos[0], end_pos[0]),
                min(start_pos[1], end_pos[1]),
                abs(end_pos[0] - start_pos[0]),
                abs(end_pos[1] - start_pos[1])
            ), 2)
        elif shape == 'circle':
            radius = int(math.dist(start_pos, end_pos))
            pygame.draw.circle(screen, color, start_pos, radius, 2)
    
    pygame.display.flip()
    clock.tick(120)

pygame.quit()