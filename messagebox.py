from gettext import bind_textdomain_codeset
from logging import root
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('hola mundo')

#def click():
   # messagebox.showwarning('popup','Hola mundo')

#def click():
    #messagebox.showinfo('popup','Hola mundo')

#def click():
 #   messagebox.showerror('popup','Hola mundo')

def click():
     repuesta = messagebox.askquestion('popup','Hola mundo :(' )
     if repuesta == 'yes':
        messagebox.showinfo('respuesta','La respuesta fue'+ repuesta)
     else:
        messagebox.showinfo('repuesta', 'la repuesta fue'+ repuesta)

btn = Button(root, text="presioname", command=click)
btn.pack()

root.mainloop()