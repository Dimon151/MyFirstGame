import random
import pygame
import math


from settings import WIDTH, HEIGHT
from title import Desert, Montans1, Montans2, City

#### ГЕНЕРАЦИЯ МИРА

#### Города отступы от края карты
h = int((HEIGHT - 2) * 100)
w = int((WIDTH - 2) * 100)


#### Названия городов

# min_dist = 50 * h


# def dist(x1, y1, x2, y2):
#     x = (x1 - x2)
#     y = (y1 - y2)
#
#     return math.hypot(x, y)


def city_name(n):
    name_c_1 = ["Волчий", "Дикий", "Жгучий", "Зеленый", "Чёрный", "Железный", "Пустынный", "Собачий", "Чертов",
                "Вороний"]
    name_c_2 = ["город", "яр", "пруд", "куст", "камень", "сук", "рубеж", "рог", "грот"]

    city_name_list = []
    for i in range(n):
        city_name_gen = '{} {}'.format(random.choice(name_c_1), random.choice(name_c_2))
        if i not in city_name_list:
            city_name_list.append(city_name_gen)

    # while True:
    #     city_name_gen1 = '{} {}'.format(random.choice(name_c_1), random.choice(name_c_2))
    #     city_name_gen2 = '{} {}'.format(random.choice(name_c_1), random.choice(name_c_2))
    #     city_name_gen3 = '{} {}'.format(random.choice(name_c_1), random.choice(name_c_2))
    #     if city_name_gen1 == city_name_gen2 or city_name_gen2 == city_name_gen3 or city_name_gen1 == city_name_gen3:
    #         continue
    #     else:
    #         break

    # return city_name_gen1, city_name_gen2, city_name_gen3
    return city_name_list

### distance city

# def citys_geo():
#     def city_x():
#         return random.randint(1, h) * 100
#
#     def city_y():
#         return random.randint(1, w) * 100
#
#     dist_OK = 0
#     while dist_OK == 0:
#         city1_x = city_x()
#         city1_y = city_y()
#         city2_x = city_x()
#         city2_y = city_y()
#         city3_x = city_x()
#         city3_y = city_y()
#         city4_x = city_x()
#         city4_y = city_y()
#         city5_x = city_x()
#         city5_y = city_y()
#
#         dict_1_2 = (dist(city1_x + 50, city1_y + 50, city2_x + 50, city2_y + 50))
#         dict_1_3 = (dist(city1_x + 50, city1_y + 50, city3_x + 50, city3_y + 50))
#         dict_1_4 = (dist(city1_x + 50, city1_y + 50, city3_x + 50, city3_y + 50))
#         dict_1_5 = (dist(city1_x + 50, city1_y + 50, city3_x + 50, city3_y + 50))
#         dict_2_3 = (dist(city2_x + 50, city2_y + 50, city3_x + 50, city3_y + 50))
#         dict_2_4 = (dist(city2_x + 50, city2_y + 50, city3_x + 50, city3_y + 50))
#         dict_2_5 = (dist(city2_x + 50, city2_y + 50, city3_x + 50, city3_y + 50))
#         dict_3_4 = (dist(city2_x + 50, city2_y + 50, city3_x + 50, city3_y + 50))
#         dict_3_5 = (dist(city2_x + 50, city2_y + 50, city3_x + 50, city3_y + 50))
#         dict_4_5 = (dist(city2_x + 50, city2_y + 50, city3_x + 50, city3_y + 50))
#
#
#         if dict_1_2 < min_dist:
#             dist_OK = 0
#         elif dict_1_3 < min_dist:
#             dist_OK = 0
#         elif dict_2_3 < min_dist:
#             dist_OK = 0
#         else:
#             dist_OK = 1
#     city_xy_1 = city1_x, city1_y
#     city_xy_2 = city2_x, city2_y
#     city_xy_3 = city3_x, city3_y
#     return city_xy_1, city_xy_2, city_xy_3


#### Генерация глобальной карты

#### расчёт количества тайлов START


def gen_titles(list_city_xy):
    titles = int(WIDTH * HEIGHT)  # all titles
    # print(titles)
    montans1 = int(math.ceil(titles * 0.15))  # titles montans 1
    montans2 = int(math.ceil(titles * 0.15))  # titles montans 1
    desert = int(math.ceil(titles * 0.70))  # titles desert


    list_city = []

    for xy in list_city_xy:
        city = City(xy[0], xy[1])
        list_city.append(city)

    #### расчёт количества тайлов END

    titlarray = []

    ### присваиваем талам id и создаём список тайлов по id

    for i in range(montans1):
        titlarray.append(1)

    for i in range(montans2):
        titlarray.append(2)

    for i in range(desert):
        titlarray.append(0)

    # print(titlarray)
    random.shuffle(titlarray)  # перемешиваем id тайлов

    # map_tile = ['desert2.jpg', 'Montanas1.png', 'Montanas2.png']

    def chunks(lst, chunk_count):
        chunk_size = len(lst) // chunk_count
        return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]

    titls = chunks(titlarray, int(WIDTH))  # создаёт список кортеджей с id тайлов

    # print(titls)

    city_group = pygame.sprite.Group()
    sprite_group = pygame.sprite.Group()
    # city_group.add((city1, city2, city3))
    city_group.add(list_city)

    #### создаёт двумерный массив с id тайлов

    map_arr = []

    x = 0
    y = 0

    for row in titls:
        row_titls = str(row)
        row_titls = row_titls.replace('[', '')
        row_titls = row_titls.replace(']', '')
        row_titls = row_titls.replace(' ', '')
        row_titls = row_titls.replace(',', '')
        for i in row_titls:
            if i == '0':
                sprite_group.add(Desert(x, y))
                map_arr.append(Desert(x, y))
            if i == '1':
                sprite_group.add(Montans1(x, y))
                map_arr.append(Montans1(x, y))
            if i == '2':
                sprite_group.add(Montans2(x, y))
                map_arr.append(Montans2(x, y))
            x += 100
        y += 100
        x = 0
    return map_arr, city_group, sprite_group, titls
    # print(titls)


if __name__ == "__main__":
    from citys_geo import citys_geo
    from settings import n_city

    print(city_name(3))
    # print(citys_geo())
    list_city_xy = citys_geo(n_city)
    print(list_city_xy)
    gen_titles(list_city_xy)
    print(gen_titles())
