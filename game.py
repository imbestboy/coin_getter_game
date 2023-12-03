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

    # -- close main menu window
    main_menu_window.destroy()

    # -- pygame setup
    pygame.init()
    clock = pygame.time.Clock()
    is_running = True

    # -- game window size
    screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))

    # -- game loop
    while is_running:
        for event in pygame.event.get():
            # -- pygame.QUIT event means the user clicked X to close your window
            if event.type == pygame.QUIT:
                is_running = False
                # -- run main menu window again
                main_menu.start_main_menu()

        # -- for test screen color will change
        game_background_color = "gray10" if dark_mode else "gray95"
        screen.fill(game_background_color)

        # -- RENDER THE GAME

        # -- update() the display to put your work on screen
        pygame.display.update()

        # -- limits FPS to 60
        clock.tick(60)

    pygame.quit()
