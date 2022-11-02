import pygame
import math
import bugSprites
pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 750, 750
GREY = (79, 79, 79)
GREEN = (214, 255, 125)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
costumeCounter = 0
level = 1

running = True
levelOneAdded = False
while running:
    if (level == 1) and not levelOneAdded:
        robug = bugSprites.Robug()
        door = bugSprites.Door()
        levelOneAdded = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if pygame.mouse.get_pressed()[0]:
        mouseX, mouseY = pygame.mouse.get_pos()
        if (abs(mouseX - robug.rect.centerx) > 1) and (abs(mouseY - robug.rect.centery) > 1):
            robug.update()
            costumeCounter +=1
            if costumeCounter%6 == 0:
                robug.updateim()
    robug.rect.clamp_ip(screen.get_rect())


    screen.fill(GREY)
    screen.blit(door.image, door.rect)
    screen.blit(robug.image, robug.rect)
    pygame.display.flip()
    clock.tick(60)


pygame.quit()