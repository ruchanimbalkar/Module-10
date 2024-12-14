# ----------------------------------------------------------------------------- #
# Title: Module 10 - Creating a time widget Window UI
# # Description: Time Widget to show current time
# --window_root (tk.Tk)
# --lbl_time_teller (tk.label)
# --lbl_time (tk.label)
# --lbl_hours (tk.label)
# ChangeLog: (Who, When, What)
# Rucha Nimbalkar, 12/12/2024,Created Script
# ------------------------------------------------------------------------------ #
import datetime
import tkinter as tk
from datetime import datetime #from datetime import date
application_window = tk.Tk() #creates a root node
#application_window.mainloop() #displays window UI #Commented because dimensions and label are added
#This window serves as a  holder for widgets, encompassing them within its boundaries.

application_window.geometry("400x100") #Define the size of the window
application_window.title("Current Time")#Adds a title to the Window

#Create a label object in the Window and add it to the grid container
lbl_time_teller = tk.Label(application_window, text = "The time is: ")
lbl_time_teller.grid(row=1, column=1, sticky=tk.NW, padx=10, pady=5)


now = datetime.now() # current time

time = now.strftime("%H:%M:%S")

#Create a label object in the Window and add it to the grid container
lbl_time= tk.Label(application_window, text = time)
lbl_time.grid(row=1, column=2, sticky=tk.NW, padx=10, pady=5)

#Create a label object in the Window and add it to the grid container
lbl_hours= tk.Label(application_window, text = "HRS")
lbl_hours.grid(row=1, column=3, sticky=tk.NW, padx=10, pady=5)

#Display the window
application_window.mainloop()