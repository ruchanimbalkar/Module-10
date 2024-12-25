# ----------------------------------------------------------------------------- #
# Title: Module 10 - Creating a Christmas Calendar
# # Description: Creates the UI object showing various images on the grid
# ChangeLog: (Who, When, What)
# Rucha Nimbalkar, 12/24/2024,Created Script
# Rucha Nimbalkar, 12/24/2024,Added title
# Rucha Nimbalkar, 12/24/2024,Added images reference using tkinter
# Rucha Nimbalkar, 12/24/2024,Added images to the grid
# ------------------------------------------------------------------------------ #
import tkinter as tk
application_window = tk.Tk() #creates a root node
application_window.geometry("855x600")
application_window.title("Christmas Calendar")
application_window.config(bg="lightblue")

image = tk.PhotoImage(file="1.png")
large_img = image.subsample(4,4)

img = tk.Label(application_window, image=large_img)
img.grid(row=1, column=1, rowspan=6, padx=5, pady=5)

image_2 = tk.PhotoImage(file="2.png")
large_img_2 = image_2.subsample(4,4)

img_2 = tk.Label(application_window, image=large_img_2)
img_2.grid(row=1, column=2, rowspan=6, padx=5, pady=5)

image_3 = tk.PhotoImage(file="3.png")
large_img_3 = image_3.subsample(4,4)

img_3 = tk.Label(application_window, image=large_img_3)
img_3.grid(row=1, column=3, rowspan=6, padx=5, pady=5)

image_4 = tk.PhotoImage(file="4.png")
large_img_4 = image_4.subsample(4,4)

img_4 = tk.Label(application_window, image=large_img_4)
img_4.grid(row=1, column=4, rowspan=6, padx=5, pady=5)

image_5 = tk.PhotoImage(file="5.png")
large_img_5 = image_5.subsample(4,4)

img_5 = tk.Label(application_window, image=large_img_5)
img_5.grid(row=1, column=5, rowspan=6, padx=5, pady=5)


image_6 = tk.PhotoImage(file="6.png")
large_img_6 = image_6.subsample(4,4)

img_6 = tk.Label(application_window, image=large_img_6)
img_6.grid(row=1, column=6, rowspan=6, padx=5, pady=5)

image_7 = tk.PhotoImage(file="7.png")
large_img_7 = image_7.subsample(4,4)

img_7 = tk.Label(application_window, image=large_img_7)
img_7.grid(row=7, column=1, rowspan=6, padx=5, pady=5)


image_8 = tk.PhotoImage(file="8.png")
large_img_8 = image_8.subsample(3,3)

img_8 = tk.Label(application_window, image=large_img_8)
img_8.grid(row=7, column=2, rowspan=6, padx=5, pady=5)


image_9 = tk.PhotoImage(file="9.png")
large_img_9 = image_9.subsample(4,4)

img_9 = tk.Label(application_window, image=large_img_9)
img_9.grid(row=7, column=3, rowspan=6, padx=5, pady=5)


image_10 = tk.PhotoImage(file="10.png")
large_img_10 = image_10.subsample(4,4)

img_10 = tk.Label(application_window, image=large_img_10)
img_10.grid(row=7, column=4, rowspan=6, padx=5, pady=5)


image_11 = tk.PhotoImage(file="11.png")
large_img_11 = image_11.subsample(4,4)

img_11 = tk.Label(application_window, image=large_img_11)
img_11.grid(row=7, column=5, rowspan=6, padx=5, pady=5)


image_12 = tk.PhotoImage(file="12.png")
large_img_12 = image_12.subsample(4,4)

img_12 = tk.Label(application_window, image=large_img_12)
img_12.grid(row=7, column=6, rowspan=6, padx=5, pady=5)


image_13 = tk.PhotoImage(file="13.png")
large_img_13 = image_13.subsample(4,4)

img_13 = tk.Label(application_window, image=large_img_13)
img_13.grid(row=13, column=1, rowspan=6, padx=5, pady=5)


image_14 = tk.PhotoImage(file="14.png")
large_img_14 = image_14.subsample(3,3)

img_14 = tk.Label(application_window, image=large_img_14)
img_14.grid(row=13, column=2, rowspan=6, padx=5, pady=5)


image_15 = tk.PhotoImage(file="15.png")
large_img_15 = image_15.subsample(4,4)

img_15 = tk.Label(application_window, image=large_img_15)
img_15.grid(row=13, column=3, rowspan=6, padx=5, pady=5)


image_16 = tk.PhotoImage(file="16.png")
large_img_16 = image_16.subsample(4,4)

img_16 = tk.Label(application_window, image=large_img_16)
img_16.grid(row=13, column=4, rowspan=6, padx=5, pady=5)


image_17 = tk.PhotoImage(file="17.png")
large_img_17 = image_17.subsample(4,4)

img_17 = tk.Label(application_window, image=large_img_17)
img_17.grid(row=13, column=5, rowspan=6, padx=5, pady=5)


image_18 = tk.PhotoImage(file="18.png")
large_img_18 = image_18.subsample(4,4)

img_18 = tk.Label(application_window, image=large_img_18)
img_18.grid(row=13, column=6, rowspan=6, padx=5, pady=5)


image_19 = tk.PhotoImage(file="19.png")
large_img_19 = image_19.subsample(4,4)

img_19 = tk.Label(application_window, image=large_img_19)
img_19.grid(row=19, column=1, rowspan=6, padx=5, pady=5)


image_20 = tk.PhotoImage(file="20.png")
large_img_20 = image_20.subsample(4,4)

img_20 = tk.Label(application_window, image=large_img_20)
img_20.grid(row=19, column=2, rowspan=6, padx=5, pady=5)


image_21 = tk.PhotoImage(file="21.png")
large_img_21 = image_21.subsample(4,4)

img_21 = tk.Label(application_window, image=large_img_21)
img_21.grid(row=20, column=3, rowspan=6, padx=5, pady=5)


image_22 = tk.PhotoImage(file="22.png")
large_img_22 = image_22.subsample(4,4)

img_22 = tk.Label(application_window, image=large_img_22)
img_22.grid(row=20, column=4, rowspan=6, padx=5, pady=5)


image_23 = tk.PhotoImage(file="23.png")
large_img_23 = image_23.subsample(4,4)

img_23 = tk.Label(application_window, image=large_img_23)
img_23.grid(row=20, column=5, rowspan=6, padx=5, pady=5)


image_24 = tk.PhotoImage(file="24.png")
large_img_24 = image_24.subsample(4,4)

img_24 = tk.Label(application_window, image=large_img_24)
img_24.grid(row=20, column=6, rowspan=6, padx=5, pady=5)

application_window.mainloop() #displays window UI