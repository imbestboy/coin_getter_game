import customtkinter

# -- screen config
SCREEN_WIDTH: int = 1000
SCREEN_HEIGHT: int = 800

# -- theme config
customtkinter.set_default_color_theme("dark-blue")
customtkinter.set_appearance_mode("system")

# -- creating temp window for config fonts this window will destroy
temp_window = customtkinter.CTk()

# -- font config
normal_font = customtkinter.CTkFont("Helvetica", 20)
bold_font = customtkinter.CTkFont("Helvetica", 20, "bold")
big_font = customtkinter.CTkFont("Helvetica", 30)
big_bold_font = customtkinter.CTkFont("Helvetica", 30, "bold")
small_font = customtkinter.CTkFont("Helvetica", 12)
small_bold_font = customtkinter.CTkFont("Helvetica", 12, "bold")

temp_window.destroy()

# -- spaceship config
spaceship_default_speed = 10
SPACESHIP_WIDTH: int = 60
SPACESHIP_HEIGHT: int = 60
SPACESHIP_RESPAWN_X: int = (SCREEN_WIDTH // 2) - (SPACESHIP_WIDTH // 2)
SPACESHIP_RESPAWN_Y: int = SCREEN_HEIGHT - SPACESHIP_HEIGHT - 20
