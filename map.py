import random

from Tiles import *
from Enemies import *


class MapGenerator:
    def __init__(self, base):
        self.map = base
        self.len_map = len(base)
        self.entrance_coordinates = (0, 17)  # это координаты входной двери
        self.exit_coordinates = 0
        self.platform_coordinates = []  # тут координаты платформ
        self.random_items_coordinates = []  # тут координаты для рандомных объектов
        self.generate_door_exit()
        self.platform_objects()

        # self.random_decor_items()

    # return_map - проектирует на map_1 координаты

    def return_map(self):
        self.map[self.exit_coordinates[0]][self.exit_coordinates[1]] = 3
        self.map[self.exit_coordinates[0] + 1][self.exit_coordinates[1]] = 23
        self.map[self.exit_coordinates[0]][self.exit_coordinates[1] + 1] = 23
        self.map[self.exit_coordinates[0] + 1][self.exit_coordinates[1] + 1] = 23
        self.map[self.exit_coordinates[0] + 2][self.exit_coordinates[1] + 1] = 5
        self.map[self.exit_coordinates[0] + 2][self.exit_coordinates[1]] = 5
        self.map[self.exit_coordinates[0] + 2][self.exit_coordinates[1] - 1] = 5

        for i in range(len(self.platform_coordinates)):
            for_this = self.platform_coordinates[i]
            self.map[for_this[0]][for_this[1]] = 5

        '''
        for i in range(len(self.random_items_coordinates)):
            for_this = self.random_items_coordinates[i]
            self.map[for_this[0]][for_this[1]] = 4
        '''
        return self.map

    # generate_door_exit - генерирует координаты для выхода

    def generate_door_exit(self):
        horizontal_branch = random.randint(1, self.len_map - 3)
        self.exit_coordinates = (horizontal_branch, -2)

        # random_decor_items - генерирует рандомные объекты, которые потом будут просто декорацией на фоне
        '''
    def random_decor_items(self):
        number_of_objects = random.randint(1, 4)
        for i in range(number_of_objects):

            horizontal_branch = random.randint(1, self.len_map - 2)
            vertical_branch = random.randint(1, self.len_map - 2)

            while map_1[horizontal_branch][vertical_branch] != 0:
                horizontal_branch = random.randint(1, self.len_map - 2)
                vertical_branch = random.randint(1, self.len_map - 2)

            self.random_items_coordinates.append((horizontal_branch, vertical_branch))
        '''

    def platform_objects(self):  # функция для платформ, пока платформы статичны, но это пока
        # x = random.randint(3, 16)
        y = 16  # (1)
        x = 7
        if x <= 9:
            self.plus_platform(4, x, y, 9)

            x = random.randint(1, 10)
            y = random.randint(13, 14)  # (2)

            if x <= 5:
                self.plus_platform(3, x, y, 5)

                x = random.randint(3, 8)
                y = 11  # (3) ----- ЗЕЛЁНАЯ ВЕТКА

                self.plus_platform(2, x, y, 9)

                number = random.randint(0, 1)
                if number == 0:
                    x = random.randint(1, 6)
                    y = 8  # (4)

                    self.plus_platform(3, x, y, 6)

                    x = random.randint(2, 4)
                    y = 5  # (5)
                    self.plus_platform(1, x, y, 4)

                    x = 5
                    y = random.randint(2, 3)  # (6)
                    self.plus_platform(4, x, y, 15)

                    x = 9
                    y = 3
                    self.plus_platform(1, x, y, 15)

                    y = random.randint(2, 3)  # (7)
                    if y == 2:
                        x = 15
                        self.plus_platform(2, x, y, 17)
                    else:
                        x = random.randint(13, 16)
                        self.plus_platform(2, x, y, 15)

                    x = random.randint(10, 13)
                    y = random.randint(6, 8)  # (8)
                    self.plus_platform(3, x, y, 13)

                    x = random.randint(15, 16)  # (10)
                    y = random.randint(8, 11)
                    self.plus_platform(1, x, y, 16)

                    x = random.randint(13, 15)
                    y = random.randint(14, 15)  # (9)
                    self.plus_platform(3, x, y, 16)

                else:
                    x = random.randint(8, 9)
                    y = random.randint(8, 9)  # (3) ----- ФИОЛЕТОВАЯ ВЕТКА
                    self.plus_platform(1, x, y, 9)

                    x = random.randint(9, 10)
                    y = random.randint(8, 9)  # (4)
                    self.plus_platform(2, x, y, 10)

                    x = random.randint(4, 7)
                    y = 6  # (5)
                    self.plus_platform(1, x, y, 7)

                    x = random.randint(0, 3)
                    y = random.randint(3, 4)  # (6)
                    self.plus_platform(3, x, y, 3)

                    x = random.randint(7, 15)
                    y = random.randint(3, 4)  # (7)
                    while x == 7 and y == 4:
                        x = random.randint(7, 15)

                    self.plus_platform(6, x, y, 20)

                    number = random.randint(0, 1)  # (8) - 1
                    if number == 0:
                        x = 14
                        y = 10
                        self.plus_platform(1, x, y, 16)

                    number = random.randint(0, 1)  # (8) - 2
                    if number == 0:
                        x = 13
                        y = 12
                        self.plus_platform(1, x, y, 16)

                    number = random.randint(0, 1)  # (8) - 3
                    if number == 0:
                        x = 15
                        y = 12
                        self.plus_platform(1, x, y, 16)

                    number = random.randint(0, 1)  # (8) - 4
                    if number == 0:
                        x = 16
                        y = 12
                        self.plus_platform(1, x, y, 16)

                    x = random.randint(14, 16)
                    y = 15  # (9)
                    self.plus_platform(2, x, y, 17)

                    x = random.randint(12, 14)
                    y = 16  # (10)
                    self.plus_platform(2, x, y, 17)

                    number = random.randint(0, 1)  # (?)
                    if number == 0:
                        x = random.randint(1, 3)
                        y = random.randint(7, 10)

                        len_platform = random.randint(1, 2)

                        self.plus_platform(len_platform, x, y, 3)
            else:
                self.plus_platform(3, x, y, 10)  # (2) ЖЕЛТАЯ ВЕТКА

                x = random.randint(11, 13)
                y = random.randint(12, 13)  # (3)
                self.plus_platform(2, x, y, 13)

                x = 14  # (4)
                y = 10
                self.plus_platform(4, x, y, 50)

                x = 17
                y = 8
                self.plus_platform_vert(2, x, y, 12)

                number = random.randint(1, 3)
                if number == 1:
                    x = 15
                    y = 8
                    self.plus_platform(1, x, y, 20)
                elif number == 2:
                    x = 15
                    y = 9
                    self.plus_platform(1, x, y, 20)
                else:
                    x = 17
                    y = 7
                    self.plus_platform(1, x, y, 20)

                x = random.randint(6, 10)  # (5)
                y = random.randint(8, 9)
                self.plus_platform(4, x, y, 50)

                number = random.randint(1, 8)  # (6)
                if number > 6:
                    x = random.randint(13, 14)
                    y = 5
                    self.plus_platform(1, x, y, 50)
                else:
                    x = random.randint(13, 14)
                    y = random.randint(4, 6)
                    self.plus_platform(1, x, y, 50)

                x = random.randint(15, 17)  # (7)
                y = random.randint(2, 3)
                self.plus_platform(2, x, y, 50)

                x = random.randint(0, 5)  # (8)
                y = random.randint(5, 6)
                self.plus_platform(5, x, y, 50)

                x = random.randint(3, 5)  # (9)
                y = 1
                self.plus_platform_vert(3, x, y, 50)

                x = random.randint(0, 2)  # (10)
                y = random.randint(9, 12)
                self.plus_platform_vert(3, x, y, 50)
        else:
            self.plus_platform(2, x, y, 16)

    def plus_platform(self, number, x, y, restrictions):
        for i in range(number):
            if x <= restrictions // 2:
                self.platform_coordinates.append((y, x + i))
            else:
                self.platform_coordinates.append((y, x - i))

    def plus_platform_vert(self, number, x, y, restrictions):
        for i in range(number):
            if x <= restrictions // 2:
                self.platform_coordinates.append((y + i, x))
            else:
                self.platform_coordinates.append((y + i, x))


# тут очень плохо выводится карта

def generate(level):
    import random
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == 1 or level[y][x] == 5:
                random_photo = random.randint(1, 5)
                Part((x * 30, y * 30), f'wall_{random_photo}.png')
            if level[y][x] == 0:
                BackGroundPart((x * 30, y * 30), f'wall_{randrange(1, 4)}_dark.png')
            if 3 >= level[y][x] >= 2:
                for i in range(4):
                    for j in range(4):
                        BackGroundPart(((x + j) * 30, (y + i) * 30),
                                       f'wall_{randrange(1, 4)}_dark.png')
            if level[y][x] == 3:
                Door((x * 30, y * 30), 'door.png', True)
            if level[y][x] == 2:
                Door((x * 30, y * 30), 'door.png', False)

    enemy_count = randrange(2, 7)
    enemy_distance = 120
    flag = True
    while flag:
        for y in range(len(level)):
            for x in range(len(level[y])):
                if level[y][x] == 0 and enemy_distance == 0:
                    if not flag:
                        break
                    enemy_spawn_chance = randrange(1, 10)
                    if enemy_spawn_chance == 9:
                        enemy_distance = 7
                        enemy_id = randrange(0, 6)
                        if enemy_id == 0:
                            Shootar((x * 30, y * 30), 30, 30, 100)
                        elif enemy_id == 1:
                            Messy((x * 30, y * 30), 30, 30, 100)
                        elif enemy_id == 2:
                            Bat((x * 30, y * 30), 30, 30, 300)
                        elif enemy_id == 3:
                            BatMessy((x * 30, y * 30), 30, 30, 250)
                        elif enemy_id == 4:
                            Winger((x * 30, y * 30), 30, 30, 400)
                        elif enemy_id == 5:
                            Toorar((x * 30, y * 30), 30, 30, 400)
                        else:
                            BrokenToorar((x * 30, y * 30), 30, 30, 400)
                        enemy_count -= 1
                        if not enemy_count:
                            flag = False
                elif enemy_distance:
                    enemy_distance -= 1
