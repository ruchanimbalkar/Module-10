# ----------------------------------------------------------------------------- #
# Title: Module 10 - Creating a Windowed UI
# # Description: Creates the following UI objects
# --window_root (tk.Tk)
# --lbl_math_info (tk.label)
# ChangeLog: (Who, When, What)
# Rucha Nimbalkar, 12/12/2024,Created Script
# ------------------------------------------------------------------------------ #

import tkinter as tk

application_window = tk.Tk() #creates a root node

#This window serves as a  holder for widgets, encompassing them within its boundaries.

application_window.geometry("400x100") #Define the size of the window

#Create a label object in the Window and get a reference
lbl_math_results = tk.Label(application_window, text = "Math Results")

#add to the root container using the pack "Layout Manager" method
lbl_math_results.pack()

#Display the window
application_window.mainloop()