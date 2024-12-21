# ------------------------------------------------------------------------------------------------ #
# Title: Module 10 - Creating a signup Form
# # Description: Date and Time widget to show current time and date
# --window_root (tk.Tk)
# --user_name_label(tk.label)
# --user_name_text(tk.entry)
# --password_label(tk.label)
# --password_text(tk.entry)
# --email_id_label(tk.label)
# --email_address_text(tk.entry)
# --sign_up_button(tk.button)
# ChangeLog: (Who, When, What)
# Rucha Nimbalkar, 12/20/2024,Created Script
# Rucha Nimbalkar, 12/20/2024,Added label and text entry box for username
# Rucha Nimbalkar, 12/20/2024,Added label and text entry box for password
# Rucha Nimbalkar, 12/20/2024,Added label for email address
# Rucha Nimbalkar, 12/20/2024,Added a text entry box for email address
# Rucha Nimbalkar, 12/20/2024,Added a signup button to the form
# -------------------------------------------------------------------------------------------------- #

import tkinter as tk

application_window = tk.Tk() #creates a root node
application_window.geometry("300x200") #Define the size of the window
application_window.title("Sign Up Form")#Adds a title to the Window

#Create a label object username in the Window and add it to the grid container
user_name_label = tk.Label(application_window, text = "username")
user_name_label.grid(row=1, column=1, sticky=tk.NW, padx=10, pady=5)

# Create a text entry window for username
user_name_text = tk.Entry(application_window, width=16)
user_name_text.grid(row=1, column=2)


#Create a label object password  in the Window and add it to the grid container
password_label = tk.Label(application_window, text = "password")
password_label.grid(row=2, column=1, sticky=tk.NW, padx=10, pady=5)

# Create a text entry window for password
password_text = tk.Entry(application_window, width=16)
password_text.grid(row=2, column=2)

#Create a label object 'email' in the Window and add it to the grid container
email_id_label = tk.Label(application_window, text = "email address")
email_id_label.grid(row=4, column=1, sticky=tk.NW, padx=10, pady=5)

# Create a text entry window for email address
email_address_text = tk.Entry(application_window, width=32)
email_address_text.grid(row=4, column=2)


# Create a signup button and add it to a grid container
sign_up_button = tk.Button(application_window, text="SIGN UP", width=6)
sign_up_button.grid(row=5, column=2, sticky=tk.NW, padx=5, pady=5)

application_window.mainloop() #displays window UI