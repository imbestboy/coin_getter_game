import customtkinter
import models


def get_settings_from_db() -> models.Setting:
    """get_settings_from_db get user settings from database

    Returns:
        models.Settings -- setting table
    """
    settings, _ = models.Setting.get_or_create(id=1)
    return settings


def change_difficulty(difficulty: str) -> None:
    """change_difficulty change database difficulty

    Arguments:
        difficulty {str} -- new difficulty
    """
    settings = get_settings_from_db()
    settings.difficulty = difficulty
    settings.save()


def change_spaceship_speed(speed: int) -> None:
    """change_spaceship_speed_in_settings change spaceship speed on database

    Arguments:
        speed {int} -- new speed
    """
    if isinstance(speed, int):
        settings = get_settings_from_db()
        settings.spaceship_speed = speed
        settings.save()
    else:
        raise ValueError("speed should be int")


def change_theme(theme: str) -> None:
    """change_theme change application theme

    Arguments:
        theme {str} -- only "dark" , "light" and "system"
    """
    if theme in ("dark", "light", "system"):
        customtkinter.set_appearance_mode(theme)
        settings = get_settings_from_db()
        settings.theme = theme[0]
        settings.save()
    else:
        raise ValueError("theme should be in 'dark' , 'light' and 'system'")


def show_spaceship_speed_value(
    speed_value: float, spaceship_speed_label: customtkinter.CTkLabel
) -> None:
    """change_spaceship_speed change spaceship speed label next to spaceship slider for end user with every slider move

    Arguments:
        speed_value {float} -- spaceship speed
        spaceship_speed_label {customtkinter.CTkLabel} -- label to show spaceship speed
    """
    speed_value = int(speed_value)
    spaceship_speed_label.configure(text=speed_value)
    change_spaceship_speed(speed_value)


def show_statistic():
    pass
