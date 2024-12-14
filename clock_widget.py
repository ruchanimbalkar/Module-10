# ----------------------------------------------------------------------------- #
# Title: Module 10 - Creating a real time clock widget Window UI
# # Description: Clock Widget to show current time
# --window_root (tk.Tk)
# --lbl_time_teller (tk.label)
# --lbl_time (tk.label)
# --lbl_hours (tk.label)
# ChangeLog: (Who, When, What)
# Rucha Nimbalkar, 12/13/2024,Created Script
# Rucha Nimbalkar, 12/13/2024 Added code from "https://pythonbasics.org/tkinter-label/" to display clock on widget
# ------------------------------------------------------------------------------ #
import tkinter as tk
from tkinter import Frame
from tkinter import Label
import time

application_window = tk.Tk() #creates a root node

class App(Frame):

    def __init__(self,master=None):
        Frame.__init__(self, master)
        self.master = master
        self.label = Label(text="", fg="Green", font=("Cambria Math", 26))
        self.label.place(x=100,y=20)
        self.update_clock()

    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.label.configure(text=now)
        self.after(1000, self.update_clock)


application_window.geometry("400x200") #Define the size of the window
application_window.title("Tkinter Digital Clock")#Adds a title to the Window
app=App(application_window) #Create an App object #Set attributes for time label
application_window.after(1000, app.update_clock)

#Display the window
application_window.mainloop()