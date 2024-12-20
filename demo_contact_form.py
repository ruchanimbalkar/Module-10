# ------------------------------------------------------------------------------------------------ #
# Title: Module 10 - Creating a Contact Form
# # Description: Date and Time widget to show current time and date
# --window_root (tk.Tk)
# --first_name_label(tk.label)
# --first_name_text(tk.entry)
# --last_name_label(tk.label)
# --last_name_text(tk.entry)
# --subject_label(tk.label)
# --subject_text(tk.entry)
# --message_label(tk.label)
# --multi_line_message_text(tk.text)
# --submit_button(tk.button)
# ChangeLog: (Who, When, What)
# Rucha Nimbalkar, 12/19/2024,Created Script
# Rucha Nimbalkar, 12/19/2024,Added label and text entry box for first name  and last name
# Rucha Nimbalkar, 12/19/2024,Added label and text entry box for subject
# Rucha Nimbalkar, 12/19/2024,Added label for message
# Rucha Nimbalkar, 12/19/2024,Added a multi line text entry box for message
# Rucha Nimbalkar, 12/19/2024,Added a submit button to the form
# -------------------------------------------------------------------------------------------------- #

import tkinter as tk

application_window = tk.Tk() #creates a root node
application_window.geometry("600x200") #Define the size of the window
application_window.title("Contact Form")#Adds a title to the Window

#Create a label object 'First Name' in the Window and add it to the grid container
first_name_label = tk.Label(application_window, text = "First Name")
first_name_label.grid(row=1, column=1, sticky=tk.NW, padx=10, pady=5)

# Create a text entry window for first name
first_name_text = tk.Entry(application_window, width=16)
first_name_text.grid(row=1, column=2)

#Create a label object 'Last Name' in the Window and add it to the grid container
last_name_label = tk.Label(application_window, text = "Last Name")
last_name_label.grid(row=1, column=4, sticky=tk.NW, padx=10, pady=5)

# Create a text entry window for last name
last_name_text = tk.Entry(application_window, width=16)
last_name_text.grid(row=1, column=5)

#Create a label object 'Subject' in the Window and add it to the grid container
subject_label = tk.Label(application_window, text = "Subject")
subject_label.grid(row=4, column=1, sticky=tk.NW, padx=10, pady=5)

# Create a text entry window for subject
subject_text = tk.Entry(application_window, width=32)
subject_text.grid(row=4, column=2)

#Create a label object 'Message' in the Window and add it to the grid container
message_label = tk.Label(application_window, text = "Message")
message_label.grid(row=5, column=1, sticky=tk.NW, padx=10, pady=5)

multi_line_message = tk.Text(width=50, height=5)
multi_line_message.grid(row=5,
                 column=2,
                 sticky=tk.N,
                 columnspan=4,
                 padx=10,
                 pady=10
                 )

# Create a submit button and add it to a grid container
submit_button = tk.Button(application_window, text="Submit", width=6)
submit_button.grid(row=6, column=5, sticky=tk.NW, padx=5, pady=5)

application_window.mainloop() #displays window UI