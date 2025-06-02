import pygame
import random

class Food:
    def __init__(self, block_size, width, height, image=None):
        self.block_size = block_size
        self.width = width
        self.height = height
        self.image = image
        self.position = self._random_position()

    def _random_position(self):
        x = random.randrange(0, self.width - self.block_size, self.block_size)
        y = random.randrange(0, self.height - self.block_size, self.block_size)
        return (x, y)

    def respawn(self):
        self.position = self._random_position()

    def draw(self, window):
        if self.image:
            img = pygame.transform.scale(self.image, (self.block_size, self.block_size))
            window.blit(img, self.position)
        else:
            pygame.draw.rect(window, (255, 0, 0), (*self.position, self.block_size, self.block_size))

    def get_position(self):
        return self.position