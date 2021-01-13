import pygame
from pygame.math import Vector2
from Globals import Globals

BULLET_IMAGE = pygame.Surface((20, 11), pygame.SRCALPHA)
pygame.draw.polygon(BULLET_IMAGE, pygame.Color('aquamarine1'),
                    [(0, 0), (20, 5), (0, 11)])


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, angle, owner, damage):
        super().__init__(Globals.all_sprites)
        self.owner = owner
        self.damage = damage
        try:
            assert owner == 'player'
            Globals.player_bullets.add(self)
        except AssertionError:
            Globals.enemy_bullets.add(self)

        self.image = pygame.transform.rotate(BULLET_IMAGE, -(angle + 90))
        self.rect = self.image.get_rect(center=pos)
        offset = Vector2(0, 0).rotate(angle + 90)
        self.pos = Vector2(pos) + offset
        self.velocity = Vector2(1, 0).rotate(angle + 90) * (Globals.FPS / 9)

    def update(self):
        self.pos += self.velocity
        self.rect.center = self.pos
