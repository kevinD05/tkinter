from cProfile import label
from calendar import c
from email.mime import image
import imghdr
from logging import root
from sqlite3 import Row
from tkinter import *
from tkinter.tix import COLUMN
from PIL import Image, ImageTk

root = Tk()
root.title('Carrusel')

img1 = ImageTk.PhotoImage(Image.open('images/1.png'))
img2 = ImageTk.PhotoImage(Image.open('images/2.png'))
img3 = ImageTk.PhotoImage(Image.open('images/3.png'))

lista = [img1,img2,img3]


l = label(root, image=img1)
l.grid(Row=0,COLUMN=0, columspan=3)

def adelante(img_num):
    global l
    global btn_atras
    global btn_adelante

    l.grid_forget()
    l = label(root, image=lista[img_num])
    btn_atras = Button(root, text="<-", command=lambda: atras(img_num - 1))
    btn_adelante = Button(root, text='->', command=lambda: adelante(img_num + 1))
    
    if img_num == 3:
        btn_adelante = Button(root, text='N/A', state=DISABLED)

    l.grid(Row=0, COLUMN=0, columspan=3)
    btn_atras.grid(row=1, column=0)
    btn_adelante.grid(row=1, column=2)

def atras():
    global l
    global btn_atras
    global btn_adelante

    l.grid_forget()
    l = Label(root, image=lista[img_num])
    btn_atras = Button(root, text="<-", command=lambda: atras(img_num - 1))
    btn_adelante = Button(root, text='->', command=lambda: adelante(img_num + 1))
    
    if img_num == 0:
        btn_atras = Button(root, text='N/A', state=DISABLED)

    l.grid(Row=0, COLUMN=0, columspan=3)
    btn_atras.grid(row=1, column=0)
    btn_adelante.grid(row=1, column=2)





btn_atras = Button(root,text='N/A',state=DISABLED)
btn_adelante = Button(root, text='->', command=lambda: adelante(1))

btn_atras.grid(row=1, column=0)
btn_adelante.grid(row=1, column=2)

root.mainloop()