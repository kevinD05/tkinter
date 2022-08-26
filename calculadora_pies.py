from cProfile import label
from distutils.log import ERROR
from importlib.metadata import entry_points
from logging import root
from mimetypes import init
from multiprocessing.sharedctypes import Value
from pickle import FRAME
from sqlite3 import Row
from tkinter import *

root = Tk()
root.title('Pies a metro')

def calcular():
    try:
        Value = float(pies.get())
        m = int(0.3048 * Value * 10000 + 0.5)/10000
        metros.set(m)
    except ValueError:
        metros.set('ERROR')

Frame = Frame(root, pady=3, padx=3)
Frame.grid(column=0, row=0)

pies = StringVar()
pies_input = Entry(Frame, width=7, textvariable=pies)
pies_input.grid(column=1, row=0)

metros = StringVar()
Label(Frame, textvariable=metros).grid(column=1, row=1)

Button(Frame, text='calcular', command=calcular).grid(column=2, row=2)

Label(Frame, text='pies').grid(column=0, row=0)
Label(Frame, text='es igual a').grid(column=0, row=1)
Label(Frame, text='metros').grid(column=2, row=1)

pies_input.focus()
root.bind("<Return>", calcular)
root.mainloop()