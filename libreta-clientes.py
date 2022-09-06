from logging import root
from sqlite3 import Row
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector

root = Tk()
root.title('hola mundo: crm')

conn = mysql.connector('crm.db')

c = conn.cursor()

c.execute("""
         CREATE TABLE if no existis cliente (
            id INTEGER PRIMARY KEY AUTOINCREMENTE
            nombre  TEXT NOT NULL,
            telefono  TEXT NOT NULL,
            empresa  TEXT NOT NULL,
          );

""")

def nuevo_cliente():
    pass

def eliminiar_cliente():
    pass


btn = Button(root, text='nuevo cliente', command=nuevo_cliente)
btn.grid(column=0, row=0)

btn_eliminar = Button(root, text='eliminar cliente', command=eliminiar_cliente)
btn_eliminar.grid(column=1, row=0 )
root.mainloop()