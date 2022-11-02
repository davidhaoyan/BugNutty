import pygame
import math, random

SCREEN_WIDTH, SCREEN_HEIGHT = 750, 750
GREEN = (214, 255, 125)

class Robug(pygame.sprite.Sprite):
    def __init__(self):
        super(Robug, self).__init__()
        self.images = []
        self.images.append(pygame.image.load('assets/robug/robug164.png'))
        self.images.append(pygame.image.load('assets/robug/robug264.png'))
        self.images.append(pygame.image.load('assets/robug/robug364.png'))
        self.images.append(pygame.image.load('assets/robug/robug464.png'))
        self.index = 0
        self.speed = 3
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.pos = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        self.rect.center = self.pos
        self.rotated_image = self.image
        self.hitbox = pygame.Rect(0, 26, 64, 64)
    
    def update(self):
        rectX, rectY = self.rect.center
        mouseX, mouseY = pygame.mouse.get_pos()
        dy = mouseY - rectY
        dx = mouseX - rectX
        self.angle = math.atan2(dy, dx)
        self.rect.x += self.speed * math.cos(self.angle)
        self.rect.y += self.speed * math.sin(self.angle)
        self.pos = (self.rect.centerx, self.rect.centery)
        self.rotated_image = pygame.transform.rotate(self.image, ((180/math.pi)*-self.angle)-90)
        self.rect = self.rotated_image.get_rect()
        self.rect.center = self.pos

    def updateim(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]

        
class Door(pygame.sprite.Sprite):
    def __init__(self):
        super(Door, self).__init__()
        self.image = pygame.Surface((100,100))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.top = 0
        self.rect.centerx = SCREEN_WIDTH/2
        self.finish = False

    def accept(self):
        self.finish = True

    def update(self):
        if self.finish:
            self.image.fill(GREEN)