import pygame

class Snake:
    def __init__(self, block_size, color, start_pos):
        self.block_size = block_size
        self.body = [start_pos]
        self.direction = (0, 0)  # Ahora empieza quieta
        self.color = color
        self.growing = False

    def set_direction(self, dx, dy):
        if (dx, dy) == (-self.direction[0], -self.direction[1]):
            return
        self.direction = (dx, dy)

    def move(self):
        dx, dy = self.direction
        head_x, head_y = self.body[-1]
        new_head = (head_x + dx * self.block_size, head_y + dy * self.block_size)
        self.body.append(new_head)
        if not self.growing:
            self.body.pop(0)
        else:
            self.growing = False

    def grow(self):
        self.growing = True

    def get_head_position(self):
        return self.body[-1]

    def check_collision(self, width, height):
        head = self.get_head_position()
        x, y = head
        return (
            x < 0 or x >= width or y < 0 or y >= height or head in self.body[:-1]
        )

    def draw(self, surface):
        for segment in self.body:
            rect = pygame.Rect(segment[0], segment[1], self.block_size, self.block_size)
            pygame.draw.rect(surface, self.color, rect)