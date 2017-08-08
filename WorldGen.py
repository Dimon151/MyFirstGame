import random
import pygame
import math

from settings import WIDTH, HEIGHT, city_font
from title import Desert, Montans1, Montans2, City

#### ГЕНЕРАЦИЯ МИРА

#### Города отступы от края карты
h = int(HEIGHT / 100) - 2
w = int((WIDTH - 30) / 100) - 2

#### Названия городов

def city_name(C_NAME: str, x_cn: int, y_cn: int) -> None:       #### Render city name
    city_font.render(C_NAME, 1, (50, 50, 50)), (x_cn, y_cn)


name_c_1 = ["Волчий", "Дикий", "Жгучий", "Зеленый", "Чёрный", "Железный", "Пустынный", "Собачий", "Чертов", "Вороний"]
name_c_2 = ["город", "яр", "пруд", "куст", "камень", "сук", "рубеж", "рог", "грот"]

while True:  # not pythonic way
    city_name_gen1 = '{} {}'.format(random.choice(name_c_1), random.choice(name_c_2))
    city_name_gen2 = '{} {}'.format(random.choice(name_c_1), random.choice(name_c_2))
    city_name_gen3 = '{} {}'.format(random.choice(name_c_1), random.choice(name_c_2))
    condition = city_name_gen1 == city_name_gen2 or city_name_gen2 == city_name_gen3 \
                or city_name_gen1 == city_name_gen3
    if condition:
        continue
    else:
        break

print(city_name_gen1, city_name_gen2, city_name_gen3)


### distance city

def dist(x1, y1, x2, y2):
    x = (x1 - x2)
    y = (y1 - y2)

    return math.hypot(x, y)

min_dist = 50 * h

dist_OK = 0
while dist_OK == 0:
    city1_x = random.randint(1, h) * 100
    city1_y = random.randint(1, w) * 100
    city2_x = random.randint(1, h) * 100
    city2_y = random.randint(1, w) * 100
    city3_x = random.randint(1, h) * 100
    city3_y = random.randint(1, w) * 100

    dict_1_2 = (dist(city1_x + 50, city1_y + 50, city2_x + 50, city2_y + 50))
    dict_1_3 = (dist(city1_x + 50, city1_y + 50, city3_x + 50, city3_y + 50))
    dict_2_3 = (dist(city2_x + 50, city2_y + 50, city3_x + 50, city3_y + 50))

    if dict_1_2 < min_dist:
        dist_OK = 0
    elif dict_1_3 < min_dist:
        dist_OK = 0
    elif dict_2_3 < min_dist:
        dist_OK = 0
    else:
        dist_OK = 1
    #return city1_x, city1_y,city2_x, city2_y, city3_x, city3_y

city1 = City(city1_x, city1_y)
city2 = City(city2_x, city2_y)
city3 = City(city3_x, city3_y)

#### Генерация глобальной карты

#### расчёт количества тайлов START

titles = int(((WIDTH - 30) / 100) * (HEIGHT / 100)) # all titles
print(titles)
montans1 = int(math.ceil(titles * 0.15))     # titles montans 1
montans2 = int(math.ceil(titles * 0.15))     # titles montans 1
desert = int(math.ceil(titles * 0.70))      # titles desert

#### расчёт количества тайлов END

titlarray = []

### присваиваем талам id и создаём список тайлов по id

for i in range(montans1):
    titlarray.append(1)

for i in range(montans2):
    titlarray.append(2)

for i in range(desert):
    titlarray.append(0)

print(titlarray)
random.shuffle(titlarray)  # перемешиваем id тайлов

map_tile = ['desert2.jpg', 'Montanas1.png', 'Montanas2.png']

# desert_n = 0
# montans_n = 1
# montans2_2 = 2

def chunks(lst, chunk_count):
    chunk_size = len(lst) // chunk_count
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]


titls = chunks(titlarray, int((WIDTH - 30) / 100))   # создаёт список кортеджей с id тайлов

print(titls)

unit_group = pygame.sprite.Group()
city_group = pygame.sprite.Group()
sprite_group = pygame.sprite.Group()
city_group.add((city1, city2, city3))

#### создаёт двумерный массив с id тайлов

map_arr = []

x = 0
y = 0
for row in titls:
    titls = str(row)
    titls = titls.replace('[', '')
    titls = titls.replace(']', '')
    titls = titls.replace(' ', '')
    titls = titls.replace(',', '')
    for i in titls:
        if i == '0':
            ds = Desert(x, y)
            sprite_group.add(ds)
            map_arr.append(ds)
            # x += 100
        if i == '1':
            mn1 = Montans1(x, y)
            sprite_group.add(mn1)
            map_arr.append(mn1)
            # x += 100
        if i == '2':
            mn2 = Montans2(x, y)
            sprite_group.add(mn2)
            map_arr.append(mn2)
        x += 100
    y += 100
    x = 0
    print(titls)