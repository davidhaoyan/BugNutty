import pygame
import math, random

SCREEN_WIDTH, SCREEN_HEIGHT = 750, 750

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
        self.rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    def update(self):
        rectX, rectY = self.rect.center
        mouseX, mouseY = pygame.mouse.get_pos()
        dy = mouseY - rectY
        dx = mouseX - rectX
        angle = math.atan2(dy, dx)
        self.rect.x += self.speed * math.cos(angle)
        self.rect.y += self.speed * math.sin(angle)
        pygame.transform.rotate(self.image, angle)

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