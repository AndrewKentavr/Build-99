from map import MapGenerator, generate
from Player import Player
from Weapons import *
from Tiles import *
from Graphics import *
from Bosses import *

pygame.init()
pygame.display.set_caption("build 0")
screen = pygame.display.set_mode(Globals.SIZE)
clock = pygame.time.Clock()


def generate_level():
    Wall((-10, 0))
    Wall((Globals.WIDTH + 1, 0))
    level = MapGenerator(Globals.level_base).return_map()
    generate(level)
    Globals.level_base = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [2, 23, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [23, 23, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]


def main_function():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                Globals.game_cycle = False
            if event.type == pygame.MOUSEBUTTONDOWN and not Globals.pause:
                if event.button == 1 and len(Globals.player_bullets) < 6:
                    Bullet(bow.rect.center, bow.angle, 'player', None)

        if pygame.key.get_pressed():
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                Globals.pause = not Globals.pause
                continue
            if keys[pygame.K_a]:
                player.speed_x = -player.max_speed_x
            elif keys[pygame.K_d]:
                player.speed_x = player.max_speed_x
            if keys[pygame.K_SPACE] and not player.jumping and not player.falling:
                player.jumping = True

        if not Globals.pause:
            player.update()
            Globals.enemies.update(player)
            bow.update(player.rect.center)

            Globals.player_bullets.update()
            Globals.enemy_bullets.update()

            Globals.health_bars.update(player)

            for bullet in Globals.player_bullets:
                for enemy in Globals.enemies_hit_boxes:
                    if pygame.sprite.collide_rect(bullet, enemy):
                        enemy.health -= player.damage
                        Globals.player_bullets.remove(bullet)
                        Globals.all_sprites.remove(bullet)
                        if enemy.health <= 0:
                            Globals.all_sprites.remove(enemy)
                            Globals.enemies.remove(enemy)
                            Globals.enemies_hit_boxes.pop(Globals.enemies_hit_boxes.index(enemy))

                if pygame.sprite.spritecollideany(bullet, Globals.tiles):
                    Globals.player_bullets.remove(bullet)
                    Globals.all_sprites.remove(bullet)

            for bullet in Globals.enemy_bullets:
                if pygame.sprite.spritecollideany(bullet, Globals.tiles):
                    Globals.all_sprites.remove(bullet)
                    Globals.enemy_bullets.remove(bullet)

            player.speed_x = 0
        screen.fill((0, 0, 0))
        clock.tick(Globals.FPS)
        Globals.all_sprites.draw(screen)
        Globals.health_bars.draw(screen)
        Globals.player_group.draw(screen)
        pygame.display.flip()

        if pygame.sprite.spritecollideany(player, Globals.level_door) and not Globals.enemies_hit_boxes:
            for sprite in Globals.all_sprites:
                if sprite == player:
                    player.rect.x, player.rect.y = 50, 540
                elif sprite == bow:
                    bow.update(player.rect.center)
                else:
                    Globals.all_sprites.remove(sprite)
            Globals.tiles = pygame.sprite.Group()
            Globals.level_door = pygame.sprite.Group()
            Globals.starter_door = pygame.sprite.Group()
            Globals.player_bullets = pygame.sprite.Group()
            Globals.enemy_bullets = pygame.sprite.Group()
            running = False


player = Player((50, 540, 30, 30), 200, 35)
bow = Bow((player.rect.x + 30, player.rect.y + 30, 20, 20), 35)

HealthBar(player.health, 10)

while Globals.game_cycle:
    generate_level()
    main_function()

pygame.quit()
