import customtkinter
import tkinter

import functions
import config
import game


def start_main_menu():
    # -- create main menu window
    main_menu_window = customtkinter.CTk()

    # -- main menu window config
    main_menu_window.geometry(f"{config.SCREEN_WIDTH}x{config.SCREEN_HEIGHT}")
    main_menu_window.title("Main Menu")
    main_menu_window.resizable(False, False)

    # load settings from database
    settings = functions.get_settings_from_db()

    # -- add theme section to main menu window
    customtkinter.CTkLabel(
        main_menu_window,
        text="Choose game theme (default : system) : ",
        font=config.normal_font,
    ).grid(column=0, row=0, padx=10, pady=30)
    customtkinter.CTkButton(
        main_menu_window, text="Dark", command=lambda: functions.change_theme("dark")
    ).grid(column=1, row=0, pady=30)
    customtkinter.CTkButton(
        main_menu_window, text="Light", command=lambda: functions.change_theme("light")
    ).grid(column=2, row=0, padx=10, pady=30)

    # -- speed section
    customtkinter.CTkLabel(
        main_menu_window,
        text=f"Spaceship Speed (default : {config.spaceship_default_speed}) : ",
        font=config.normal_font,
    ).grid(column=0, row=1)
    spaceship_speed = customtkinter.IntVar(value=settings.spaceship_speed)
    spaceship_speed_slider = customtkinter.CTkSlider(
        main_menu_window,
        from_=1,
        to=20,
        number_of_steps=19,
        variable=spaceship_speed,
        command=lambda value: functions.show_spaceship_speed_value(
            value, spaceship_speed_label
        ),
        width=150,
    )
    spaceship_speed_slider.grid(column=1, row=1)
    spaceship_speed_label = customtkinter.CTkLabel(
        main_menu_window, text=settings.spaceship_speed, font=config.bold_font
    )
    spaceship_speed_label.grid(column=2, row=1)

    # -- game difficulty section
    customtkinter.CTkLabel(
        main_menu_window,
        text="Choose game difficulty (default: medium) : ",
        font=config.normal_font,
    ).grid(column=0, row=2, pady=30)
    difficulty_var = tkinter.StringVar(value=settings.difficulty)
    easy_radio_button = customtkinter.CTkRadioButton(
        main_menu_window,
        text="Easy",
        variable=difficulty_var,
        value="e",
        command=lambda: functions.change_difficulty("e"),
    )
    medium_radio_button = customtkinter.CTkRadioButton(
        main_menu_window,
        text="Medium",
        variable=difficulty_var,
        value="m",
        command=lambda: functions.change_difficulty("m"),
    )
    hard_radio_button = customtkinter.CTkRadioButton(
        main_menu_window,
        text="Hard",
        variable=difficulty_var,
        value="h",
        command=lambda: functions.change_difficulty("h"),
    )
    easy_radio_button.grid(column=1, row=2, pady=30)
    medium_radio_button.grid(column=2, row=2, pady=30, ipadx=20)
    hard_radio_button.grid(column=3, row=2, pady=30, ipadx=20)

    # -- start game section
    customtkinter.CTkButton(
        main_menu_window,
        text="Start game",
        command=lambda: game.start_game(main_menu_window=main_menu_window),
        width=220,
        height=60,
        font=config.bold_font,
    ).grid(column=2, row=3, columnspan=2)

    customtkinter.CTkButton(
        main_menu_window,
        text="Quit",
        command=main_menu_window.destroy,
        width=220,
        height=60,
        font=config.normal_font,
    ).grid(column=0, row=3, columnspan=2)

    return main_menu_window
