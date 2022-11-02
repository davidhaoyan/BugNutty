import pygame
import math
import Sprites
pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 750, 750
GREY = (79, 79, 79)
GREEN = (214, 255, 125)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

fist = Sprites.Fist()
Enemies = pygame.sprite.Group()

enemyEvent = pygame.USEREVENT + 1
pygame.time.set_timer(enemyEvent, 2000)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
                fist.punch()
                getsHit = pygame.sprite.spritecollide(fist, Enemies, True)
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 3:
                fist.unpunch()
        elif event.type == enemyEvent:
                enemy = Sprites.Enemy()
                Enemies.add(enemy)
    if pygame.mouse.get_pressed()[0]:
        mouseX, mouseY = pygame.mouse.get_pos()
        if (abs(mouseX - fist.rect.centerx) > 1) & (abs(mouseY - fist.rect.centery) > 1):
            fist.update()
    fist.rect.clamp_ip(screen.get_rect())

    screen.fill(GREY)
    screen.blit(fist.image, fist.rect)
    Enemies.draw(screen)
    pygame.display.flip()
    clock.tick(60)


pygame.quit()