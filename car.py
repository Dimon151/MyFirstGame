# coding UTF-8
from pygame.sprite import Sprite
from pygame.image import load

# pygame.init()
from citys_geo import w, h

MOVE_SPEED = 4

w = w + 120
h = h + 150


class Car(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = load("img//pikup.png")
        # self.image = Surface((30, 40))
        # self.image.fill((50, 50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, left, right, up, down):
        if left:
            if self.rect.x <= 0:
                self.rect.x = 0
            else:
                self.rect.x += - MOVE_SPEED
            self.image = load("img//pikup_L.png")

        if right:
            if self.rect.x >= h:
                self.rect.x = h
            else:
                self.rect.x += MOVE_SPEED
            self.image = load("img//pikup_R.png")
        if up:
            if self.rect.y <= 0:
                self.rect.y = 0
            else:
                self.rect.y += - MOVE_SPEED
            self.image = load("img//pikup_U.png")
            if left:
                self.image = load("img//pikup_UL.png")
            if right:
                self.image = load("img//pikup_UR.png")
        if down:
            if self.rect.y >= w:
                self.rect.y = w
            else:
                self.rect.y += MOVE_SPEED
            self.image = load("img//pikup_D.png")
            if left:
                self.image = load("img//pikup_DL.png")
            if right:
                self.image = load("img//pikup_DR.png")

    def draw(self, surf):
        surf.blit(self.image, (self.rect.x, self.rect.y))

    def get_xy(self):
        return self.rect.x, self.rect.y
