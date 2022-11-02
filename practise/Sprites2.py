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
        self.rotated_image = self.image.copy()
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        self.angle = 0
        
    
    def update(self):
        rectX, rectY = self.rect.center
        mouseX, mouseY = pygame.mouse.get_pos()
        dy = mouseY - rectY
        dx = mouseX - rectX
        self.angle = math.atan2(dy, dx)
        self.rect.x += self.speed * math.cos(self.angle)
        self.rect.y += self.speed * math.sin(self.angle)
        self.rotated_image = pygame.transform.rotate(self.image, ((180/math.pi)*-self.angle)-90)
        self.rect = self.image.get_rect(center=self.rect.center )
        
       

    def updateim(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        
        self.image = self.images[self.index]
    
