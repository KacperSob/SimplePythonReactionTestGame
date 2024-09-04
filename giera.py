import pygame
import random

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
LORR = 0
LORR_ = 0
UORRD = 0
UORRD_ = 0
RTIME = 0
CRR = 0
CRRD = 0
CHNGVALUE = 3
KTR = 0 

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("giera")

rect_1 = pygame.Rect(0, 0, 25, 25)

posX = []
posY = []
rnX = 0
rnY = 0
obstacles = []
for _ in range(5):
    rnX = random.randint(0,500)
    rnY = random.randint(0,300)
    obstacle_rect = pygame.Rect(rnX, rnY,50,50)
    obstacles.append(obstacle_rect)
    posX.append(rnX)
    posY.append(rnY)
    # obstacles.append(obstacle_rect)

BG = (50,50,50)
GREEN = (0,255,0)
BLUE = (0,0,255)
RED = (255,0,0)

pygame.mouse.set_visible(False)

LORR = random.randint(0,1)
UORRD = random.randint(0,1)


running = True
while(running):
    KTR += 1
    if KTR == 1:
        for obstacle in obstacles:
            # CRR = random.randint(0, 10)
            # CRRD = random.randint(0, 10)
            # if CRR == 10:
            LORR = random.randint(0,1)
            # if CRRD == 10:
            UORRD = random.randint(0,1)
            # print("LEFT",obstacle.left, LORR)
            # print("TOP",obstacle.top, UORRD)
            if LORR == 1:
                obstacle.left += CHNGVALUE
            else:
                obstacle.left -= CHNGVALUE
            if UORRD == 1:
                obstacle.top += CHNGVALUE
            else:
                obstacle.top -= CHNGVALUE
            if obstacle.left >= 600:
                obstacle.left -= 1
            elif obstacle.left <= 0:
                obstacle.left += 1
            if obstacle.top >= 400:
                obstacle.top -= 1
            elif obstacle.top <= 0:
                obstacle.top += 1
        KTR = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BG)
    col = GREEN
    for obstacle in obstacles:
        if rect_1.collidelist(obstacles) >= 0:
            col = RED
            running = False
    pos = pygame.mouse.get_pos()
    rect_1.center = pos
    pygame.draw.rect(screen,col,rect_1)
    for obstacle in obstacles:
        pygame.draw.rect(screen,BLUE,obstacle)
    pygame.display.flip()
pygame.quit()