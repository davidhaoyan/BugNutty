import pygame
import math, random

SCREEN_WIDTH, SCREEN_HEIGHT = 750, 750

class Robug(pygame.sprite.Sprite):
    def __init__(self):
        super(Robug, self).__init__()
        self.images = []
        self.images.append(pygame.image.load('assets/robug/robug1.png'))
        self.images.append(pygame.image.load('assets/robug/robug2.png'))
        self.images.append(pygame.image.load('assets/robug/robug3.png'))
        self.images.append(pygame.image.load('assets/robug/robug4.png'))
        self.index = 0
        self.speed = 5
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

    def updateim(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        
        self.image = self.images[self.index]
