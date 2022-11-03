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
level = 0

running = True
levelOneAdded = False
levelTwoAdded = False
levelThreeAdded = False

allSprites = pygame.sprite.Group()
rats = pygame.sprite.Group()
enemies = pygame.sprite.Group()

ratEvent = pygame.USEREVENT + 1
pygame.time.set_timer(ratEvent, 300)
enemyEvent = pygame.USEREVENT + 2
pygame.time.set_timer(enemyEvent, 500)
ratCounter = 0
wingCounter = 2

foot = bugSprites.Foot()
robug = bugSprites.Robug()
door = bugSprites.Door()
intro = bugSprites.Intro()
background = bugSprites.Background()
allSprites.add(background)
hasEnteredFoot = False
while running:
    if (level == 0):
        allSprites.add(intro)
        robug.hide = True
    if (level == 1) and not levelOneAdded:
        robug.hide = False
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
    if (level == 3):
        foot.enter()
    if (level == 5 and not robug.playing):
        robug.hide = False 
        robug.play()
        robug.speed = 3
        robug.playing = True
        robug.update()
        robug.updateim()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                foot.punch()
                for enemy in enemies:
                    if foot.hitbox.colliderect(enemy.rect) and not enemy.dead and not enemy.wing:
                        if random.randint(1,5) == 1:
                            if wingCounter > 0:
                                enemy.dropWing()
                                enemy.wing = True
                                wingCounter -= 1
                            else:
                                enemy.punched()
                        else:
                            enemy.punched()
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 3:
                foot.unpunch()    
        elif event.type == ratEvent:
            if level == 2:
                if random.randint(1,5) >= 3:
                    rat = bugSprites.Rat()
                    allSprites.add(rat)
                    rats.add(rat)
        elif (event.type == enemyEvent) and wingCounter > 0:
            if level == 3:
                enemy = bugSprites.Enemy()
                enemies.add(enemy)
                allSprites.add(enemy)

    hitsDoor = pygame.sprite.spritecollide(robug, pygame.sprite.Group(door), False, pygame.sprite.collide_mask)
    hitsRat = pygame.sprite.spritecollide(robug, rats, False, pygame.sprite.collide_mask)
    entersFoot = (robug.rect.x - foot.rect.left > 100) and (robug.rect.y - foot.rect.top > 50) 
    if intro.finished and level == 0:
        level = 1
        intro.kill()
    if len(hitsDoor) and level == 1:
        robug.kill()
        door.kill()
        level = 2
    if len(hitsDoor) and level == 2:
        robug.reset()
    if len(hitsRat) and level == 2:
        robug.reset()
    if ((entersFoot and level == 2) or hasEnteredFoot):
        hasEnteredFoot = True
        foot.changeSkin(robug)
    if level == 2 and foot.rect.x < SCREEN_WIDTH and robug.hide and foot.index >= 14 and level != 4:
        foot.rect.x += 4
    if foot.rect.x >= SCREEN_WIDTH and hasEnteredFoot and level != 4:
        hasEnteredFoot = False
        foot.reset()
        door.kill()
        level = 3
        for rat in rats:
            rat.kill()
    if wingCounter == 0:
        level = 4
        for enemy in enemies:
            if not enemy.wing:
                enemy.kill()
            if enemy.wing:
                enemy.leaving = True
                enemy.leave(foot)
        foot.leaving = True
        foot.exit()
    if level == 4 and foot.rect.left > SCREEN_WIDTH:
        foot.kill()
        for enemy in enemies:
            enemy.kill()
        level = 5

    if pygame.mouse.get_pressed()[0]:
        mouseX, mouseY = pygame.mouse.get_pos()
        if ((abs(mouseX - robug.rect.centerx) > 1) or (abs(mouseY - robug.rect.centery) > 1)) and not hasEnteredFoot:
            robug.update()
            costumeCounter +=1
            if costumeCounter%6 == 0:
                robug.updateim()
        if (abs(mouseX - foot.rect.centerx) > 1) and (abs(mouseY - foot.rect.centery) > 1) and level == 3 and foot.playable:
            foot.move()
    robug.rect.clamp_ip(screen.get_rect())
    ratCounter += 1
    if ratCounter%10 == 0:
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