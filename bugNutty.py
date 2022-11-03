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
levelThreeAdded = False

allSprites = pygame.sprite.Group()
rats = pygame.sprite.Group()

ratEvent = pygame.USEREVENT + 1
pygame.time.set_timer(ratEvent, 300)
counter = 0

foot = bugSprites.Foot()
hasEnteredFoot = False
hasFootEntered = False
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
        allSprites.add(foot)
        levelTwoAdded = True
    if (level == 3) and (foot.rect.centerx > SCREEN_WIDTH/2) and not hasFootEntered:
        foot.enter()
    if foot.rect.centerx == SCREEN_WIDTH/2:
        hasFootEntered = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == ratEvent:
            if level == 2:
                if random.randint(1,6) >= 3:
                    rat = bugSprites.Rat()
                    allSprites.add(rat)
                    rats.add(rat)


    hitsDoor = pygame.sprite.spritecollide(robug, pygame.sprite.Group(door), False, pygame.sprite.collide_mask)
    hitsRat = pygame.sprite.spritecollide(robug, rats, False, pygame.sprite.collide_mask)
    entersFoot = (robug.rect.x - foot.rect.left > 100) and (robug.rect.y - foot.rect.top > 50) 
    if len(hitsDoor) and level == 1:
        robug.kill()
        door.kill()
        level += 1
    if len(hitsDoor) and level == 2:
        robug.reset()
    if len(hitsRat) and level == 2:
        robug.reset()
    if ((entersFoot and level == 2) or hasEnteredFoot) and not robug.hide:
        hasEnteredFoot = True
        foot.shake(robug)
    if robug.hide and level == 2 and foot.rect.x < SCREEN_WIDTH:
        foot.rect.x += 5
        foot.changeSkin()
    if foot.rect.x >= SCREEN_WIDTH and hasEnteredFoot:
        hasEnteredFoot = False
        foot.reset()
        level += 1
        for rat in rats:
            rat.kill()
    if pygame.mouse.get_pressed()[0]:
        mouseX, mouseY = pygame.mouse.get_pos()
        if ((abs(mouseX - robug.rect.centerx) > 1) or (abs(mouseY - robug.rect.centery) > 1)) and not hasEnteredFoot:
            robug.update()
            costumeCounter +=1
            if costumeCounter%6 == 0:
                robug.updateim()
    robug.rect.clamp_ip(screen.get_rect())
    counter += 1
    if counter%10 == 0:
         for rat in rats:
            rat.updateim()
    allSprites.update()
    

    screen.fill(GREY)
    for s in allSprites:
        screen.blit(s.image, s.rect)
    screen.blit(robug.rotated_image, robug.rect) if not robug.hide else None
    pygame.display.flip()
    clock.tick(60)


pygame.quit()