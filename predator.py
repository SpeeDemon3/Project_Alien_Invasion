import pygame

from alien import Alien
from pygame.sprite import Sprite

class Predator(Alien, Sprite):
    """Clase para representar un solo predator en la flota"""

    def __init__(self, ai_game):
        """Inicializa el alien y establece su posicion inicial"""
        super().__init__(ai_game) # Llama al constructor de Alien
        super().__init__() # Llama al constructor de Sprite

        # Carga la imagen del predator
        self.image = pygame.image.load('images/bad_2.bmp')
