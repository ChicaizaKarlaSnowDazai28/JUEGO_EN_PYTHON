import pygame

class GameConfig:
    def __init__(self):
        self.WIDTH = 600
        self.HEIGHT = 400
        self.BLOCK_SIZE = 20

        self.BLACK = (0, 0, 0)
        self.NAVY_BLUE = (0, 0, 128)
        self.RED = (255, 0, 0)
        self.WHITE = (255, 255, 255)

        pygame.init()
        pygame.mixer.init()

        self.sonido_comida = pygame.mixer.Sound("comida.wav")
        self.sonido_perder = pygame.mixer.Sound("perder.wav")

        pygame.mixer.music.load("musica_fondo.mp3")
        pygame.mixer.music.set_volume(0.3)

        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Juego de la Culebrita")

        self.fondo_img = pygame.image.load("fondo.jpg")
        self.fondo_img = pygame.transform.scale(self.fondo_img, (self.WIDTH, self.HEIGHT))

        self.font_small = pygame.font.SysFont(None, 30)
        self.font_big = pygame.font.SysFont(None, 60)