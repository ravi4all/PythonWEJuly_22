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
move_x = 0
move_y = 0

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

    pygame.draw.rect(SCREEN, RED, [x,y,50,50])
    x += move_x
    y += move_y
    
    # if x > WIDTH - 50:
    #     move_x = -SPEED
    # elif x < 0:
    #     move_x = SPEED
    
    # if y > HEIGHT - 50:
    #     move_y = -SPEED
    # elif y < 0:
    #     move_y = SPEED

    if x > WIDTH:
        x = -50
    elif x < -50:
        x = WIDTH
    
    if y > HEIGHT:
        y = -50
    elif y < -50:
        y = HEIGHT

    pygame.display.flip()
