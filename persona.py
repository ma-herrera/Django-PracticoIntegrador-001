from cexception import *
from integrador1 import get_int

# class ErrorDeInicializacionDeAtributos(Exception):
#     """El valor asignado al atributo no es válido."""


""""
6. Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los
siguientes métodos para la clase:
• Un constructor, donde los datos pueden estar vacíos.
• Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos. (Para cumplir esta consigna hago una funcion de validacion)
• mostrar(): Muestra los datos de la persona.
• es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.
"""
# CONSTRUCTOR (los datos pueden estar vacíos)
class Persona():
    def __init__(self, nombre=None, edad=None, dni=None):
        self._nombre=nombre
        self._edad=edad
        self._dni=dni

    @property
    def nombre(self):
        return self._nombre

    @property
    def edad(self):
        return self._edad

    @property
    def dni(self):
        return self._dni

####################### SETTERS ############################

    @nombre.setter
    def nombre(self, nombre):
        try:
            self.validar_nombre(nombre)
        except ErrorDeInicializacionDeAtributos as e:
            print(e)
            raise
        else:
            self._nombre = nombre


    @edad.setter
    def edad(self, edad):
        try:
            self.validar_edad(edad)
        except ErrorDeInicializacionDeAtributos as e:
            print(e)
            raise
        except Exception as e:
            print(e)
            raise
        else:
            self._edad=edad


    @dni.setter
    def dni(self, dni):
        try:
            self.validar_dni(dni)
        except ErrorDeInicializacionDeAtributos as e:
            print(e)
            raise
        except Exception:
            print("DNI inválido")
            raise            
        else:
            self._dni = dni

#########################################################################

    def __str__ (self):
        return f'{self.nombre}, {self.edad} años, DNI {self.dni}'

    def mostrar(self):
        return f'{self.nombre}, {self.edad} años, DNI {self.dni}'
        # print(self)

    def es_mayor_de_edad(self):
        return self.edad > 18
    
######################### VALIDACION DE DATOS ###########################

    def validar_nombre(self, nombre):
        if (nombre is None):
            raise ErrorDeInicializacionDeAtributos("El nombre no puede ser nulo")
        elif (len(nombre.strip())==0):
            raise ErrorDeInicializacionDeAtributos("El nombre no puede ser una cadena vacía")

# que no sea nulo, que sea un entero y que sea >0
    def validar_edad(self, edad):
        if (edad is None):
            raise ErrorDeInicializacionDeAtributos('La edad no puede ser nula')
        elif not isinstance(edad, int):
            raise ErrorDeInicializacionDeAtributos("La edad debe ser un número entero")
        elif edad <= 0:
            raise ErrorDeInicializacionDeAtributos("La edad debe ser mayor a cero")
        
#que el dni no sea nulo, que sea entero y tenga 7 u 8 digitos
    def validar_dni(self, dni):
        if (dni is None):
            raise ErrorDeInicializacionDeAtributos('El DNI no puede ser nulo')
        elif not isinstance(dni, int):
            raise ErrorDeInicializacionDeAtributos("El DNI debe ser un número entero")
        elif dni<= 0:
            raise ErrorDeInicializacionDeAtributos("El DNI debe ser un número entero positivo")
        else:
            dni_str = str(dni)
            if len(dni_str) < 7 or len(dni_str) > 8:
                raise ErrorDeInicializacionDeAtributos("El DNI debe ser tener 7 u 8 dígitos")
