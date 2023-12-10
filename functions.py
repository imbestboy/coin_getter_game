import customtkinter
import models
import config


def get_username(string_var: customtkinter.StringVar) -> str:
    """get_username convert string var tkinter default variable to str

    Arguments:
        string_var {customtkinter.StringVar} -- string var contains username

    Returns:
        str -- username
    """
    username = string_var.get()
    return username


def set_record_to_db(username: str, score: int) -> None:
    """set_record_to_db set each game record to database

    Arguments:
        username {str} -- name of user
        score {int} -- score of user
    """
    models.Record.create(name=username, score=score)


def set_statistic_to_db(coin_count: int, score: int) -> None:
    """set_statistic_to_db add each game statistic to database

    Arguments:
        coin_count {int} -- count of coins user get
        score {int} -- score of user
    """
    statistic = get_statistic_from_db()
    statistic.game_count += 1
    statistic.coin_count += coin_count
    statistic.score += score
    statistic.save()


def get_statistic_from_db() -> models.Statistic:
    """get_statistic_from_db get statistic from database

    Returns:
        models.Statistic -- statistic table
    """
    statistic, _ = models.Statistic.get_or_create(id=1)
    return statistic


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


def show_statistic(main_menu_window: customtkinter.CTk):
    statistic = get_statistic_from_db()
    statistic_window = customtkinter.CTkToplevel(main_menu_window)
    statistic_window.geometry(
        f"{config.STATISTIC_WINDOW_WIDTH}x{config.STATISTIC_WINDOW_HEIGHT}"
    )
    statistic_window.title("Game Statistic")
    statistic_window.resizable(False, False)
    customtkinter.CTkLabel(
        statistic_window,
        text=f"Total game played : {statistic.game_count}",
        font=config.normal_font,
    ).grid(row=0, column=0, pady=10)
    customtkinter.CTkLabel(
        statistic_window,
        text=f"Total coin collected : {statistic.coin_count}",
        font=config.normal_font,
    ).grid(row=1, column=0, pady=10)
    customtkinter.CTkLabel(
        statistic_window,
        text=f"Total score earned : {statistic.score}",
        font=config.normal_font,
    ).grid(row=2, column=0, pady=10)

    customtkinter.CTkLabel(
        statistic_window,
        text="3 Latest records :",
        font=config.normal_font,
    ).grid(row=3, column=0, pady=10)
    row = 4
    for record in models.Record.select().order_by(models.Record.id.desc()):
        customtkinter.CTkLabel(
            statistic_window,
            text=f"{record.name} : {record.score}",
            font=config.normal_font,
        ).grid(row=row, column=0, pady=10)
        row += 1
        if row == 7:
            break

    customtkinter.CTkButton(
        statistic_window,
        text="Done",
        command=statistic_window.destroy,
        font=config.normal_font,
        height=40,
    ).grid(column=0, row=row, pady=10)
