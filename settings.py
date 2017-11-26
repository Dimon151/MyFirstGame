from math import pi
import pygame

pygame.init()
pygame.font.init()


WIDTH = 10  # 630             # высота
HEIGHT = 10  # 1000           # ширина
SIZE = (600, 480)
n_city = int((HEIGHT * WIDTH * 10000) / (pi * 250 ** 2) * 0.8)
# print(n_city)

window = pygame.display.set_mode((SIZE))
pygame.display.set_caption('My Game')
screen = pygame.Surface((HEIGHT * 100, WIDTH * 100))
info_string = pygame.Surface((SIZE[0], 30))
"""Шрифты"""


city_font = pygame.font.Font(None, 25)