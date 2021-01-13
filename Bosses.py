from random import randrange

from Enemies import HitBox
from Physics import collision_work, gravity_work
from Bullet import *


class Ricobulb(HitBox):
    def __init__(self, pos, width, height, health):
        super().__init__(pos, width, height, health)
        Globals.enemies.add(self)

        self.fire_delay = Globals.FPS * 3
        self.angle = 45
        self.have_ricochet = True

        self.speed_x = 4
        self.speed_y = 4
        self.max_speed_x = self.speed_x
        self.max_speed_y = self.speed_y

    def update(self, character):
        self.rect = self.rect.move(self.speed_x, self.speed_y)
        collision_work(self)

        try:
            assert not self.fire_delay
            self.angle = 45 + randrange(0, 10)
            for i in range(6):
                bullet = Bullet(self.rect.center, self.angle, 'enemy', 50)
                try:
                    assert i != 2
                    self.angle += 45
                except AssertionError:
                    self.angle += 90
            self.fire_delay = Globals.FPS * randrange(1, 7)
        except AssertionError:
            self.fire_delay -= 1
