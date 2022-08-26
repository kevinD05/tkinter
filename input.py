from cProfile import label
from cgitb import text
from logging import root
from struct import pack
from tkinter import *

root = Tk ()
root.title('hola mundo')
root.geometry('500x500')

e = Entry(root, width=60)
e.pack()

def click():
    texto = e.get()
    textvariable.set(texto)
    valor = textvariable.get()
    print(valor)
  #  l = label(root, text=texto)
  #  l = pack()
    e.delete(0, END)
    # l.configure(text = texto)

btn = Button(root, text='click', command=click)
btn.pack()

textvariable = StringVar()

l = label(root, textvariable=textvariable)
l.pack()

root.mainloop
