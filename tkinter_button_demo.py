# --------------------------------------------------------------------------------------------------------- #
# Title: Module 10 - Creating a numberpad Window UI
# # Description: Practicing to create a number pad
# --window_root (tk.Tk)
# --lbl_number_keys (tk.label)
# --my_button(tk.button)
# ChangeLog: (Who, When, What)
# Rucha Nimbalkar, 12/16/2024,Created Script
# Rucha Nimbalkar, 12/16/2024,Code for button with wider length added
# Rucha Nimbalkar, 12/16/2024,Tested code for button method by adding height parameter with value = 5
# ----------------------------------------------------------------------------------------------------------- #

import tkinter as tk

application_window = tk.Tk() #creates a root node
#application_window.mainloop() #displays window UI #Commented because dimensions and label are added
#This window serves as a  holder for widgets, encompassing them within its boundaries.

application_window.geometry("500x150") #Define the size of the window
application_window.title("Button Demo")#Adds a title to the Window

#Create a label object in the Window and add it to the grid container
lbl_number_keys = tk.Label(application_window, text = "My Button")
lbl_number_keys.grid(row=1, column=1, sticky=tk.NW, padx=10, pady=5)

#Create a button for 1 and add it to a grid container
my_button = tk.Button(application_window, text="Button", width=10, height= 5)
my_button.grid(row=2, column=2, sticky=tk.NW, padx=6, pady=6)


application_window.mainloop()