from tkinter import *

root = Tk()
root.title('hola mundo')
root.geometry('500x500')

def enviar():
    l = Label(root, text=value.get())
    l.pack()

lista = [
    'ZEUS'
    'KIRA'
    'CHESTER'
]

value = StringVar()
value.set(lista[1])

drop = OptionMenu(root, value, *lista)
drop.pack()

btn = Button(root, text='enviar', command=enviar)
btn.pack()

root.mainloop()