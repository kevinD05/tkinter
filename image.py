from cProfile import label
from email.mime import image
from logging import root
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Hola mundo')

image = ImageTk.PhotoImage(image.open('one piece.jpg'))
l = label(image=img)
l.pack()

root.mainloop()
