import helpers 
import database

def iniciar():
    while True:
        helpers.limpiar_pantalla()

        print('BIENVENIDO AL GESTOR')
        print('='.center(50, '='))
        print('1. Listar clientes')
        print('2. Buscar cliente')
        print('3. Añadir cliente')
        print('4. Modificar cliente')
        print('5. Borrar cliente')
        print('6. Cerrar el gestor')
        print('='.center(50, '='))

        opcion = input('> ')
        helpers.limpiar_pantalla()

        if opcion == '1':
            print('Listando clientes...\n')
            for cliente in database.Clientes.lista:
                print(cliente)

        if opcion == '2':
            print('Buscando un cliente...\n')
            dni = helpers.leer_texto(9, 9, 'DNI 8 núneros y 1 letra').upper()
            cliente = database.Clientes.buscar(dni)
            if cliente:
                print(cliente)
            else:
                print('Cliente no encontado')

        if opcion == '3':
            print('Añadiendo un cliente...\n')
            dni = None
            while True:
                dni = helpers.leer_texto(9, 9, 'DNI 8 núneros y 1 letra').upper()
                if helpers.dni_valido(dni, database.Clientes.lista):
                    break
            
            nombre = helpers.leer_texto(1, 30, 'Nombre del cliente').capitalize()
            apellido = helpers.leer_texto(1, 30, 'Apellido del cliente').capitalize()
            telefono = helpers.leer_texto(9, 9, 'Telefono del cliente')

            database.Clientes.crear(dni, nombre, apellido, telefono)

        if opcion == '4':
            print('Modificando un cliente...\n')
            dni = helpers.leer_texto(9, 9, 'DNI 8 núneros y 1 letra').upper()
            cliente = database.Clientes.buscar(dni)

            if cliente:
                nombre = helpers.leer_texto(2, 30, f"Nombre (de 2 a 30 chars) [{cliente.nombre}]").capitalize()
                apellido = helpers.leer_texto(2, 30, f"Apellido (de 2 a 30 chars) [{cliente.apellido}]").capitalize()
                telefono = helpers.leer_texto(9, 9, f"Teléfono (9 digitos) [{cliente.telefono}]")
                database.Clientes.modificar(cliente.dni, nombre, apellido, telefono)
                print("Cliente modificado correctamente.")
            else:
                print('Cliente no encontrado.')

        if opcion == '5':
            print('Borrando un cliente...\n')
            dni = helpers.leer_texto(9, 9, 'DNI 8 núneros y 1 letra').upper() 
            if database.Clientes.borrar(dni):
                print('Cliente borrado correctamente')
            else:
                print('Cliente no encontrado') 

        if opcion == '6':
            print('Cerrando el gestor...')
            break;
        
    
        input("\nPresiona ENTER para continuar...")



