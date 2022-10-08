import pygame
pygame.init()

# Screen
SIZE = WIDTH, HEIGHT = 1000, 500
SCREEN = pygame.display.set_mode(SIZE)

WHITE = 255,255,255
BLACK = 0,0,0
RED = 255,0,0
GREEN = 0,255,0
BLUE = 0,0,255

SPEED = 0.5
x,y = 0,0
move_x = SPEED
move_y = SPEED

while True:

    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            quit()

    SCREEN.fill(WHITE)

    pygame.draw.rect(SCREEN, RED, [x,y,50,50])
    x += move_x
    y += move_y
    
    if x > WIDTH - 50:
        move_x = -SPEED
    elif x < 0:
        move_x = SPEED
    
    if y > HEIGHT - 50:
        move_y = -SPEED
    elif y < 0:
        move_y = SPEED

    pygame.display.flip()
