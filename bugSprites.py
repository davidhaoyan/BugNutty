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
        self.speed = 4
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.pos = (SCREEN_WIDTH/2, SCREEN_HEIGHT)
        self.rect.center = self.pos
        self.mask = pygame.mask.from_surface(self.image)
        self.rotated_image = self.image

    def reset(self):
        self.rect.centerx = SCREEN_WIDTH/2
        self.rect.centery = SCREEN_HEIGHT

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
        self.image = pygame.Surface((100,30))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.top = 0
        self.rect.centerx = SCREEN_WIDTH/2
        self.green = False
        self.mask = pygame.mask.from_surface(self.image)

    def changeColour(self):
        self.green = True

    def update(self):
        if self.green:
            self.image.fill(GREEN)

class Rat(pygame.sprite.Sprite):
    def __init__(self):
        super(Rat, self).__init__()
        self.image = pygame.Surface((100,60))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.spawnLeft = random.randint(0,1)
        if self.spawnLeft:
            self.rect.centerx = 0
        else:
            self.rect.centerx = SCREEN_WIDTH
        self.rect.centery = random.randint(100, SCREEN_HEIGHT-200)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        if self.spawnLeft:
            self.rect.x += 4
        else:
            self.rect.x -= 4
        if (self.rect.x > SCREEN_WIDTH+100) or (self.rect.x < -100):
            self.kill()

class Foot(pygame.sprite.Sprite):
    def __init__(self):
        super(Foot, self).__init__()
        self.image = pygame.image.load('assets/factory/footpic.png')
        self.rect = self.image.get_rect()
        self.rect.right = SCREEN_WIDTH
        self.rect.y = SCREEN_HEIGHT - 300

