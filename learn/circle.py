import pygame
import math
import os
pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 750, 750
GREY = (79, 79, 79)
GREEN = (214, 255, 125)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        """self.image = pygame.Surface((50, 50))
        self.image.fill((0,0,0))"""
        self.image = pygame.image.load(r"C:\Users\david\Documents\bug nutty\BugNutty\learn\Clenched_human_fist.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (300, 300))
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        self.speed = 10

    def update(self):
        rectX, rectY = self.rect.center
        mouseX, mouseY = pygame.mouse.get_pos()
        dy = mouseY - rectY
        dx = mouseX - rectX
        angle = math.atan2(dy, dx)
        self.rect.x += self.speed * math.cos(angle)
        self.rect.y += self.speed * math.sin(angle)
        
    def punch(self):
        self.rect.y -= 30

    def unpunch(self):
        self.rect.y += 30

player = Player()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                player.punch()
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 3:
                player.unpunch()
    if pygame.mouse.get_pressed()[0]:
        mouseX, mouseY = pygame.mouse.get_pos()
        if (abs(mouseX - player.rect.centerx) > 10) & (abs(mouseY - player.rect.centery) > 10):
            player.update()
    player.rect.clamp_ip(screen.get_rect())

    screen.fill(GREY)
    screen.blit(player.image, player.rect)
    pygame.display.flip()
    clock.tick(30)


pygame.quit()