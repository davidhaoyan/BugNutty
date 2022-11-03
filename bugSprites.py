import pygame
import math, random, time

SCREEN_WIDTH, SCREEN_HEIGHT = 750, 750
GREEN = (214, 255, 125)

class Robug(pygame.sprite.Sprite):
    def __init__(self):
        super(Robug, self).__init__()
        self.images = []
        for i in range(1,5):
            path = "assets/robug/robug{}64.png"
            self.images.append(pygame.image.load(path.format(i)))
        self.index = 0
        self.speed = 4
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.pos = (SCREEN_WIDTH/2, SCREEN_HEIGHT)
        self.rect.center = self.pos
        self.mask = pygame.mask.from_surface(self.image)
        self.rotated_image = self.image
        self.hide = False

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
        self.enterright = []
        self.enterright.append(pygame.image.load('assets/enemy/rat1.png'))
        self.enterright.append(pygame.image.load('assets/enemy/rat2.png'))
        self.enterleft = []
        self.enterleft.append(pygame.image.load('assets/enemy/ratright1.png'))
        self.enterleft.append(pygame.image.load('assets/enemy/ratright2.png'))
        self.index = 0
        self.image = self.enterright[self.index]
        self.rect = self.image.get_rect()
        self.spawnLeft = random.randint(0,1)
        if self.spawnLeft:
            self.rect.centerx = 0
            self.image = self.enterleft[self.index]
        else:
            self.rect.centerx = SCREEN_WIDTH
            self.image = self.enterright[self.index]
        self.rect.centery = random.randint(100, SCREEN_HEIGHT-350)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        if self.spawnLeft:
            self.rect.x += 4
        else:
            self.rect.x -= 4
        if (self.rect.x > SCREEN_WIDTH+100) or (self.rect.x < -100):
            self.kill()


    def updateim(self):
        self.index += 1
        if self.index >= 2:
            self.index = 0
        
        if self.spawnLeft:
            self.image = self.enterleft[self.index]
        else:
            self.image = self.enterright[self.index]


        



class Foot(pygame.sprite.Sprite):
    def __init__(self):
        super(Foot, self).__init__()
        self.image = pygame.image.load("assets/factory/halffoot.png")
        self.images = []
        for i in range(1,15):
            path = "assets/factory/footimations/foot{}.png"
            self.images.append(pygame.image.load(path.format(i)))
        self.index = 0
        self.rect = self.image.get_rect()
        self.rect.right = SCREEN_WIDTH + 250
        self.rect.y = SCREEN_HEIGHT - 300
        self.mask = pygame.mask.from_surface(self.image)
        self.counter = 0
        self.speed = 5
        self.punching = 0
        self.playable = False

    def changeSkin(self, robug):  
        if self.counter == 0:
            robug.hide = True
        if self.counter % 4 == 0:
            self.index += 1
            if self.index < 14:
                self.image = self.images[self.index]    

    def reset(self):
        self.counter = 0
        self.rect.centery = SCREEN_HEIGHT/2
        self.rect.left = SCREEN_WIDTH

    def enter(self):
        self.counter += 1
        if (self.counter % 2 == 0) and (self.rect.centerx > SCREEN_WIDTH/2) and not self.playable:
            self.rect.x -= 10
        elif (self.counter % 2 == 0) and not self.playable:
            self.playable = True

    def move(self):
        if self.playable:
            rectX, rectY = self.rect.center
            mouseX, mouseY = pygame.mouse.get_pos()
            dy = mouseY - rectY
            dx = mouseX - rectX
            angle = math.atan2(dy, dx)
            self.rect.x += self.speed * math.cos(angle)
            self.rect.y += self.speed * math.sin(angle)
        
    def punch(self):
        self.hitbox = self.rect
        self.punching = 1
        self.rect.x -= 20
        self.rect.y += 40

    def unpunch(self):
        self.punching = 0
        self.rect.x += 20
        self.rect.y -= 40

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


