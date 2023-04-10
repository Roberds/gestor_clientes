#Interfaz de usuario
import database
import helpers
from tkinter import *
from tkinter import ttk #widgets extendidos
from tkinter.messagebox import askokcancel, WARNING

   
class CenterWidgetMixin():
    def center(self):
        self.update()
        w = self.winfo_width()
        h = self.winfo_height()
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        x = int(ws/2 - w/2)
        y = int(hs/2 - h/2)
        #self.geometry('WIDTHxHEIGTH+OFFSET_X+OFFSET_Y')
        self.geometry(f'{w}x{h}+{x}+{y}')

#Ventana de creacion del cliente
#Toplevel widget de manejo de subventanas
class CreateClientWindow(Toplevel, CenterWidgetMixin):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Crear cliente')
        self.build()
        self.center()
        #estos dos metodos bloquearan que podamos ir a la ventana principal sin cerrar la subventana
        self.transient(parent)
        self.grab_set()
    
    def build(self):
        frame = Frame(self)
        frame.pack(padx=20, pady=10)

        Label(frame, text='DNI (8 números 1 letra mayúscula)').grid(row=0, column=0)
        Label(frame, text='Nombre (de 2 a 30 caracteres)').grid(row=0, column=1)
        Label(frame, text='Apellido (de 2 a 30 caracteres)').grid(row=0, column=2)
        Label(frame, text='Teléfono (9 digitos)').grid(row=0, column=3)

        #campos de texto y validaciones
        dni = Entry(frame)
        dni.grid(row=1, column=0)
        dni.bind('<KeyRelease>', lambda event: self.validate(event, 0))

        nombre = Entry(frame)
        nombre.grid(row=1, column=1)
        nombre.bind('<KeyRelease>', lambda event: self.validate(event, 1))

        apellido = Entry(frame)
        apellido.grid(row=1, column=2)
        apellido.bind('<KeyRelease>', lambda event: self.validate(event, 2))

        telefono = Entry(frame)
        telefono.grid(row=1, column=3)
        telefono.bind('<KeyRelease>', lambda event: self.validate(event, 3))

        frame = Frame(self)
        frame.pack(pady=10)

        crear = Button(frame, text='Crear', command=self.create_client)
        crear.configure(state=DISABLED)
        crear.grid(row=0, column=0)

        Button(frame, text='Cancelar', command=self.close).grid(row=0, column=1)

        #Lista para validar y que se active el botón crear 
        self.validaciones = [False, False, False, False]
        self.crear = crear
        #exportamos para podder acceder a ellos en create client
        self.dni = dni
        self.nombre = nombre
        self.apellido =apellido
        self.telefono = telefono
        


    def create_client(self):
        self.master.treeview.insert(
            parent='', index='end', iid=self.dni.get(),
            values=(self.dni.get(), self.nombre.get(), self.apellido.get(), self.telefono.get()))
        #Creamos el cliente tambien en el fichero
        database.Clientes.crear(self.dni.get(), self.nombre.get(), self.apellido.get(), self.telefono.get())
        self.close()

    def close(self):
        self.destroy()
        self.update()

    def validate(self, event, index):
        valor = event.widget.get() #recuperar el valor del widget
        if index == 0:
            valido = helpers.dni_valido(valor, database.Clientes.lista)
            if valido: 
                event.widget.configure({'bg':'lawn green'})
            else:
                event.widget.configure({'bg':'red'})

        if index == 1:
            valido = valor.isalpha() and len(valor) >= 2 and len(valor) <= 30
            if valido: 
                event.widget.configure({'bg':'lawn green'})
            else:
                event.widget.configure({'bg':'red'})

        if index == 2:
            valido = valor.isalpha() and len(valor) >= 2 and len(valor) <= 30
            if valido: 
                event.widget.configure({'bg':'lawn green'})
            else:
                event.widget.configure({'bg':'red'})

        if index == 3:
            valido = valor.isdigit() and len(valor) == 9
            if valido: 
                event.widget.configure({'bg':'lawn green'})
            else:
                event.widget.configure({'bg':'red'})

        #Cambiar el estado del botón en base a las validaciones
        self.validaciones[index] = valido
        self.crear.config(state=NORMAL if self.validaciones == [True, True, True, True] else DISABLED)


#Ventana de modificación del cliente
class EditClientWindow(Toplevel, CenterWidgetMixin):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Modificar cliente')
        self.build()
        self.center()
        #estos dos metodos bloquearan que podamos ir a la ventana principal sin cerrar la subventana
        self.transient(parent)
        self.grab_set()


    def build(self):
        frame = Frame(self)
        frame.pack(padx=20, pady=10)

        Label(frame, text='DNI (No modificable)').grid(row=0, column=0)
        Label(frame, text='Nombre (de 2 a 30 caracteres)').grid(row=0, column=1)
        Label(frame, text='Apellido (de 2 a 30 caracteres)').grid(row=0, column=2)
        Label(frame, text='Teléfono (9 digitos)').grid(row=0, column=3)

        #campos de texto y validaciones
        dni = Entry(frame)
        dni.grid(row=1, column=0)
        dni.bind('<KeyRelease>', lambda event: self.validate(event, 0))

        nombre = Entry(frame)
        nombre.grid(row=1, column=1)
        nombre.bind('<KeyRelease>', lambda event: self.validate(event, 1))

        apellido = Entry(frame)
        apellido.grid(row=1, column=2)
        apellido.bind('<KeyRelease>', lambda event: self.validate(event, 2))

        telefono = Entry(frame)
        telefono.grid(row=1, column=3)
        telefono.bind('<KeyRelease>', lambda event: self.validate(event, 3))

        #establecer entradas valores iniciales
        cliente = self.master.treeview.focus()
        campos = self.master.treeview.item(cliente, 'values')
        dni.insert(0, campos[0])
        dni.config(state=DISABLED)
        nombre.insert(0, campos[1])
        apellido.insert(0, campos[2])
        telefono.insert(0, campos[3])

        frame = Frame(self)
        frame.pack(pady=10)

        actualizar  = Button(frame, text='Crear', command=self.edit_client)
        actualizar .grid(row=0, column=0)

        Button(frame, text='Cancelar', command=self.close).grid(row=0, column=1)

        #Lista para validar y que se active el botón crear 
        self.validaciones = [False, False, False, False]
        self.actualizar = actualizar
        #exportamos para podder acceder a ellos en create client
        self.dni = dni
        self.nombre = nombre
        self.apellido =apellido
        self.telefono = telefono

    def edit_client(self):
        #accedemos al cliente seleccionado
        cliente = self.master.treeview.focus()
        self.master.treeview.item(
        cliente, values=(self.dni.get(), self.nombre.get(), self.apellido.get()))
        #Moficamos el cliente tambien en el fichero
        database.Clientes.modificar(self.dni.get(), self.nombre.get(), self.apellido.get(), self.telefono.get())
        self.close()


    def close(self):
        self.destroy()
        self.update()

    def validate(self, event, index):
        valor = event.widget.get() #recuperar el valor del widget
        if index == 0:
            valido = helpers.dni_valido(valor, database.Clientes.lista)
            if valido: 
                event.widget.configure({'bg':'lawn green'})
            else:
                event.widget.configure({'bg':'red'})

        if index == 1:
            valido = valor.isalpha() and len(valor) >= 2 and len(valor) <= 30
            if valido: 
                event.widget.configure({'bg':'lawn green'})
            else:
                event.widget.configure({'bg':'red'})

        if index == 2:
            valido = valor.isalpha() and len(valor) >= 2 and len(valor) <= 30
            if valido: 
                event.widget.configure({'bg':'lawn green'})
            else:
                event.widget.configure({'bg':'red'})

        if index == 3:
            valido = valor.isdigit() and len(valor) == 9
            if valido: 
                event.widget.configure({'bg':'lawn green'})
            else:
                event.widget.configure({'bg':'red'})

        #Cambiar el estado del botón en base a las validaciones
        self.validaciones[index] = valido
        self.actualizar.config(state=NORMAL if self.validaciones == [True, True, True, True] else DISABLED)

    
#App principal
class App(Tk, CenterWidgetMixin):
    def __init__(self):
        super().__init__()
        self.title('Gestor de clientes')
        self.build()
        self.center()
        
    
    def build(self): #construcción de la interfaz
        frame = Frame(self)
        frame.pack()

        #columnas
        treeview = ttk.Treeview(frame)
        treeview['columns'] = ('DNI', 'Nombre', 'Apellido', 'Teléfono')

        treeview.column('#0', width=0, stretch=NO) #Para que no se vea la columna que genera por defecto
        treeview.column('DNI', anchor=CENTER)
        treeview.column('Nombre', anchor=CENTER)
        treeview.column('Apellido', anchor=CENTER)
        treeview.column('Teléfono', anchor=CENTER)

        #Cabeceras
        treeview.heading('DNI', text='DNI', anchor=CENTER)
        treeview.heading('Nombre', text='Nombre', anchor=CENTER)
        treeview.heading('Apellido', text='Apellido', anchor=CENTER)
        treeview.heading('Teléfono', text='Teléfono', anchor=CENTER)


        #Añadimos los clientes al treeview
        for cliente in database.Clientes.lista:
            treeview.insert(
                parent='', index='end', iid=cliente.dni,
                values=(cliente.dni, cliente.nombre, cliente.apellido, cliente.telefono))
            
        #Barra de desplazamiento
        scrollbar = Scrollbar(frame)
        scrollbar.pack(side=RIGHT, fill=Y)

        treeview['yscrollcommand'] = scrollbar.set
        scrollbar.config(command=treeview.yview)

        treeview.pack()

        #Botones
        frame = Frame(self)
        frame.pack(pady=20)

    

        Button(frame, text='Crear', command=self.create).grid(row=0, column=0)
        Button(frame, text='Modificar', command=self.updated).grid(row=0, column=1)
        Button(frame, text='Borrar', command=self.delete).grid(row=0, column=2)


        self.treeview = treeview #para acceder a su info desde otros metodos lo exportamos como atributo de instancia
    
    #Metodo de borrado
    def delete(self):
        cliente = self.treeview.focus()
        if cliente:
            campos = self.treeview.item(cliente, 'values')
            confirmar = askokcancel(
                title='Confirmar borrado',
                message=f'¿Borrar {campos[1]} {campos[2]}?',
                icon=WARNING
            )
            if confirmar:
                self.treeview.delete(cliente)
                #Borramos tambien del fichero
                database.Clientes.borrar(campos[0])

    #Metodo de creación de cliente
    def create(self):
        CreateClientWindow(self)

    #Metodo de mpdoficación de cliente
    def updated(self):
        EditClientWindow(self)
