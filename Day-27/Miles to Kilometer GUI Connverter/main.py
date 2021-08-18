from tkinter import *

window = Tk()
window.minsize(height=85, width=250)

def on_click():
    miles = input.get()
    km = int(miles) * 1.60934
    label_3.config(text=km)

input = Entry()
input.grid(row=0,column=1)

label = Label(text="Miles", font=("Arial", 10, "bold"))
label.grid(row=0, column=2)

label_2 = Label(text="is equal to", font=("Arial", 10, "bold"))
label_2.grid(row=1, column=0)

label_3 = Label(text="0", font=("Arial", 10, "bold"))
label_3.grid(row=1, column=1)

label_4 = Label(text="Km", font=("Arial", 10, "bold"))
label_4.grid(row=1, column=2)

button = Button(text="Click", command=on_click)
button.grid(row=2, column=1)

window.mainloop()