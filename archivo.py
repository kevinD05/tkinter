from email.mime import image
from tkinter import *
from urllib import robotparser
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title('hola mundo: archivos')

root.filename = filedialog.askopenfile(title='elige una foto', filetypes=(('archivos PNG','*.png'),('todos','*')))
l = Label(root, text=root.filename)
l.pack()
img = Image.open(root.filename)
ImgTk = ImageTk(img)

l = Label(root, image=ImgTk)
l.pack()

root.mainloop()