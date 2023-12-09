import main_menu
import models

# -- create and initialize database
models.database_init()

# -- create main menu window
main_menu_window = main_menu.start_main_menu()

# -- keep running
main_menu_window.mainloop()
