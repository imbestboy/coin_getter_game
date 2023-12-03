import customtkinter

# -- screen config
SCREEN_WIDTH: int = 900
SCREEN_HEIGHT: int = 800

# -- theme config
customtkinter.set_default_color_theme("dark-blue")
customtkinter.set_appearance_mode("system")

# -- creating temp window for config fonts this window will destroy
temp_window = customtkinter.CTk()

# -- font config
normal_font = customtkinter.CTkFont("Helvetica", 22)
bold_font = customtkinter.CTkFont("Helvetica", 22, "bold")
big_font = customtkinter.CTkFont("Helvetica", 32)
big_bold_font = customtkinter.CTkFont("Helvetica", 32, "bold")
small_font = customtkinter.CTkFont("Helvetica", 12)
small_bold_font = customtkinter.CTkFont("Helvetica", 12, "bold")

temp_window.destroy()
