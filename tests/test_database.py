import copy
import unittest
import database as db

#Ejecutar pruebas en terminal con pytest -v

class TestDatabase(unittest.TestCase):

    def setUp(self):
        # Se ejecuta antes de cada prueba
        db.Clientes.lista = [
            db.Cliente('71359324W', 'Roberto', 'Díaz', 666666687),
            db.Cliente('33596246T', 'Manolo', 'López', 6645631234),
            db.Cliente('20359624J', 'Ana', 'García', 664563234)
        ]


    def test_buscar_cliente(self):
        cliente_existente = db.Clientes.buscar('71359324W')
        cliente_no_existente = db.Clientes.buscar('99999999X')
        self.assertIsNotNone(cliente_existente)
        self.assertIsNone(cliente_no_existente)

    def test_crear_cliente(self):
        nuevo_cliente = db.Clientes.crear('39232321X', 'Luis', 'Ruiz', 634232456)
        self.assertEqual(len(db.Clientes.lista), 4)
        self.assertEqual(nuevo_cliente.dni, '39232321X')
        self.assertEqual(nuevo_cliente.nombre, 'Luis')
        self.assertEqual(nuevo_cliente.apellido, 'Ruiz')
        self.assertEqual(nuevo_cliente.telefono, 634232456)

    def test_modificar_cliente(self):
        cliente_a_modificar = copy.copy(db.Clientes.buscar('33596246T'))
        cliente_modificado = db.Clientes.modificar('33596246T', 'Mariana', 'Pérez', 653234678)
        self.assertEqual(cliente_a_modificar.nombre, 'Manolo')
        self.assertEqual(cliente_modificado.nombre, 'Mariana')

    def test_borrar_cliente(self):
        cliente_borrado = db.Clientes.borrar('33596246T')
        cliente_rebuscado = db.Clientes.buscar('33596246T')
        self.assertNotEqual(cliente_borrado, cliente_rebuscado)


if __name__ == '__main__':
    unittest.main()