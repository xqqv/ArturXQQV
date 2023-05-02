from pygame.locals import *
import pygame, sys

pygame.init()

kollane = [255, 255, 10]
punane = [255, 0, 0]
hall = [200, 200, 200]
roosa = [255, 150, 255]
roheline = [100, 255, 100]

X = 640
Y = 480
ekraan = pygame.display.set_mode([X, Y])
pygame.display.set_caption("Animatsion")
ekraan.fill(roheline)

mesilane = pygame.image.load("bee.png")
posX = 0
posY = 0

direction = "right"

samm = 1

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if direction == "right":
        posX += samm
        if posX >= X - mesilane.get_rect().width:
            direction = "down"
    elif direction == "down":
        posY += samm
        if posY >= Y - mesilane.get_rect().height:
            direction = "left"
    elif direction == "left":
        posX -= samm
        if posX <= 0:
            direction = "up"
    elif direction == "up":
        posY -= samm
        if posY <= 0:
            direction = "right"

    ekraan.fill(roheline)
    ekraan.blit(mesilane, (posX, posY))
    pygame.display.update()
    pygame.time.Clock().tick(60)
