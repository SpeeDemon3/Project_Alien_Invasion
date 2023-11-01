import sys

import pygame

from Proyectos.Alien_Invasion.settings import Settings
from Proyectos.Alien_Invasion.ship import Ship
from bullet import Bullet

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

        # Creamos un grupo de balas para dibujarlas en la pantalla y actualizar la posicion de cada bala
        self.bullets = pygame.sprite.Group()


    def run_game(self):
        """Inicia le bucle principal para el juego"""
        while True:
            # Busca eventos de teclado y raton
            self._check_events()

            # Comprueba si hay eventos y actualiza la posicion de la nave en la pantalla
            self.ship.update()

            # Llama a bullet.update() para cada bala colocada en el grupo bullets
            self.bullets.update()

            # Se deshace de las balas que han desaparecido para que no consuman recursos
            for bullet in self.bullets.copy():
                # Comprobamos si el valor bottom del react tiene un valor de 0, lo que indica que la bala a superado el borde superior de la pantalla
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)

            # Redibuja la pantalla en cada paso por el bucle
            self._update_screen()

            # Hace visible la ultima pantalla dibujada
            pygame.display.flip()


    def _update_screen(self):
        """Actualiza las imagenes en la pantalla y cambia a la pantalla nueva"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()  # Llamamos al metodo blitme() para que la nave aparezca encima del fondo

        # El metodo sprites() devuelve una lista de todos los sprites del grupo bullets
        for bullet in self.bullets.sprites():
            bullet.draw_bullet() # Utilizamos el metodo draw_bullet() para pintarlas en pantalla



    def _check_events(self):
        """Responde a pulsaciones de teclado y eventos de raton"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Para finalizar cuando se cierre la ventana
                sys.exit()

            elif event.type == pygame.KEYDOWN: # Si el evento es igual a pulsar una tecla
                self.check_keydown_events(event)

            elif event.type == pygame.KEYUP: # Si el evento es igual a dejar de pulsar una tecla
                self._check_keyup_events(event)

    def check_keydown_events(self, event):
        """Responde a pulsaciones de teclado"""
        if event.key == pygame.K_RIGHT:  # Comprobamos si la tecla pulsada es la derecha
            # Mueve la nave a la derecha
            self.ship.moving_right = True  # Si el jugador pulsa la tecla cambiamos el valor de la bandera a True

        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True  # Si el jugador pulsa la tecla cambiamos el valor de la bandera a True

        elif event.key == pygame.K_q: # Al pulsar la tecla Q cerramos el programa
            sys.exit()

        elif event.key == pygame.K_SPACE: # Al pulsar la tecla espaciadora llamamos al metodo para disparar
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Responde a la liberacion de teclas"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False  # Si el jugador deja de pulsar la tecla cambiamos el valor de la bandera a False

        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Crea una bala nueva y la añade al grupo de balas"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)


if __name__ == '__main__':
    #Hace una instance del juego y lo ejecuta
    ai = AlienInvasion()
    ai.run_game()