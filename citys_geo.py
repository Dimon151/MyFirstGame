import random
import math

import time

from settings import WIDTH, HEIGHT, n_city

#### ГЕНЕРАЦИЯ МИРА

#### Города отступы от края карты
h = int((HEIGHT - 2) * 100)
w = int((WIDTH - 2) * 100)

#### Названия городов

min_dist = 400


def dist(x1, y1, x2, y2):
    return math.hypot((x1 - x2), (y1 - y2))


def citys_geo(n):
    def city_x():
        r_x = random.randint(1, (HEIGHT - 2)) * 100
        # print("r_x ", r_x)
        return r_x

    def city_y():
        r_y = random.randint(1, (WIDTH - 2)) * 100
        # print("r_y ", r_y)
        return r_y

    def chek_dist():
        list_coor = []
        while len(list_coor) != n:
            if len(list_coor) >= n:
                return list_coor
            for _ in range(n):
                list_coor.append((list([city_x(), city_y()])))
            for i in list_coor:
                if list_coor.count(i) != 1:
                    return None
                for ii in list_coor:
                    if i == ii:
                        continue
                    d = dist(i[0] + 50, i[1] + 50, ii[0] + 50, ii[1] + 50)
                    # print(d)
                    if d < min_dist:
                        return None
            return list_coor

    while True:
        list_coor = chek_dist()
        if list_coor is not None:
            return list_coor


if __name__ == "__main__":
    t_start = time.time()
    print(n_city)
    list_coor = citys_geo(n_city)
    print(list_coor)
    print((t_start - time.time()) * -1)
