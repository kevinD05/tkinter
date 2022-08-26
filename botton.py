from tkinter import *


root = Tk()
root.title("Hola mundo")
l = Label(root, text='Hola mundo')
def click():
    l.Pack()

btn = Button(root, text='Clickckeame', command=click, fg='#FFFF00', bg= 'blue' )
btn.pack()

root.mainloop()