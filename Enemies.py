from random import randrange
from math import atan2, pi

from Physics import gravity_work, collision_work
from Bullet import *


class HitBox(pygame.sprite.Sprite):
    def __init__(self, pos, width, height, health):
        super(HitBox, self).__init__(Globals.all_sprites)
        self.image = pygame.Surface([width, height])
        self.image.fill((255, 0, 0))
        self.rect = pygame.Rect(pos[0], pos[1] + 1, width, height)
        self.health = health
        Globals.enemies_hit_boxes.append(self)


class Shootar(HitBox):
    def __init__(self, pos, width, height, health):
        super(Shootar, self).__init__(pos, width, height, health)
        Globals.enemies.add(self)

        self.fire_delay = 0

    def update(self, character):
        try:
            assert not self.fire_delay
            target_pos = character.rect.center
            vector_x, vector_y = target_pos[0] - self.rect.x, target_pos[1] - self.rect.y
            angle = -(atan2(vector_x, vector_y) * 180 / pi) + randrange(-6, 6)
            bullet = Bullet(self.rect.center, angle, 'enemy', 20)
            self.fire_delay = Globals.FPS
        except AssertionError:
            self.fire_delay -= 1


class Messy(HitBox):
    def __init__(self, pos, width, height, health):
        super().__init__(pos, width, height, health)
        Globals.enemies.add(self)

        self.fire_delay = 0

    def update(self, character):
        try:
            assert not self.fire_delay
            target_pos = character.rect.center
            vector_x, vector_y = target_pos[0] - self.rect.x, target_pos[1] - self.rect.y
            angle = -(atan2(vector_x, vector_y) * 180 / pi) + randrange(-6, 6)
            bullet = Bullet(self.rect.center, angle + 15, 'enemy', 20)
            bullet = Bullet(self.rect.center, angle - 15, 'enemy', 20)
            self.fire_delay = Globals.FPS
        except AssertionError:
            self.fire_delay -= 1


class Bat(HitBox):
    def __init__(self, pos, width, height, health):
        super().__init__(pos, width, height, health)
        Globals.enemies.add(self)

        self.acceleration = randrange(1, 4) * 0.1
        self.speed_x = randrange(0, 1)
        self.max_speed_x = randrange(5, 7)
        self.max_speed_y = 0

    def update(self, *args):
        self.rect = self.rect.move(self.speed_x, 0)
        collision_work(self)
        try:
            assert self.speed_x == 0 or \
                   (self.speed_x >= self.max_speed_x or self.speed_x <= -self.max_speed_x)
            self.acceleration = -self.acceleration
        except AssertionError:
            pass
        self.speed_x += self.acceleration


class BatMessy(Bat):
    def __init__(self, pos, width, height, health):
        super().__init__(pos, width, height, health)
        self.fire_delay = 0

    def update(self, character):
        super(BatMessy, self).update(character)
        try:
            assert not self.fire_delay
            target_pos = character.rect.center
            vector_x, vector_y = target_pos[0] - self.rect.x, target_pos[1] - self.rect.y
            angle = -(atan2(vector_x, vector_y) * 180 / pi) + randrange(-6, 6)
            bullet = Bullet(self.rect.center, angle + 15, 'enemy', 20)
            bullet = Bullet(self.rect.center, angle - 15, 'enemy', 20)
            self.fire_delay = Globals.FPS
        except AssertionError:
            self.fire_delay -= 1


class Winger(HitBox):
    def __init__(self, pos, width, height, health):
        super().__init__(pos, width, height, health)
        Globals.enemies.add(self)

        self.acceleration = randrange(1, 4) * 0.1
        self.speed_y = randrange(0, 1)
        self.max_speed_y = randrange(5, 7)
        self.max_speed_x = 0

    def update(self, *args):
        self.rect = self.rect.move(0, self.speed_y)
        collision_work(self)
        try:
            assert self.speed_y == 0 or \
                   (self.speed_y >= self.max_speed_y or self.speed_y <= -self.max_speed_y)
            self.acceleration = -self.acceleration
        except AssertionError:
            pass
        self.speed_y += self.acceleration


class Toorar(HitBox):
    def __init__(self, pos, width, height, health):
        super().__init__(pos, width, height, health)
        Globals.enemies.add(self)

        self.fire_delay = 0
        self.angle = 0

    def update(self, *args):
        try:
            assert not self.fire_delay
            bullet = Bullet(self.rect.center, self.angle + randrange(-6, 6), 'enemy', 10)
            self.fire_delay = Globals.FPS * 0.1
            try:
                assert self.angle >= 360
                self.angle = 0
            except AssertionError:
                self.angle += 15
        except AssertionError:
            self.fire_delay -= 1


class BrokenToorar(HitBox):
    def __init__(self, pos, width, height, health):
        super().__init__(pos, width, height, health)
        Globals.enemies.add(self)

        self.fire_delay = 0

    def update(self, *args):
        try:
            assert not self.fire_delay
            bullet = Bullet(self.rect.center, randrange(0, 360), 'enemy', 25)
            self.fire_delay = Globals.FPS * 2
        except AssertionError:
            self.fire_delay -= 1
