import pygame
import random
import customtkinter

import config
import main_menu
import functions


def start_game(main_menu_window: customtkinter.CTk, username: str) -> None:
    """start_game close main menu and start the game

    Arguments:
        main_menu_window {customtkinter.CTk} -- tkinter main menu window
    """
    # -- loading settings
    settings = functions.get_settings_from_db()
    dark_mode = True if settings.theme == "d" else False
    spaceship_speed = settings.spaceship_speed
    game_background_color = main_menu_window["bg"]
    SPACESHIP_COLOR = "gray95" if dark_mode else "gray10"
    BLOCK_COLOR = "#b30000" if dark_mode else "#800000"
    COIN_COLOR = "#ffff00" if dark_mode else "#cccc00"
    TEXT_COLOR = "gray84" if dark_mode else "gray14"
    difficulty = settings.difficulty

    # -- close main menu window
    main_menu_window.destroy()

    # -- pygame setup
    pygame.init()
    game_normal_font = pygame.font.SysFont("Helvetica", 32)
    clock = pygame.time.Clock()
    is_running = True
    game_over = False
    score = 0
    combo = 1.0
    is_pause = False
    coin_count = 0

    # -- game window size
    screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
    spaceship_x = config.SPACESHIP_RESPAWN_X
    spaceship_y = config.SPACESHIP_RESPAWN_Y

    # -- block setup
    if difficulty == "h":
        blocks = [
            [
                random.randint(0, config.SCREEN_WIDTH - config.BLOCK_WIDTH),
                -config.BLOCK_HEIGHT,
            ],
            [
                random.randint(0, config.SCREEN_WIDTH - config.BLOCK_WIDTH),
                -config.BLOCK_HEIGHT * 2.5,
            ],
            [
                random.randint(0, config.SCREEN_WIDTH - config.BLOCK_WIDTH),
                -config.BLOCK_HEIGHT * 4.5,
            ],
        ]
    elif difficulty == "m":
        blocks = [
            [
                random.randint(0, config.SCREEN_WIDTH - config.BLOCK_WIDTH),
                -config.BLOCK_HEIGHT,
            ],
            [
                random.randint(0, config.SCREEN_WIDTH - config.BLOCK_WIDTH),
                -config.BLOCK_HEIGHT * 2.5,
            ],
        ]
    else:
        blocks = [
            [
                random.randint(0, config.SCREEN_WIDTH - config.BLOCK_WIDTH),
                -config.BLOCK_HEIGHT,
            ],
        ]
    block_speed = config.block_speed

    # -- coin setup
    coin_radius = config.coin_radius
    coin_x = random.randint(coin_radius, config.SCREEN_WIDTH - coin_radius)
    coin_y = (-coin_radius) * 10
    coin_speed = config.coin_speed

    # -- game loop
    while is_running:
        for event in pygame.event.get():
            # -- pygame.QUIT event means the user clicked X to close your window
            if event.type == pygame.QUIT:
                is_running = False
                functions.set_record_to_db(username=username, score=score)
                functions.set_statistic_to_db(coin_count=coin_count, score=score)
                # -- run main menu window again
                main_menu.start_main_menu()
            if event.type == pygame.KEYDOWN and event.key in (
                pygame.K_ESCAPE,
                pygame.K_p,
            ):
                is_pause = not is_pause

        screen.fill(game_background_color)

        if game_over:
            is_running = False
            functions.set_statistic_to_db(coin_count=coin_count, score=score)
            functions.set_record_to_db(username=username, score=score)
            # -- run main menu window again
            main_menu.start_main_menu()
        elif is_pause:
            score_text = game_normal_font.render(f"Game paused", True, TEXT_COLOR)
            screen.blit(score_text, (config.PAUSE_X, config.PAUSE_Y))
        else:
            # -- get which key pressed by user (pygame.K_LEFT => left arrow and pygame.K_RIGHT => right arrow)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and spaceship_x > 15:
                spaceship_x -= spaceship_speed
            if (
                keys[pygame.K_RIGHT]
                and spaceship_x < config.SCREEN_WIDTH - config.SPACESHIP_WIDTH - 15
            ):
                spaceship_x += spaceship_speed
            if keys[pygame.K_UP] and spaceship_y > 15:
                spaceship_y -= spaceship_speed
            if (
                keys[pygame.K_DOWN]
                and spaceship_y < config.SCREEN_HEIGHT - config.SPACESHIP_HEIGHT - 15
            ):
                spaceship_y += spaceship_speed

            coin_y += coin_speed
            if coin_y > config.SCREEN_HEIGHT:
                coin_x = random.randint(0, config.SCREEN_WIDTH - coin_radius)
                coin_y = (-coin_radius) * 10
                block_speed = config.block_speed
                coin_speed = config.coin_speed
                combo = 1.0
            for block_index in range(len(blocks)):
                blocks[block_index][1] += block_speed
                block_x, block_y = blocks[block_index]
                if block_y > config.SCREEN_HEIGHT:
                    blocks[block_index][0] = random.randint(
                        0, config.SCREEN_WIDTH - config.BLOCK_WIDTH
                    )
                    blocks[block_index][1] = -config.BLOCK_HEIGHT
                if (
                    spaceship_x < (block_x + config.BLOCK_WIDTH)
                    and (spaceship_x + config.SPACESHIP_WIDTH) > block_x
                    and spaceship_y < (block_y + config.BLOCK_HEIGHT)
                    and (spaceship_y + config.SPACESHIP_HEIGHT) > block_y
                ):
                    game_over = True

            if (
                spaceship_x < coin_x + coin_radius
                and spaceship_x + config.SPACESHIP_WIDTH > coin_x - coin_radius
                and spaceship_y < coin_y + coin_radius
                and spaceship_y + config.SPACESHIP_HEIGHT > coin_y - coin_radius
            ):
                coin_count += 1
                score += (
                    10 * combo
                    if (spaceship_y + config.SPACESHIP_HEIGHT)
                    >= (config.SCREEN_HEIGHT // 3)
                    else 10 * (combo + 0.2)
                )
                coin_x = random.randint(coin_radius, config.SCREEN_WIDTH - coin_radius)
                coin_y = -coin_radius
                combo += (
                    0.1
                    if (spaceship_y + config.SPACESHIP_HEIGHT)
                    >= (config.SCREEN_HEIGHT // 3)
                    else 0.2
                )
                coin_speed = (
                    coin_speed + config.INCREASE_SPEED
                    if coin_speed < config.MAX_SPEED
                    else MAX_SPEED
                )
                block_speed = (
                    block_speed + config.INCREASE_SPEED
                    if block_speed < config.MAX_SPEED
                    else MAX_SPEED
                )

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

        for block_x, block_y in blocks:
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
            coin_radius,
        )

        score_text = game_normal_font.render(f"Score: {int(score)}", True, TEXT_COLOR)
        screen.blit(score_text, (config.SCORE_X, config.SCORE_Y))

        score_text = game_normal_font.render(f"Combo: {combo:.1f}x", True, TEXT_COLOR)
        screen.blit(score_text, (config.COMBO_X, config.COMBO_Y))

        # -- update() the display to put your work on screen
        pygame.display.update()

        # -- limits FPS to 60
        clock.tick(60)

    pygame.quit()
