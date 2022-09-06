from logging import root
from tkinter import *
from tkinter import ttk

root = Tk()
root.title('hola mundo: treeview')

tree = ttk.Treeview(root)
tree['columns'] = ('nombre','telefono','empresa',)

tree.column('#0')
tree.column('nombre')
tree.column('telefono')
tree.column('empresa')

tree.heading('#0',text=id)
tree.heading('nombre', text='nombre')
tree.heading('telefono', text='telefono')
tree.heading('empresa', text='empresa')

tree.grid(column=0, row=0)

tree.insert('',END,'lala', values=('uno','dos','tres'), text='chanchito feliz')
tree.insert('',END,'lele', values=('cuatro','cinco','seis'), text='chanchito triste')
tree.insert('lele',END,'lili', values=('4','5','6'), text='hijo')


root.mainloop()