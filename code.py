import pygame
from GameConfig import GameConfig
from Snake import Snake
from Food import Food
from Game import Game

def pantalla_inicio(window, background_img, font_big):
    negro = (0, 0, 0)
    azul = (0, 0, 128)
    blanco = (255, 255, 255)

    boton_jugar = pygame.Rect(200, 250, 200, 50)  # Ajusta según tu resolución

    esperando = True
    while esperando:
        window.blit(background_img, (0, 0))

        # Título
        titulo = font_big.render("Juego de la Culebrita", True, negro)
        window.blit(titulo, (window.get_width() // 2 - titulo.get_width() // 2, 150))

        # Botón
        pygame.draw.rect(window, azul, boton_jugar)
        texto_jugar = font_big.render("Jugar", True, blanco)
        window.blit(texto_jugar, (boton_jugar.x + 45, boton_jugar.y + 5))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if boton_jugar.collidepoint(pygame.mouse.get_pos()):
                    esperando = False

def main():
    config = GameConfig()

    # Mostrar pantalla de inicio
    pantalla_inicio(config.window, config.fondo_img, config.font_big)

    # Crear instancia de la serpiente
    snake = Snake(config.BLOCK_SIZE, config.NAVY_BLUE, (config.WIDTH // 2, config.HEIGHT // 2))

    # Crear comida
    food = Food(config.BLOCK_SIZE, config.WIDTH, config.HEIGHT)

    # Sonidos en diccionario
    sounds = {
        'eat': config.sonido_comida,
        'lose': config.sonido_perder
    }

    # Crear el juego
    game = Game(
        config.window,
        snake,
        food,
        sounds,
        config.fondo_img,
        config.font_small,
        config.font_big,
        config.BLOCK_SIZE,
        config.WIDTH,
        config.HEIGHT
    )

    # Iniciar música
    pygame.mixer.music.play(-1)

    # Correr el juego
    game.run()

    pygame.quit()

if __name__ == "__main__":
    main()