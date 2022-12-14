import pygame
import math, random

SCREEN_WIDTH, SCREEN_HEIGHT = 750, 750
GREEN = (214, 255, 125)


class Robug(pygame.sprite.Sprite):
    def __init__(self):
        super(Robug, self).__init__()
        self.images = []
        self.images.append(pygame.image.load('assets/robug/robug1.png'))
        self.images.append(pygame.image.load('assets/robug/robug2.png'))
        self.images.append(pygame.image.load('assets/robug/robug3.png'))
        self.images.append(pygame.image.load('assets/robug/robug4.png'))


class Fist(pygame.sprite.Sprite):
    def __init__(self):
        super(Fist, self).__init__()
        self.image = pygame.image.load('assets/fist/Clenched_human_fist.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (200, 200))
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        self.speed = 5
        self.punching = 0

    def update(self):
        rectX, rectY = self.rect.center
        mouseX, mouseY = pygame.mouse.get_pos()
        dy = mouseY - rectY
        dx = mouseX - rectX
        angle = math.atan2(dy, dx)
        self.rect.x += self.speed * math.cos(angle)
        self.rect.y += self.speed * math.sin(angle)
        
    def punch(self):
        self.hitbox = pygame.Rect(self.rect.centerx, self.rect.top, 200, 200)
        self.punching = 1
        self.rect.x += 20
        self.rect.y -= 40

    def unpunch(self):
        self.punching = 0
        self.rect.x -= 20
        self.rect.y += 40

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.image = pygame.Surface((50,50))
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(150, SCREEN_WIDTH-150)
        self.rect.centery = random.randint(150, SCREEN_HEIGHT-150)
        self.dead = False
        self.opacity = 255

    def update(self):
        if self.dead:
            self.opacity -= 5
        self.image.set_alpha(self.opacity)

    def punched(self):
        self.image.fill(GREEN)
        self.dead = True