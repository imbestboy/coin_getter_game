import customtkinter


def change_theme(theme: str) -> None:
    """change_theme change application theme

    Arguments:
        theme {str} -- only "dark" , "light" and "system"
    """
    if theme in ("dark", "light", "system"):
        customtkinter.set_appearance_mode(theme)
    else:
        raise ValueError("theme should be in 'dark' , 'light' and 'system'")


def show_spaceship_speed_value(
    speed_value: float, spaceship_speed_label: customtkinter.CTkLabel
) -> None:
    """show_spaceship_speed_value change spaceship speed label next to spaceship slider for end user with every slider move

    Arguments:
        speed_value {float} -- spaceship speed
        spaceship_speed_label {customtkinter.CTkLabel} -- label to show spaceship speed
    """
    spaceship_speed_label.configure(text=int(speed_value))
