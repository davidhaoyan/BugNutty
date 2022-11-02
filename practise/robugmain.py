import pygame
import math
import Sprites2
pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 750, 750
GREY = (79, 79, 79)
GREEN = (214, 255, 125)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
robug = Sprites2.Robug()
clock = pygame.time.Clock()
counter = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if pygame.mouse.get_pressed()[0]:
        mouseX, mouseY = pygame.mouse.get_pos()
        if (abs(mouseX - robug.rect.centerx) > 1) and (abs(mouseY - robug.rect.centery) > 1):
            robug.update()
            counter +=1
            if counter%8 == 0:
                robug.updateim()
    robug.rect.clamp_ip(screen.get_rect())

    screen.fill(GREY)
    screen.blit(robug.image, robug.rect)
    pygame.display.flip()
    clock.tick(60)


pygame.quit()