from logging import root
from tkinter import *

root = Tk()
root.title("hola mundo")

exit = Button(root, text='salir', command=root.quit)
exit.pack()

root.mainloop()