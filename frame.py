from tkinter import *

root = Tk()
root.title('Hola mundo')

Frame = LabelFrame(root, text='login', padx=10, pady=10, borderwidth=10)
Frame.pack()

l = Label(Frame, text='Estoy dentro un frame')
btn = Button(Frame, text='salir', command=root.quit)
l.pack()
btn.pack()

root.mainloop()