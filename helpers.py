import re #Expresiones regulares
import os #Funciones del sistema operativo
import platform #Identificar el sistema operativo

#Funcion para limpar la terminal
def limpiar_pantalla():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')


#Función para leer texto
def leer_texto(min=0, max=100, mensaje=None):
    print(mensaje) if mensaje else None
    while True:
        texto = input('> ')
        if len(texto) >= min and len(texto) <= max:
            return texto


#Función dni válido
def dni_valido(dni, lista):
    if not re.match('[0-9]{8}[A-Z]$', dni):
        print('Formato de DNI incorrecto')
        return False
    for cliente in lista:
        if cliente.dni == dni:
            print('Cliente ya existente')
            return False
    return True
        
