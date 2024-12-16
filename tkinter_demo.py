# ----------------------------------------------------------------------------- #
# Title: Module 10 - Creating a Windowed UI
# # Description: Creates the UI object
# --window_root (tk.Tk)
# ChangeLog: (Who, When, What)
# Rucha Nimbalkar, 12/15/2024,Created Script
# ------------------------------------------------------------------------------ #

import tkinter as tk
application_window = tk.Tk() #creates a root node
application_window.geometry("600x200")
application_window.title("TKINTER")
application_window.mainloop() #displays window UI