import pgzrun
import pygame
import time
from pygame.locals import *

pygame.init()
pygame.font.init()

display_surface = pygame.display.set_mode((500, 600))
pygame.display.set_caption("Birthday Card")
img = pygame.image.load("images/cake.jpg")
image = pygame.transform.scale(img, (500, 600))
font = pygame.font.SysFont("Times New Roman", 10)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    font = pygame.font.SysFont("Times New Roman", 72)
    text = font.render("Happy Birthday", True, ("blue"))
    display_surface.fill((255, 255, 255))
    display_surface.blit(text, (0, 300))
    display_surface.blit(image, (0, 0))



    pygame.display.update()
    time.sleep(2)


    img2 = pygame.image.load("images/card.jpg")
    image2 = pygame.transform.scale(img2, (500, 600))

    font2 = pygame.font.SysFont("Times New Roman", 72)
    text2 = font2.render("Happy Birthday!", True, ("blue"))
    display_surface.fill((255, 255, 255))
    display_surface.blit(image2, (0, 0))
    display_surface.blit(text2, (35, 300))

    pygame.display.update()
    time.sleep(2)

    img3 = pygame.image.load("images/gift.jpg")
    image3 = pygame.transform.scale(img3, (250, 250))

    font3 = pygame.font.SysFont("Times New Roman", 72)
    text3 = font3.render("Happy Birthday!", True, ("blue"))
    display_surface.fill((255, 255, 255))
    display_surface.blit(image3, (0, 0))
    display_surface.blit(text3, (35, 300))

    pygame.display.update()
    time.sleep(2)