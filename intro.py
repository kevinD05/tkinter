
from sqlite3 import Row
import tkinter as tk
from tkinter.tix import COLUMN
from tkinter.ttk import Label


root = tk.Tk()
root.title("Hola mundo")
root.geometry('500x500')
l1 = Label(root, text ="Hola mundo mi primera etiqueta")
l2 = Label(root, text ="Hola mundo mi primera etiqueta")
l1.grid(row=0, column=0)
l2.grid(row=1, column=1)
root.mainloop()