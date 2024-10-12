"""Mòdul que conté la classe Obstacle."""
import os
import random
import pygame
import const

class Obstacle(pygame.sprite.Sprite):
    """Classe dels obstacles."""
    def __init__(self):
        super().__init__()
        # Asignar l'imatge de l'obstacle
        self.image = pygame.image.load(os.path.join(const.BASE_DIR, "assets/img/cimatarra.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (const.OBSTACLE_SIZE, const.OBSTACLE_SIZE))
        # Crear el rectangle de col·lisió
        self.rect = self.image.get_rect()
        # Asignar la posició i la velocitat incials aleatòriament
        self.rect.x = random.randint(0, const.WIDTH - const.OBSTACLE_SIZE)
        self.rect.y = random.randint(-100, -40)
        self.speed_y = random.randint(5, 10)

    def update(self):
        """Actualitza la posició de l'obstacle."""
        self.rect.y += self.speed_y
        # Asignar una velocitat i posició aleatòria
        if self.rect.top > const.HEIGHT:
            self.rect.x = random.randint(0, const.WIDTH - const.OBSTACLE_SIZE)
            self.rect.y = random.randint(-100, -40)
            self.speed_y = random.randint(5, 10)
