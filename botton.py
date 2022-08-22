

from sqlite3 import Row
import tkinter as tk
from tkinter.tix import COLUMN
from tkinter.ttk import Label
from tkinter.ttk import Button



root = tk.Tk()
root.title("Hola mundo")
l = Label(root, text='Hola mundo')
def click():
    l.Pack()

btn = Button(root, text='Clickckeame', command=click, fg='#FFFF00', bg= 'blue' )
btn.pack()

root.mainloop()