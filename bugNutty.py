import pygame
import math, random
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
levelTwoAdded = False

allSprites = pygame.sprite.Group()
rats = pygame.sprite.Group()

ratEvent = pygame.USEREVENT + 1
pygame.time.set_timer(ratEvent, 300)

while running:
    if (level == 1) and not levelOneAdded:
        robug = bugSprites.Robug()
        door = bugSprites.Door()
        allSprites.add(door)
        levelOneAdded = True
    if (level == 2) and not levelTwoAdded:
        robug.reset()
        robug.speed = 3
        door = bugSprites.Door()
        door.changeColour()
        allSprites.add(door)
        foot = bugSprites.Foot()
        allSprites.add(foot)
        levelTwoAdded = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == ratEvent:
            if level == 2:
                if random.randint(1,5) >= 3:
                    rat = bugSprites.Rat()
                    allSprites.add(rat)
                    rats.add(rat)


    hitsDoor = pygame.sprite.spritecollide(robug, pygame.sprite.Group(door), False, pygame.sprite.collide_mask)
    hitsRat = pygame.sprite.spritecollide(robug, rats, False, pygame.sprite.collide_mask)
    if len(hitsDoor) and level == 1:
        robug.kill()
        door.kill()
        level += 1
    if len(hitsDoor) and level == 2:
        robug.reset()
        print(level)
    if len(hitsRat) and level == 2:
        robug.reset()
    if pygame.mouse.get_pressed()[0]:
        mouseX, mouseY = pygame.mouse.get_pos()
        if (abs(mouseX - robug.rect.centerx) > 1) or (abs(mouseY - robug.rect.centery) > 1):
            robug.update()
            costumeCounter +=1
            if costumeCounter%6 == 0:
                robug.updateim()
    robug.rect.clamp_ip(screen.get_rect())
    allSprites.update()

    screen.fill(GREY)
    for s in allSprites:
        screen.blit(s.image, s.rect)
    screen.blit(robug.rotated_image, robug.rect)
    pygame.display.flip()
    clock.tick(60)


pygame.quit()