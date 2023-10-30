class Settings:
    """Una clase para guardar toda la configuracion de Alien Invasion"""

    def __init__(self):
        """Inicializa la configuracion del juego"""
        # Configuracion de pantalla
        self.screen_width = 1200 # Ancho
        self.screen_height = 800 # Alto
        self.bg_color = (39, 39, 39) # Color RGB

        # Configuracion de la nave
        self.ship_speed = 1.5 # Valocidad inicial a la que se movera la nave (en 1,5 pixeles)