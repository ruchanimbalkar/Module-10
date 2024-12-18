# ----------------------------------------------------------------------------- #
# Title: Module 10 - Creating a Log In Form
# # Description: Date and Time widget to show current time and date
# --window_root (tk.Tk)
# --user_name_label(tk.label)
# --pass_word_label(tk.label)
# --log_in_button(tk.button)
# ChangeLog: (Who, When, What)
# Rucha Nimbalkar, 12/17/2024,Created Script
# Rucha Nimbalkar, 12/17/2024,Added label for username
# Rucha Nimbalkar, 12/17/2024,Added text entry box for username
# Rucha Nimbalkar, 12/17/2024,Added label for password
# Rucha Nimbalkar, 12/17/2024,Added text entry box for password
# Rucha Nimbalkar, 12/17/2024,Added a log_in button to the form
# ------------------------------------------------------------------------------ #

import tkinter as tk

application_window = tk.Tk() #creates a root node
application_window.geometry("300x100") #Define the size of the window
application_window.title("Log In Form")#Adds a title to the Window

#Create a label object in the Window and add it to the grid container
user_name_label = tk.Label(application_window, text = "Username")
user_name_label.grid(row=3, column=2, sticky=tk.NW, padx=10, pady=5)

# Create a username entry window
user_name_text = tk.Entry(application_window, width=10)
user_name_text.grid(row=3, column=3)

pass_word_label = tk.Label(application_window, text = "Password")
pass_word_label.grid(row=4, column=2, sticky=tk.NW, padx=10, pady=5)

# Create a password entry window
pass_word_text = tk.Entry(application_window, width=10)
pass_word_text.grid(row=4, column=3)

# Create a log_in button and add it to a grid container
log_in_button = tk.Button(application_window, text="Log In", width=6)
log_in_button.grid(row=5, column=5, sticky=tk.NW, padx=5, pady=5)

application_window.mainloop() #displays window UI