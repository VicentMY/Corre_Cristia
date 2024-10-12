"""Mòdul que conté la classe Jugador."""
import os
import pygame
import const

class Jugador(pygame.sprite.Sprite):
    """Classe del jugador."""
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join(const.BASE_DIR, "assets/img/cristiano.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (const.JUGADOR_SIZE, const.JUGADOR_SIZE))
        self.rect = self.image.get_rect()
        self.rect.center = (const.WIDTH // 2, const.HEIGHT - const.JUGADOR_SIZE)
        self.speed_x = 0

    def update(self):
        """Actualitza la posició del jugador."""
        self.speed_x = 0
        # KeyListener per al moviment del jugador
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.speed_x = -5
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.speed_x = 5
        self.rect.x += self.speed_x

        # Llimitar el moviment del jugador per a que no isca de la pantalla
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > const.WIDTH:
            self.rect.right = const.WIDTH
