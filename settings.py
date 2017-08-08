import pygame

pygame.init()
pygame.font.init()

WIDTH = 630             # высота
HEIGHT = 1000           # ширина
SIZE = (HEIGHT, WIDTH)

window = pygame.display.set_mode((SIZE))
pygame.display.set_caption('My Game')
screen = pygame.Surface((HEIGHT, WIDTH - 30))
info_string = pygame.Surface((HEIGHT, 30))
"""Шрифты"""

city_font = pygame.font.Font(None, 25)