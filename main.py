#! coding UTF-8

from settings import *
from WorldGen import * #WorldGen
#from camera import *
from car import Car

pygame.init()

"""герой"""

city_list = ((city1_x, city1_y), (city2_x, city2_y), (city3_x, city3_y))
city_rdm = random.choice(city_list)

hero = Car((city_rdm[0] + 120), city_rdm[1] + 25)
left = right = up = down = False

unit_group.add(hero)

#WorldGen()

#camera = Camera(camera_func, total_titls_width, total_titls_height)

done = True
timer = pygame.time.Clock()
while done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False
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

    """Отрисовка объектов"""

    sprite_group.draw(screen)
    info_string.fill((150, 150, 150))

    """отрисовка строений"""
    city_group.draw(screen)

    '''отрисовка шрифтов'''
    screen.blit(city_font.render(city_name_gen1, 1, (50, 50, 150)), ((city1_x + 10), (city1_y + 80)))
    screen.blit(city_font.render(city_name_gen2, 1, (50, 50, 150)), ((city2_x + 10), (city2_y + 80)))
    screen.blit(city_font.render(city_name_gen3, 1, (50, 50, 150)), ((city3_x + 10), (city3_y + 80)))

    """отображение героя"""
    hero.update(left, right, up, down)
    unit_group.draw(screen)

    """Отрисовка холста на экране"""
    window.blit(info_string, (0, 0))
    window.blit(screen, (0, 30))

    """обновляем окно"""
    pygame.display.flip()
    timer.tick(45)