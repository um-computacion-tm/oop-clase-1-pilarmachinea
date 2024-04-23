"""
Apuntes de clase:
self.__atributo__ = 0
solo para los atributos

variable = MiClase(par1, par2)
variable ----> referencia
MiClase(par1, par2) ----> objeto

NombreDeUnaClase
nombre_de_una_variable
"""

class Persona: 
    def __init__(self, nombre: str = "Jhon", apellido: str = "Doe", du: int = "123456"):
        self.__nombre__ = nombre
        self.__apellido__ = apellido
        self.__du__ = du
    
    def mostrar_datos(self):
        print(f'Mis datos son nombre = {self.__nombre__} apellido = {self.__apellido__} documento = {self.__du__}')