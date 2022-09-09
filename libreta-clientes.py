from tkinter import * 
from tkinter import ttk 
from tkinter import messagebox
import mysql.connector


root = Tk()
root.title('hola mundo: crm')

conn = mysql.connector.Connect('crm')

c = conn.cursor()

c.execute("""
         CREATE TABLE if no exists cliente (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            telefono TEXT NOT NULL,
            empresa TEXT NOT NULL
          );

""")


def render_Clientes():
    rows = c.execute('SELECT * FROM cliente').fetchall()

    for row in rows:
        tree.insert('', END, row[0], values=(row[1], row[2], row[3]))


def insertar():
    c.execute("""
            INSERT INTO cliente(nombre, telefono, empresa) VALUES (?, ?, ?)
    """, (Cliente['nombre'], Cliente['telfono'], Cliente['empresa']))
    conn.commit()
    render_Clientes()


def nuevo_cliente():
    def guardar():
        if not nombre.get():
            messagebox.showerror('Error', 'El nombre es obligatorio')
            return
        if not telefono.get():
            messagebox.showerror('Error', 'El telefono es obligatorio')
            return
          
        if not empresa.get():
            messagebox.showerror('Error', 'La empresa es obligatorio')
            return


        Cliente = {
            'nombre': nombre.get(),
            'telefono': telefono.get(),
            'empresa': empresa.get()
        }
        insertar(Cliente)
        top.destroy()


    top = Toplevel
    
    top.title('nuevo cliente')

    lnombre = Label(top, text='nombre')
    nombre = Entry(top, width=40)
    lnombre.grid(row=0, column=0)
    nombre.grid(row=0, column=1)

    ltelefono = Label(top, text='telefono')
    telefono = Entry(top, width=40)
    ltelefono.grid(row=1, column=0)
    telefono.grid(row=1, column=1)

    lempresa = Label(top, text='empresa')
    empresa = Entry(top, width=40)
    lempresa.grid(row=2, column=0)
    empresa.grid(row=2, column=1)

    guardar = Button(top, text='guardar',command=guardar)
    guardar.grid(row=3, column=1)

def nuevo_cliente():
    pass

def eliminiar_cliente():
    id = tree.selection()[0]

    cliente = c.execute('SELECT * FROM cliente WHERE id = ?', (id, )).fetchone()
    repuesta = messagebox.askokcancel('Seguro?', 'Estas seguro de querer eliminar el cliente ?')
    if repuesta:
        c.execute('DELETE FROM cliente WHERE id = ?', (id, ))
        conn.commit()
        render_Clientes()
    else:
        pass


btn = Button(root, text='nuevo cliente', command=nuevo_cliente)
btn.grid(column=0, row=0)

btn_eliminar = Button(root, text='eliminar cliente', command=eliminiar_cliente)
btn_eliminar.grid(column=1, row=0 )

tree = ttk.Treeview(root)
tree['columns'] = ('nombre','telefono','empresa')
tree.column('#0',width=0, stretch=No)
tree.column('nombre')
tree.column('telefono')
tree.column('empresa')

tree.heading('nombre', text='nombre')
tree.heading('telefono', text='telefono')
tree.heading('empresa', text='empresa')
tree.heading(column=0, row=1, columnspan=2)

render_Clientes()

root.mainloop()
