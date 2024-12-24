# ----------------------------------------------------------------------------- #
# Title: Module 10 - Creating a Windowed UI
# # Description: Creates the UI object (https://www.pythonguis.com/tutorials/create-ui-with-tkinter-grid-layout-manager/)
# --window_root (tk.Tk)
# ChangeLog: (Who, When, What)
# Rucha Nimbalkar, 12/23/2024,Created Script
# Rucha Nimbalkar, 12/23/2024,Added title
# Rucha Nimbalkar, 12/23/2024,Added image reference using tkinter
# Rucha Nimbalkar, 12/23/2024,Added image to the grid
# ------------------------------------------------------------------------------ #
import tkinter as tk
application_window = tk.Tk() #creates a root node
application_window.geometry("500x300")
application_window.title("Happy Holidays")
application_window.config(bg="lightblue")

image = tk.PhotoImage(file="Happy Holidays.png")
large_img = image.subsample(4,4)

img = tk.Label(application_window, image=large_img)
img.grid(row=0, column=0, rowspan=6, padx=5, pady=5)
application_window.mainloop() #displays window UI