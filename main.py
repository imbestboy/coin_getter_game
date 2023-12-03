import customtkinter

import functions
import config

# -- create main menu window
main_menu_window = customtkinter.CTk()
main_menu_window.geometry(f"{config.SCREEN_WIDTH}x{config.SCREEN_HEIGHT}")

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
customtkinter.CTkButton(
    main_menu_window, text="System", command=lambda: functions.change_theme("system")
).grid(column=3, row=0, pady=30)

# -- speed section
customtkinter.CTkLabel(
    main_menu_window,
    text=f"Spaceship Speed (default : {config.spaceship_default_speed}) : ",
    font=config.normal_font,
).grid(column=0, row=1)


# -- keep running
main_menu_window.mainloop()
