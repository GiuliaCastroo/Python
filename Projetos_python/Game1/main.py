import os
import random
import math 
import pygame
from os import listdir
from os.path import isfile, join
pygame.init()

pygame.display.set_caption("Platformer")

WIDTH, HEIGHT = 1000, 800
FPS = 60
PLAYER_VEL = 5

window = pygame.display.set_mode((WIDTH, HEIGHT))


def flip(sprites):
    return [pygame.transform.flip(sprite, True, False) for sprite in sprites]


def load_sprite_sheets(dir1, dir2, width, height, direction=False):
    path = join(dir1, dir2)
    images = [f for f in listdir(path) if isfile(join(path, f))]

    all_sprites = {}

    for image in images:
        sprite_sheet = pygame.image.load(join(path, image)).convert_alpha()

        sprites = []
        for i in range(sprite_sheet.get_width() // width):
            surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
            rect = pygame.Rect(i * width, 0, width, height)
            surface.blit(sprite_sheet, (0, 0), rect)
            sprites.append(pygame.transform.scale2x(surface))

        if direction:
            all_sprites[image.replace(".png", "") + "_right"] = sprites
            all_sprites[image.replace(".png", "") + "_left"] = flip(sprites)
        else:
            all_sprites[image.replace(".png", "")] = sprites

    return all_sprites


def get_block(size):
    path = join("Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(96, 0, size, size)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)


class Player(pygame.sprite.Sprite):
    COLOR = (255, 0, 0)
    GRAVITY = 1
    SPRITES = load_sprite_sheets("MainCharacters", "PinkMan", 32, 32, True)
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None
        self.direction = "left"
        self.animation_count = 0
        self.fall_count = 0
        self.jump_count = 0
        self.hit = False
        self.hit_count = 0

    def jump(self):
        self.y_vel = -self.GRAVITY * 8
        self.animation_count = 0
        self.jump_count += 1
        if self.jump_count == 1:
            self.fall_count = 0

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def make_hit(self):
        self.hit = True

    def move_left(self, vel):
        self.x_vel = -vel
        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0

    def move_right(self, vel):
        self.x_vel = vel
        if self.direction != "right":
            self.direction = "right"
            self.animation_count = 0

    def loop(self, fps):
        self.y_vel += min(1, (self.fall_count / fps) * self.GRAVITY)
        self.move(self.x_vel, self.y_vel)

        if self.hit:
            self.hit_count += 1
        if self.hit_count > fps * 2:
            self.hit = False
            self.hit_count = 0

        self.fall_count += 1
        self.update_sprite()

    def landed(self):
        self.fall_count = 0
        self.y_vel = 0
        self.jump_count = 0

    def hit_head(self):
        self.count = 0
        self.y_vel *= -1

    def update_sprite(self):
        sprite_sheet = "idle"
        if self.hit:
            sprite_sheet = "hit"
        elif self.y_vel < 0:
            if self.jump_count == 1:
                sprite_sheet = "jump"
            elif self.jump_count == 2:
                sprite_sheet = "double_jump"
        elif self.y_vel > self.GRAVITY * 2:
            sprite_sheet = "fall"
        elif self.x_vel != 0:
            sprite_sheet = "run"

        sprite_sheet_name = sprite_sheet + "_" + self.direction
        sprites = self.SPRITES[sprite_sheet_name]
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.sprite = sprites[sprite_index]
        self.animation_count += 1
        self.update()

    def update(self):
        self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.sprite)

    def draw(self, win, offset_x):
        win.blit(self.sprite, (self.rect.x - offset_x, self.rect.y))


class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, name=None):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.width = width
        self.height = height
        self.name = name

    def draw(self, win, offset_x):
        win.blit(self.image, (self.rect.x - offset_x, self.rect.y))


class Block(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = get_block(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)


class Fire(Object):
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "fire")
        self.fire = load_sprite_sheets("Traps", "Fire", width, height)
        self.image = self.fire["off"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "off"

    def on(self):
        self.animation_name = "on"

    def off(self):
        self.animation_name = "off"

    def loop(self):
        sprites = self.fire[self.animation_name]
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0


def get_background(name):
    image = pygame.image.load(join("Background", name))
    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height + 1):
            pos = (i * width, j * height)
            tiles.append(pos)

    return tiles, image


def draw(window, background, bg_image, player, objects, offset_x):
    for tile in background:
        window.blit(bg_image, tile)

    for obj in objects:
        obj.draw(window, offset_x)

    player.draw(window, offset_x)

    pygame.display.update()


def handle_vertical_collision(player, objects, dy):
    collided_objects = []
    for obj in objects:
        if pygame.sprite.collide_mask(player, obj):
            if dy > 0:
                player.rect.bottom = obj.rect.top
                player.landed()
            elif dy < 0:
                player.rect.top = obj.rect.bottom
                player.hit_head()

            collided_objects.append(obj)

    return collided_objects
class MovingPlatform(Object):
    def __init__(self, x, y, width, height, move_range=100, speed=2):
        super().__init__(x, y, width, height, "moving_platform")
        self.image = pygame.Surface((width, height))
        self.image.fill((100, 100, 255))  # Azul claro
        self.mask = pygame.mask.from_surface(self.image)
        self.original_x = x
        self.move_range = move_range
        self.speed = speed
        self.direction = 1  # 1 para direita, -1 para esquerda

    def loop(self):
        self.rect.x += self.speed * self.direction
        
        # Inverte a direção se atingir os limites
        if self.rect.x > self.original_x + self.move_range:
            self.direction = -1
        elif self.rect.x < self.original_x:
            self.direction = 1

class Wall(Object):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "wall")
        self.image = pygame.Surface((width, height))
        self.image.fill((150, 75, 0))  # Marrom para parede
        self.mask = pygame.mask.from_surface(self.image)

class BouncePad(Object):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "bounce_pad")
        self.image = pygame.Surface((width, height))
        self.image.fill((0, 255, 0))  # Verde para trampolim
        self.mask = pygame.mask.from_surface(self.image)
        self.bounce_power = 15


def collide(player, objects, dx):
    player.move(dx, 0)
    player.update()
    collided_object = None
    for obj in objects:
        if pygame.sprite.collide_mask(player, obj):
            collided_object = obj
            break

    player.move(-dx, 0)
    player.update()
    return collided_object


def handle_move(player, objects):
    keys = pygame.key.get_pressed()
    player.x_vel = 0
    collide_left = collide(player, objects, -PLAYER_VEL * 2)
    collide_right = collide(player, objects, PLAYER_VEL * 2)

    # Movimento horizontal
    if keys[pygame.K_LEFT] and not collide_left:
        player.move_left(PLAYER_VEL)
    if keys[pygame.K_RIGHT] and not collide_right:
        player.move_right(PLAYER_VEL)

    # Verifica colisões verticais
    vertical_collide = handle_vertical_collision(player, objects, player.y_vel)
    to_check = [collide_left, collide_right, *vertical_collide]

    for obj in to_check:
        if obj and obj.name == "fire":
            player.make_hit()
        elif obj and obj.name == "bounce_pad" and player.y_vel > 0:
            player.y_vel = -obj.bounce_power  # Impulso para cima

    # Permite escalar paredes se estiver pressionando para cima
    wall_collision = collide(player, [obj for obj in objects if obj.name == "wall"], 0)
    if wall_collision and keys[pygame.K_UP]:
        player.y_vel = -PLAYER_VEL * 0.8  # Escala mais devagar que o pulo normal



def main(window):
    clock = pygame.time.Clock()
    background, bg_image = get_background("Pink.png")

    block_size = 96
    player = Player(100, 100, 50, 50)
    
    # Configuração do nível (mantendo seu código original)
    floor = [Block(i * block_size, HEIGHT - block_size, block_size)
             for i in range(-WIDTH // block_size, (WIDTH * 3) // block_size)]
    
    # Plataformas básicas (seu código original)
    platforms = [
        Block(0, HEIGHT - block_size * 2, block_size),
        Block(block_size * 3, HEIGHT - block_size * 4, block_size),
        Block(block_size * 6, HEIGHT - block_size * 3, block_size),
        Block(block_size * 9, HEIGHT - block_size * 5, block_size),
        Block(block_size * 12, HEIGHT - block_size * 2, block_size),
    ]
    
    # Obstáculos de fogo (seu código original)
    fires = [
        Fire(block_size * 2, HEIGHT - block_size - 64, 16, 32),
        Fire(block_size * 5, HEIGHT - block_size * 3 - 64, 16, 32),
        Fire(block_size * 8, HEIGHT - block_size * 2 - 64, 16, 32),
    ]
    for fire in fires:
        fire.on()
    
    # Novos elementos de parkour (seu código original)
    moving_platforms = [
        MovingPlatform(block_size * 4, HEIGHT - block_size * 3, block_size, 20, move_range=150),
        MovingPlatform(block_size * 7, HEIGHT - block_size * 5, block_size, 20, move_range=100, speed=3),
    ]
    
    walls = [
        Wall(block_size * 10, HEIGHT - block_size * 6, 30, block_size * 5),
        Wall(block_size * 15, HEIGHT - block_size * 4, 30, block_size * 3),
    ]
    
    bounce_pads = [
        BouncePad(block_size * 11, HEIGHT - block_size - 20, 60, 20),
        BouncePad(block_size * 14, HEIGHT - block_size * 3 - 20, 60, 20),
    ]
    
    # Combine todos os objetos (seu código original)
    objects = [
        *floor,
        *platforms,
        *fires,
        *moving_platforms,
        *walls,
        *bounce_pads,
        
        # Plataforma final como objetivo (agora com nome "finish")
        Block(block_size * 18, HEIGHT - block_size * 7, block_size),
    ]
    objects[-1].name = "finish"  # Identifica a última plataforma como objetivo

    offset_x = 0
    scroll_area_width = 200
    game_won = False
    font = pygame.font.SysFont(None, 72)  # Fonte para mensagem de vitória

    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == pygame.KEYDOWN and not game_won:  # Só permite pular se não tiver vencido
                if event.key == pygame.K_SPACE and player.jump_count < 2:
                    player.jump()

        if not game_won:
            player.loop(FPS)
            
            # Atualiza todos os objetos que possuem animação (seu código original)
            for obj in objects:
                if hasattr(obj, 'loop'):
                    obj.loop()
                    
            handle_move(player, objects)

            # Verifica se alcançou a plataforma final (nova verificação)
            if pygame.sprite.collide_mask(player, objects[-1]):  # Verifica colisão com a última plataforma
                game_won = True

        draw(window, background, bg_image, player, objects, offset_x)

        # Mostra mensagem de vitória (novo código)
        if game_won:
            # Cria overlay semi-transparente
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 180))
            window.blit(overlay, (0, 0))
            
            # Renderiza texto
            text = font.render('VITÓRIA!', True, (255, 215, 0))  # Texto dourado
            text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//2))
            window.blit(text, text_rect)
            
            pygame.display.update()
            pygame.time.wait(3000)  # Espera 3 segundos
            run = False  # Encerra o jogo

        # Scroll da tela (seu código original, só funciona se não tiver vencido)
        if not game_won and ((player.rect.right - offset_x >= WIDTH - scroll_area_width) and player.x_vel > 0) or (
                (player.rect.left - offset_x <= scroll_area_width) and player.x_vel < 0):
            offset_x += player.x_vel
    pygame.quit()
    quit()
    
if __name__ == "__main__":
    main(window)





