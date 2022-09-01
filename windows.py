from cProfile import label
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("hello word")

#solucion 1
#def open():
   # img =ImageTk.PhotoImage(Image.open('one piece.jpg'))
    #top = Toplevel()
    #top.title('hello word, new windows')
    #l = Label(top, text="i am text in the second windows")
    #l2 = Label(top, image=img)
    #l.pack()
    #l2.pack()
    #top.mainloop()


def open():
    global img
    img =ImageTk.PhotoImage(Image.open('one piece.jpg'))
    top = Toplevel()
    top.title('hello word, new windows')
    l = Label(top, text="i am text in the second windows")
    l2 = Label(top, image=img)
    l.pack()
    l2.pack()
    top.mainloop()

btn = Button(root, text='click', command=open).pack()

root.mainloop()