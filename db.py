from logging import root
from tkinter import *
import sqlite3

root = Tk()
root.title('hola mundo: todo list')
root.geometry('500x500')

conn = sqlite3.connect('todo.db')

c = conn.cursor()

c.execute("""
     CREATE TABLE if is not exists todo(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        description TEXT NOT NULL,
        completed BOOLEAN NOT NULL
     );

""")

conn.commit()

l = Label(root, text='Tarea')
l.grid(row=0, column=0)

e = Entry(root, width=40)
e.grid(row=0, column=1)

btn = Button(root, text='agregar')
btn.grid(row=0, column=2)

frame = LabelFrame(root, text='mis tareas', padx=5, pady=5)
frame.grid(row=1, column=0, columnspan=3, sticky='nswe', padx=5)

root.mainloop()