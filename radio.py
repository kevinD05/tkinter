from cProfile import label
from logging import root
from re import L
from tkinter import *

root = Tk()
root.title('hola mundo')

r = IntVar()
r.set('2')

CHANCHITO =[
    ('feliz','feliz'),
    ('triste','triste'),
    ('amargado','amargado')
]

#Radiobutton(root, text='opcion 1', variable=r, value=1).pack()
#Radiobutton(root, text='opcion 2', variable=r, value=2).pack()

L =label(root, textvariable=r)
L.Pack()

root.mainloop()