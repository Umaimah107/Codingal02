import pygame
import random

surf_color = (0, 142, 204)
color = (0, 0, 0)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])

        self.image.fill(surf_color)

        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))

        self.rect = self.image.get_rect()

pygame.init()

screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Creating 2 Sprites")

all_sprites_list = pygame.sprite.Group()

sp1 = Sprite(color, 20, 30)
sp1.rect.x = random.randint(0, 480)
sp1.rect.y = random.randint(0, 370)

sp2 = Sprite(color, 40, 40)
sp2.rect.x = random.randint(0, 460)
sp2.rect.y = random.randint(0, 360)

all_sprites_list.add(sp1)
all_sprites_list.add(sp2)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites_list.update()

    screen.fill(surf_color)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
