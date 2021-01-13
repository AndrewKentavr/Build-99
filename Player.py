from Physics import *


class Player(pygame.sprite.Sprite):
    def __init__(self, rect, health, damage):
        super().__init__(Globals.all_sprites)
        self.add(Globals.player_group)
        self.image = pygame.Surface([rect[2], rect[3]])
        self.image.fill((255, 0, 0))
        self.rect = pygame.Rect(rect)

        self.falling = False
        self.jumping = False
        self.speed_x = 0
        self.speed_y = 0
        self.max_speed_y = 10
        self.max_speed_x = 4
        self.god_mode_time = 0
        self.health = health
        self.damage = damage

    def update(self):
        self.rect = self.rect.move(self.speed_x, self.speed_y)
        gravity_work(self)
        collision_work(self)

        for hit_box in Globals.enemies_hit_boxes:
            try:
                assert pygame.sprite.collide_rect(hit_box, self) and not self.god_mode_time
                self.health -= 20
                self.check_death()
            except AssertionError:
                pass

        for bullet in Globals.enemy_bullets:
            try:
                assert pygame.sprite.collide_rect(bullet, self)
                Globals.enemy_bullets.remove(bullet)
                Globals.all_sprites.remove(bullet)
                assert not self.god_mode_time
                self.health -= bullet.damage
                self.check_death()
            except AssertionError:
                pass

        try:
            assert self.god_mode_time
            self.god_mode_time -= 1
        except AssertionError:
            pass

    def check_death(self):
        try:
            assert self.health > 0
            self.god_mode_time = Globals.FPS
        except AssertionError:
            self.rect.x = 50
            self.rect.y = 490
            self.health = 150
            self.falling = True
