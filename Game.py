import pygame
from Snake import Snake

class Game:
    def __init__(self, window, snake, food, sounds, background_img, font, big_font, block_size, width, height):
        self.window = window
        self.snake = snake
        self.food = food
        self.sounds = sounds
        self.background_img = background_img
        self.font = font
        self.big_font = big_font
        self.block_size = block_size
        self.width = width
        self.height = height
        self.clock = pygame.time.Clock()
        self.running = True
        self.score = 0
        self.record = 0

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.snake.set_direction(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    self.snake.set_direction(1, 0)
                elif event.key == pygame.K_UP:
                    self.snake.set_direction(0, -1)
                elif event.key == pygame.K_DOWN:
                    self.snake.set_direction(0, 1)

    def update(self):
        self.snake.move()
        if self.snake.check_collision(self.width, self.height):
            self.sounds['lose'].play()
            pygame.time.delay(500)
            self.show_game_over()

        if self.snake.get_head_position() == self.food.get_position():
            self.sounds['eat'].play()
            self.snake.grow()
            self.food.respawn()
            self.score += 1

    def draw_text(self, text, color, position, big=False):
        font = self.big_font if big else self.font
        text_surface = font.render(text, True, color)
        self.window.blit(text_surface, position)

    def draw(self):
        self.window.blit(self.background_img, (0, 0))
        self.food.draw(self.window)
        self.snake.draw(self.window)
        self.draw_text(f"Puntaje: {self.score}", (255, 255, 255), (10, 10))
        pygame.display.update()

    def run(self):
        while self.running:
            self.handle_input()
            self.update()
            self.draw()
            self.clock.tick(15)

    def reset(self):
        self.snake = Snake(self.block_size, (0, 255, 0), (self.width // 2, self.height // 2))
        self.snake.set_direction(0, 0)  # Iniciar quieta
        self.food.respawn()
        if self.score > self.record:
            self.record = self.score
        self.score = 0

    def show_game_over(self):
        pygame.mixer.music.stop()
        self.sounds['lose'].play()
        pygame.time.delay(500)

        BLACK = (0, 0, 0)
        RED = (255, 0, 0)
        WHITE = (255, 255, 255)
        NAVY_BLUE = (0, 0, 128)

        nuevo_juego_btn = pygame.Rect(self.width // 2 - 100, self.height // 2, 200, 50)
        salir_btn = pygame.Rect(self.width // 2 - 100, self.height // 2 + 70, 200, 50)

        while True:
            self.window.fill(BLACK)

            perder_text = self.big_font.render("PERDISTE", True, RED)
            self.window.blit(perder_text, (self.width // 2 - perder_text.get_width() // 2, self.height // 3 - 50))

            score_text = self.font.render(f"PUNTAJE: {self.score}", True, WHITE)
            self.window.blit(score_text, (self.width // 2 - score_text.get_width() // 2, self.height // 3 + 10))

            pygame.draw.rect(self.window, NAVY_BLUE, nuevo_juego_btn)
            pygame.draw.rect(self.window, RED, salir_btn)

            nuevo_text = self.font.render("Nuevo Juego", True, WHITE)
            salir_text = self.font.render("Salir", True, WHITE)

            self.window.blit(nuevo_text, (nuevo_juego_btn.centerx - nuevo_text.get_width() // 2,
                                          nuevo_juego_btn.centery - nuevo_text.get_height() // 2))
            self.window.blit(salir_text, (salir_btn.centerx - salir_text.get_width() // 2,
                                          salir_btn.centery - salir_text.get_height() // 2))

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if nuevo_juego_btn.collidepoint(event.pos):
                        self.reset()
                        pygame.mixer.music.play(-1)
                        return
                    elif salir_btn.collidepoint(event.pos):
                        pygame.quit()
                        quit()
