
class Cliente():

    def __init__(self, dni, nombre, apellido, telefono):
        self._dni = dni
        self._nombre = nombre
        self._apellido = apellido
        self._telefono = telefono

    @property
    def dni(self):
        return self._dni
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    
    @property
    def apellido(self):
        return self._apellido
    
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido
    
    @property
    def telefono(self):
        return self._telefono
    
    @telefono.setter
    def telefono(self, telefono):
        self._telefono = telefono

    
    def __str__(self):
        return f'DNI: {self._dni}   Nombre: {self._nombre} {self._apellido}   Teléfono: {self._telefono}'
    


class Clientes:

    lista = [
        Cliente('50309624W', 'Roberto', 'Díaz', 666666687),
        Cliente('33596246T', 'Manolo', 'López', 6645631234),
        Cliente('20359624J', 'Ana', 'García', 664563234)
    ]

    @staticmethod
    def buscar(dni):
        for cliente in Clientes.lista:
            if cliente.dni == dni:
                return cliente
            
    @staticmethod
    def crear(dni, nombre, apellido, telefono):
        cliente = Cliente(dni, nombre, apellido, telefono)
        Clientes.lista.append(cliente)
        return cliente


    @staticmethod
    def modificar(dni, nombre, apellido, telefono):
        for i, cliente in enumerate(Clientes.lista):
            if cliente.dni == dni:
                Clientes.lista[i].nombre = nombre
                Clientes.lista[i].apellido = apellido
                Clientes.lista[i].telefono = telefono
                return Clientes.lista[i]


    @staticmethod
    def borrar(dni):
        for i, cliente in enumerate(Clientes.lista):
            if cliente.dni == dni:
                cliente = Clientes.lista.pop(i)
                return cliente
        

    
