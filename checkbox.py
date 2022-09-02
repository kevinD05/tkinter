from logging import root
from tkinter import *
import tkinter

root = Tk()
root.title('Hola mundo')

root.geometry('500x500')

var = StringVar()
var.set('Kevin diaz')

def mostrar():
    l = Label(root,text=var.get())
    l.pack()

c = Checkbutton(root, text='soy un checkbox', variable=var, onvalue='si', offvalue='Kevin diaz')
c.pack()

btn = Button(root, text='click', command=mostrar)
btn.pack()

root,mainloop()