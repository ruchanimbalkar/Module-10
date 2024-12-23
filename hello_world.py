# ----------------------------------------------------------------------------- #
# Title: Module 10 - Creating a Windowed UI
# # Description: Creates the UI object
# --window_root (tk.Tk)
# ChangeLog: (Who, When, What)
# Rucha Nimbalkar, 12/21/2024,Created Script
# ------------------------------------------------------------------------------ #

import tkinter as tk
application_window = tk.Tk() #creates a root node
application_window.geometry("300x100")
application_window.title("HELLO WORLD")
hello_world_label = tk.Label(application_window, text = "Hello, World!")
hello_world_label.grid(row=4, column=2, sticky=tk.NW, padx=10, pady=5)
application_window.mainloop() #displays window UI