"""Mòdul que conté la classe Taronja."""
import os
import random
import pygame
import const

class Taronja(pygame.sprite.Sprite):
    """Classe de les taronges."""
    def __init__(self):
        super().__init__()
        # Asignar l'imatge de la taronja
        self.image = pygame.image.load(os.path.join(const.BASE_DIR, "assets/img/taronja.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (const.TARONJA_SIZE, const.TARONJA_SIZE))
        # Crear el rectangle de col·lisió
        self.rect = self.image.get_rect()
        # Asignar la posició i la velocitat incials aleatòriament
        self.rect.x = random.randint(0, const.WIDTH - const.TARONJA_SIZE)
        self.rect.y = random.randint(-100, -40)
        self.speed_y = random.randint(3, 7)

    def update(self):
        """Actualitza la posició de la taronja."""
        self.rect.y += self.speed_y
        # Asignar una velocitat i posició aleatòria
        if self.rect.top > const.HEIGHT:
            self.rect.x = random.randint(0, const.WIDTH - const.TARONJA_SIZE)
            self.rect.y = random.randint(-100, -40)
            self.speed_y = random.randint(3, 7)
