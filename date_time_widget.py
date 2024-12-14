# ----------------------------------------------------------------------------- #
# Title: Module 10 - Creating a time widget Window UI
# # Description: Date and Time widget to show current time and date
# --window_root (tk.Tk)
# --lbl_date_time (tk.label)
# ChangeLog: (Who, When, What)
# Rucha Nimbalkar, 12/12/2024,Created Script
# ------------------------------------------------------------------------------ #

import tkinter as tk
from datetime import datetime #from datetime import datetime
application_window = tk.Tk() #creates a root node
#application_window.mainloop() #displays window UI #Commented because dimensions and label are added
#This window serves as a  holder for widgets, encompassing them within its boundaries.

application_window.geometry("400x100") #Define the size of the window
application_window.title("Current Date and Time")#Adds a title to the Window


now = datetime.now() # current date and time

#Create a label object in the Window and add it to the grid container
lbl_date_time= tk.Label(application_window, text = now)
lbl_date_time.grid(row=1, column=2, sticky=tk.NW, padx=10, pady=5)


#Display the window
application_window.mainloop()