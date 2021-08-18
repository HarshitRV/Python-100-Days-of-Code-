from tkinter import Tk, Label, Button, Entry

window = Tk()
window.title("TK Window")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20) #Changes the padding

def on_click():
    label.config(text=input.get())

#Label
label = Label(text="A Label", font=("Arial", 14, "bold"))
label.config(text="New Text") #Changes the initial text
label.grid(row=0, column=0) #Places label into the screen and centers it

#Button
button = Button(text="Click", command=on_click)
button.grid(row=1, column=1)

#New Button
button_new = Button(text="Click", command=on_click)
button_new.grid(row=0, column=2)

#Entry
input = Entry(width=20)
input.get() #return the input as string
input.grid(row=2, column=3)

window.mainloop()