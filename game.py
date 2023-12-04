import pygame
import random
import customtkinter

import config
import main_menu


def start_game(main_menu_window: customtkinter.CTk, spaceship_speed_label: int) -> None:
    """start_game close main menu and start the game

    Arguments:
        main_menu_window {customtkinter.CTk} -- tkinter main menu window
    """
    # -- loading main menu settings
    dark_mode = True if main_menu_window["bg"] == "gray10" else False
    spaceship_speed = int(spaceship_speed_label.cget("text"))
    game_background_color = main_menu_window["bg"]
    SPACESHIP_COLOR = "gray95" if dark_mode else "gray10"
    BLOCK_COLOR = "#b30000" if dark_mode else "#800000"
    COIN_COLOR = "#ffff00" if dark_mode else "#cccc00"

    # -- close main menu window
    main_menu_window.destroy()

    # -- pygame setup
    pygame.init()
    clock = pygame.time.Clock()
    is_running = True
    game_over = False

    # -- game window size
    screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
    spaceship_x = config.SPACESHIP_RESPAWN_X
    spaceship_y = config.SPACESHIP_RESPAWN_Y

    # -- block setup
    block_x = random.randint(0, config.SCREEN_WIDTH - config.BLOCK_WIDTH)
    block_y = -config.BLOCK_HEIGHT

    # -- coin setup
    coin_radius = config.coin_radius
    coin_x = random.randint(0, config.SCREEN_WIDTH - config.coin_radius)
    coin_y = (-config.coin_radius) * 10

    # -- game loop
    while is_running:
        for event in pygame.event.get():
            # -- pygame.QUIT event means the user clicked X to close your window
            if event.type == pygame.QUIT:
                is_running = False
                # -- run main menu window again
                main_menu.start_main_menu()

        screen.fill(game_background_color)

        if game_over:
            is_running = False
            # -- run main menu window again
            main_menu.start_main_menu()
        else:
            # -- get which key pressed by user (pygame.K_LEFT => left arrow and pygame.K_RIGHT => right arrow)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and spaceship_x > 15:
                spaceship_x -= spaceship_speed
            elif (
                keys[pygame.K_RIGHT]
                and spaceship_x < config.SCREEN_WIDTH - config.SPACESHIP_WIDTH - 15
            ):
                spaceship_x += spaceship_speed

            coin_y += config.coin_speed
            if coin_y > config.SCREEN_HEIGHT:
                coin_x = random.randint(0, config.SCREEN_WIDTH - config.coin_radius)
                coin_y = (-config.coin_radius) * 10

            block_y += config.block_speed
            if block_y > config.SCREEN_HEIGHT:
                block_x = random.randint(0, config.SCREEN_WIDTH - config.BLOCK_WIDTH)
                block_y = -config.BLOCK_HEIGHT

            if (
                spaceship_x < (block_x + config.BLOCK_WIDTH)
                and (spaceship_x + config.SPACESHIP_WIDTH) > block_x
                and spaceship_y < (block_y + config.BLOCK_HEIGHT)
                and (spaceship_y + config.SPACESHIP_HEIGHT) > block_y
            ):
                game_over = True

        pygame.draw.rect(
            screen,
            SPACESHIP_COLOR,
            (
                spaceship_x,
                spaceship_y,
                config.SPACESHIP_WIDTH,
                config.SPACESHIP_HEIGHT,
            ),
        )

        pygame.draw.rect(
            screen,
            BLOCK_COLOR,
            (
                block_x,
                block_y,
                config.BLOCK_WIDTH,
                config.BLOCK_HEIGHT,
            ),
        )

        pygame.draw.circle(
            screen,
            COIN_COLOR,
            (coin_x, coin_y),
            config.coin_radius,
        )

        # -- update() the display to put your work on screen
        pygame.display.update()

        # -- limits FPS to 60
        clock.tick(60)

    pygame.quit()
