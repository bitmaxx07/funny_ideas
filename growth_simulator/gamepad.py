import pygame
import random


from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Test_game")
font = pygame.font.Font("freesansbold.ttf", 24)


ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
        self.life = 1000
        self.score = 0

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -3)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 3)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-3, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(3, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((20, 10))
        self.surf.fill((255, 255, 0))
        self.rect = self.surf.get_rect(
            center=(random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                    random.randint(0, SCREEN_HEIGHT), )
        )
        self.speed = random.randint(5, 20)

    def update(self):
        self.rect.move_ip(-self.speed / 8, 0)
        if self.rect.right < 0:
            self.kill()


# set game running

player = Player()

enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

running = True
while running:
    msg = "Life: " + str(player.life)
    text = font.render(msg, True, (0, 255, 0), (0, 0, 128))
    text_rect = text.get_rect()
    text_rect.center = (80, 40)

    sc = "Score: " + str(player.score)
    sc_text = font.render(sc, True, (0, 255, 0), (0, 0, 128))
    sc_rect = sc_text.get_rect()
    sc_rect.center = (80, 100)

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        elif event.type == QUIT:
            running = False

        elif event.type == ADDENEMY:
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
            player.score += 1

    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)
    enemies.update()

    screen.fill((0, 0, 0))
    screen.blit(text, text_rect)
    screen.blit(sc_text, sc_rect)
    # screen.blit(player.surf, player.rect)
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    if pygame.sprite.spritecollideany(player, enemies):
        player.life -= 1

    if player.life == 0:
        player.kill()
        running = False
        print("Your final score is: " + str(player.score))

    pygame.display.flip()
