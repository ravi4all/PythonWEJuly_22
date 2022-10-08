import pygame
import random
pygame.init()

# Screen
SIZE = WIDTH, HEIGHT = 1000, 500
SCREEN = pygame.display.set_mode(SIZE)

WHITE = 255,255,255
BLACK = 0,0,0
RED = 255,0,0
GREEN = 0,255,0
BLUE = 0,0,255

def score(counter):
    font = pygame.font.SysFont(None, 30)
    text = font.render("Score : {}".format(counter), True, BLUE)
    SCREEN.blit(text, (100,10))

def game():
    counter = 0

    SPEED = 2
    x,y = 0,0
    move_x = 0
    move_y = 0

    frog_img = pygame.image.load("frog.png")
    frog_w = frog_img.get_width()
    frog_h = frog_img.get_height()
    frog_x = random.randint(0,WIDTH - frog_w)
    frog_y = random.randint(0,HEIGHT - frog_h)

    clock = pygame.time.Clock()
    FPS = 100

    while True:

        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    move_x = SPEED
                    move_y = 0
                elif event.key == pygame.K_LEFT:
                    move_x = -SPEED
                    move_y = 0
                elif event.key == pygame.K_DOWN:
                    move_y = SPEED
                    move_x = 0
                elif event.key == pygame.K_UP:
                    move_y = -SPEED
                    move_x = 0
            # else:
            #     move_x = 0

        SCREEN.fill(WHITE)

        SCREEN.blit(frog_img, (frog_x, frog_y))
        frog_rect = pygame.Rect(frog_x, frog_y, frog_w, frog_w)

        snake_rect = pygame.draw.rect(SCREEN, RED, [x,y,50,50])
        x += move_x
        y += move_y

        if x > WIDTH:
            x = -50
        elif x < -50:
            x = WIDTH

        if y > HEIGHT:
            y = -50
        elif y < -50:
            y = HEIGHT

        if frog_rect.colliderect(snake_rect):
            frog_x = random.randint(0, WIDTH - frog_w)
            frog_y = random.randint(0, HEIGHT - frog_h)
            counter += 1
            FPS += 20

        score(counter)

        pygame.display.flip()
        clock.tick(FPS)

game()