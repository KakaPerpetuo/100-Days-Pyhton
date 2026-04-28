from tkinter import *

# Window
my_window = Tk()
my_window.title("Challenge 1")
my_window.minsize(width=500, height=300)
# padx, pady = margens - espaco entre o programa
my_window.config(padx=20, pady=20)

# Label
my_label = Label(text="Label", font=("Arial", 24, "bold"))
my_label.grid(column=1, row=1)

# Button
def button_clicked():
    print("I got clicked")
my_button = Button(text="Click Me", command=button_clicked)
my_button.grid(column=2, row=2)

new_button = Button(text="Click me two", command=button_clicked)
new_button.grid(column=3, row=1)

# Entry
input = Entry()
input.insert(0, string="Text")
input.grid(column=4, row=3)

my_window.mainloop()