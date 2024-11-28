import tkinter as tk

root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# App title
APP_TITLE = "Student Management System"

# Scaling factor
SCALING = 2

# height and width of app
APP_WIDTH = screen_width//SCALING
APP_HEIGHT = screen_height//SCALING

# Position of app to the center of screen
X_POS = (screen_width//SCALING) - (APP_WIDTH//2)
Y_POS = (screen_height//SCALING) - (APP_HEIGHT//2)

APP_RESOLUTION = f"{APP_WIDTH}x{APP_HEIGHT}+{X_POS}+{Y_POS}"
