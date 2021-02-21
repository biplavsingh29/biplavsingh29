from tkinter import *
from PIL import ImageTk, Image
 
root = Tk()
root.title("Checkbox program")
root.iconbitmap("C:/Users/lenovo/Desktop/python/img/Bunny.ico")
root.geometry("400x400")

def show():
    my_label = Label(root, text=var.get()).pack()


var = StringVar()

c = Checkbutton(root, text="Click Here", variable=var, onvalue="on", offvalue="off")
c.deselect()
c.pack()

my_button = Button(root, text="Show selection", command=show).pack()


root.mainloop()