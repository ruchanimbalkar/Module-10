# ----------------------------------------------------------------------------- #
# Title: Module 10 - Creating a numberpad Window UI
# # Description: Practicing to create a number pad
# --window_root (tk.Tk)
# --lbl_number_keys (tk.label)
# --btn_1(tk.button)
# --btn_2(tk.button)
# --btn_3(tk.button)
# --btn_4(tk.button)
# --btn_5(tk.button)
# --btn_6(tk.button)
# --btn_7(tk.button)
# --btn_8(tk.button)
# --btn_9(tk.button)
# --btn_0(tk.button)
# ChangeLog: (Who, When, What)
# Rucha Nimbalkar, 12/12/2024,Created Script
# ------------------------------------------------------------------------------ #

import tkinter as tk

application_window = tk.Tk() #creates a root node
#application_window.mainloop() #displays window UI #Commented because dimensions and label are added
#This window serves as a  holder for widgets, encompassing them within its boundaries.

application_window.geometry("400x100") #Define the size of the window
application_window.title("Number Pad")#Adds a title to the Window

#Create a label object in the Window and add it to the grid container
lbl_number_keys = tk.Label(application_window, text = "Number Keys")
lbl_number_keys.grid(row=1, column=1, sticky=tk.NW, padx=10, pady=5)

#Create a button for 1 and add it to a grid container
btn_1 = tk.Button(application_window, text="1", width=3)
btn_1.grid(row=2, column=2, sticky=tk.NW, padx=5, pady=5)

#Create a button for 2 and add it to a grid container
btn_2 = tk.Button(application_window, text="2", width=3)
btn_2.grid(row=2, column=3, sticky=tk.NW, padx=5, pady=5)

#Create a button for 3 and add it to a grid container
btn_3 = tk.Button(application_window, text="3", width=3)
btn_3.grid(row=2, column=4, sticky=tk.NW, padx=5, pady=5)

#Create a button for 4 and add it to a grid container
btn_4 = tk.Button(application_window, text="4", width=3)
btn_4.grid(row=2, column=5, sticky=tk.NW, padx=5, pady=5)

#Create a button for 5 and add it to a grid container
btn_5 = tk.Button(application_window, text="5", width=3)
btn_5.grid(row=2, column=6, sticky=tk.NW, padx=5, pady=5)


#Create a button for 6 and add it to a grid container
btn_6 = tk.Button(application_window, text="6", width=3)
btn_6.grid(row=3, column=2, sticky=tk.NW, padx=5, pady=5)


#Create a button for 7 and add it to a grid container
btn_7 = tk.Button(application_window, text="7", width=3)
btn_7.grid(row=3, column=3, sticky=tk.NW, padx=5, pady=5)

#Create a button for 8 and add it to a grid container
btn_8 = tk.Button(application_window, text="8", width=3)
btn_8.grid(row=3, column=4, sticky=tk.NW, padx=5, pady=5)

#Create a button for 9 and add it to a grid container
btn_9 = tk.Button(application_window, text="9", width=3)
btn_9.grid(row=3, column=5, sticky=tk.NW, padx=5, pady=5)

#Create a button for 0 and add it to a grid container
btn_0 = tk.Button(application_window, text="0", width=3)
btn_0.grid(row=3, column=6, sticky=tk.NW, padx=5, pady=5)

#Display the window
application_window.mainloop()