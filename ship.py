import pygame

class Ship:
    """Clase para gestionar la nave del heroe"""

    def __init__(self, ai_game):
        """Inicializa la nave y configura su posicion inicial"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Carga la imagen de la nave y obtiene su rect
        self.image = pygame.image.load('imges/hero_1.png')
        self.rect = self.image.get_rect()

        # Coloca inicialmente cada nave nueva en el centro de la parte inferior de la pantalla
        self.rect.midbottom = self.screen_rect.midbottom


    def blitme(self):
        """Dibuja la nave en su ubicacion actual"""
        self.screen.blit(self.image, self.rect)