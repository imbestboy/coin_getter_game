import pygame
import random
import customtkinter

import config
import main_menu


def start_game(main_menu_window: customtkinter.CTk) -> None:
    """start_game close main menu and start the game

    Arguments:
        main_menu_window {customtkinter.CTk} -- tkinter main menu window
    """
    # -- close main menu window
    main_menu_window.destroy()

    # -- pygame setup
    pygame.init()
    clock = pygame.time.Clock()
    is_running = True

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
        colors_list = [
            "purple",
            "red",
            "blue",
            "gray",
            "green",
            "yellow",
            "black",
            "white",
        ]
        screen.fill(random.choice(colors_list))

        # -- RENDER THE GAME

        # -- update() the display to put your work on screen
        pygame.display.update()

        # -- limits FPS to 60
        clock.tick(60)

    pygame.quit()
