#! coding UTF-8
import random

import pygame

from camera import Camera
from camera import camera_func
from citys_geo import citys_geo
from settings import n_city, info_string, screen, city_font, window
from WorldGen import city_name, gen_titles
from car import Car
from title import City
from units import unit_group

list_city_xy = citys_geo(n_city)
print(list_city_xy)
city_name_list = city_name(n_city)
# print(city_name_list)
map_arr, city_group, sprite_group, titls = gen_titles(list_city_xy)

city_list = []
for i in list_city_xy:
    city_list.append(City(i[0], i[1]))

city_font_list = list(zip(city_name_list, list_city_xy))

"""герой"""

city_rdm = random.choice(city_list)

hero = Car((city_rdm.rect.x + 120), city_rdm.rect.y + 25)
# hero = Car(100, 100)
left = right = up = down = False

unit_group.add(hero)

total_titls_width = len(titls[0]) * 100
total_titls_height = len(titls) * 100

camera = Camera(camera_func, total_titls_width, total_titls_height)

pygame.init()

done = True
timer = pygame.time.Clock()
while done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.display.quit()
            done = False
            exit()
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                done = False

            if e.key == pygame.K_LEFT:
                left = True

            if e.key == pygame.K_RIGHT:
                right = True

            if e.key == pygame.K_UP:
                up = True

            if e.key == pygame.K_DOWN:
                down = True

        if e.type == pygame.KEYUP:
            if e.key == pygame.K_LEFT:
                left = False

            if e.key == pygame.K_RIGHT:
                right = False

            if e.key == pygame.K_UP:
                up = False

            if e.key == pygame.K_DOWN:
                down = False
        if e.type == pygame.K_ESCAPE:
            pygame.display.quit()
            exit()

    """Отрисовка объектов"""

    info_string.fill((150, 150, 150))

    """отображение героя"""
    hero.update(left, right, up, down)
    camera.update(hero)

    for e in sprite_group:
        screen.blit(e.image, camera.apply(e))

    """отрисовка строений"""
    for e in city_group:
        screen.blit(e.image, camera.apply(e))

    """отрисовка шрифтов"""

    ind = 0
    for e in city_group:
        screen.blit(e.image, camera.apply(e))
        screen.blit(city_font.render(city_name_list[ind], 1, (50, 50, 150)), camera.apply(e))
        ind += 1

    screen.blit(hero.image, camera.apply(hero))

    """Отрисовка холста на экране"""
    window.blit(info_string, (0, 0))
    window.blit(screen, (0, 30))

    """обновляем окно"""
    pygame.display.flip()
    timer.tick(45)
