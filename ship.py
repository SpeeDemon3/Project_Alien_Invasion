import pygame

class Ship:
    """Clase para gestionar la nave del heroe"""

    def __init__(self, ai_game):
        """Inicializa la nave y configura su posicion inicial"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Carga la imagen de la nave y obtiene su rect
        self.image = pygame.image.load('images/hero_1.bmp')
        self.rect = self.image.get_rect()

        # Coloca inicialmente cada nave nueva en el centro de la parte inferior de la pantalla
        self.rect.midbottom = self.screen_rect.midbottom

        # Guarda un valor decimal para la posicion horizontal de la nave
        self.x = float(self.rect.x)

        # Bandera de movimiento
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Actualiza la posicion de la nave en funcion de la bandera de movimiento"""
        # Actualiza el valor x de la nave, no el rect
        # Si self.moving_right es True y el borde derecho de la nave no alcanza el borde derecho de la pantalla
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed # Aumentamos el valor del eje X

        # Si self.moving_left es True y el borde izquierdo de la nave no alcanza el borde izquierdo de la pantalla
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed # Disminuimos el valor del eje X

        # Actualiza el objeto rect de self.x
        self.rect.x = self.x


    def blitme(self):
        """Dibuja la nave en su ubicacion actual"""
        self.screen.blit(self.image, self.rect)