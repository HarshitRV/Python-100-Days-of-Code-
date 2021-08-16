from tkinter import Tk, Label, font

window = Tk()
window.title("TK Window")
window.minsize(width=500, height=300)

#Label
label = Label(text="A Label", font=("Arial", 24, "bold"))
label.pack() #Places label into the screen and centers it









window.mainloop()