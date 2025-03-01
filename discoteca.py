import pygame
import random
from colours import *
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("../shipwar/resources/party.mp3")
pygame.mixer.music.play(-1)
size = (1280,720)
screen = pygame.display.set_mode(size,pygame.FULLSCREEN)
pygame.display.set_caption('Party')
BACKGROUND = (255,255,255)
screen.fill(BACKGROUND)
COLORS = [RED,GREEN,BLACK,WHITE,BLUE,YELLOW,CYAN,MAGENTA,MAROON,GOLD,SILVER,TEAL,OLIVE,LIME,PINK,PURPLE,BROWN,GRAY,NAVY]
FPS = 0
clock = pygame.time.Clock()
running = True
timer = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(random.choice(COLORS))
    pygame.time.delay(random.randint(200,800))
    for _ in range(10):
        x = random.randint(0,1000)
        y = random.randint(0,1000)
        radius = random.randint(10,100)
        color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        pygame.draw.circle(screen, color, (x,y), radius)
        pygame.display.flip()

pygame.quit()