import sys

import pygame

from Proyectos.Alien_Invasion.settings import Settings
from Proyectos.Alien_Invasion.ship import Ship

class AlienInvasion:
    """Clase general para gestionar los recursos y el comportamiento del juego"""

    def __init__(self):
        """Inicializa el juego y crea recursos"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((
            self.settings.screen_width, self.settings.screen_height
        ))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self) # Creamos una nave de la clase Ship


    def run_game(self):
        """Inicia le bucle principal para el juego"""
        while True:
            # Busca eventos de teclado y raton
            self._check_events()

            # Redibuja la pantalla en cada paso por el bucle
            self._update_screen()

            # Hace visible la ultima pantalla dibujada
            pygame.display.flip()

    def _check_events(self):
        """Responde a pulsaciones de teclas y eventos de raton"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Para finalizar cuando se cierre la ventana
                sys.exit()

    def _update_screen(self):
        """Actualiza las imagenes en la pantalla y cambia a la pantalla nueva"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()  # Llamamos al metodo blitme() para que la nave aparezca encima del fondo

if __name__ == '__main__':
    #Hace una instance del juego y lo ejecuta
    ai = AlienInvasion()
    ai.run_game()