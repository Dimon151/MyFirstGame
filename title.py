# coding UTF-8

from pygame.sprite import Sprite
from pygame.image import load

#pygame.init()

class City(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = load("texture//desert&city.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw(self, surf):
        surf.blit(self.image, (self.rect.x, self.rect.y))

class Desert(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = load("texture//desert2.jpg")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Montans1(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = load("texture//Montanas1.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Montans2(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = load("texture//Montanas2.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
