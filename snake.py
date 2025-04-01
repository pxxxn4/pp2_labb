import pygame, sys, random

pygame.init()

WHITE, GRAY, RED, YELLOW, GREEN = (255, 255, 255), (169, 169, 169), (255, 0, 0), (255, 255, 0), (0, 255, 0)

WIDTH, HEIGHT, CELL = 600, 600, 30
FPS = 5
LEVEL, SCORE = 0, 0

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Verdana", 20)

class Point:
    def __init__(self, x, y): self.x, self.y = x, y
    def __eq__(self, other): return self.x == other.x and self.y == other.y

class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx, self.dy = 1, 0

    def move(self):
        new_head = Point(self.body[0].x + self.dx, self.body[0].y + self.dy)
        if new_head in self.body or not (0 <= new_head.x < WIDTH // CELL and 0 <= new_head.y < HEIGHT // CELL):
            pygame.quit()
            sys.exit()
        self.body.insert(0, new_head)
        if new_head == food.pos:
            global SCORE; SCORE += 1
            food.spawn(self.body)
        else:
            self.body.pop()

    def draw(self):
        pygame.draw.rect(screen, RED, (self.body[0].x * CELL, self.body[0].y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, YELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

class Food:
    def __init__(self): self.pos = Point(0, 0); self.spawn([])
    def spawn(self, snake_body):
        while True:
            self.pos = Point(random.randint(0, WIDTH // CELL - 1), random.randint(0, HEIGHT // CELL - 1))
            if self.pos not in snake_body: break
    def draw(self):
        pygame.draw.rect(screen, GREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

def draw_grid():
    for i in range(WIDTH // CELL):
        for j in range(HEIGHT // CELL):
            pygame.draw.rect(screen, GRAY if (i + j) % 2 else WHITE, (i * CELL, j * CELL, CELL, CELL))

snake, food = Snake(), Food()

running = True
while running:
    screen.fill(WHITE)
    draw_grid()

    LEVEL = min(SCORE // 10, 3)
    FPS = 5 + LEVEL * 3

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snake.dx == 0:
                snake.dx, snake.dy = 1, 0
            elif event.key == pygame.K_LEFT and snake.dx == 0:
                snake.dx, snake.dy = -1, 0
            elif event.key == pygame.K_DOWN and snake.dy == 0:
                snake.dx, snake.dy = 0, 1
            elif event.key == pygame.K_UP and snake.dy == 0:
                snake.dx, snake.dy = 0, -1

    snake.move()
    snake.draw()
    food.draw()

    screen.blit(font.render(f"Score: {SCORE}", True, RED), (10, 10))
    screen.blit(font.render(f"Level: {LEVEL}", True, RED), (500, 10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()