# import persona
from cexception import *

###################### CLASE CUENTA #########################

"""Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (q(que es una persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional. Crear los siguientes métodos para la clase:
    Un constructor, donde los datos pueden estar vacíos.
    Los setters y getters para cada uno de los atributos. El atributo no se puede modificar
directamente, sólo ingresando o retirando dinero.
 mostrar(): Muestra los datos de la cuenta.
 ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es
negativa, no se hará nada.
 retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números
rojos.
"""

class Cuenta():
    def __init__(self, titular, cantidad=0.0):
        self._titular=titular
        self._cantidad=cantidad

    ############## GETTERS ####################
    @property
    def titular(self):
        return self._titular

    @property
    def cantidad(self):
        return self._cantidad
    


    ############## SETTERS ####################

    #recibe una Persona y la asigna como titular de la cuenta
    @titular.setter
    def titular(self, titular):
        try:
            if titular is None:
                raise ErrorDeInicializacionDeAtributos
        except ErrorDeInicializacionDeAtributos as e:
                print("El titular es obligatorio")
                raise
        else:
            self._titular = titular

    #recibe un float y lo asigna como cantidad de la cuenta
    @cantidad.setter
    def cantidad(self, cantidad):
        try:
            if (not (cantidad is None) and (not isinstance(cantidad, float))):
                raise ErrorDeInicializacionDeAtributos
            self._cantidad = cantidad
        except ErrorDeInicializacionDeAtributos as e:
            print("La cantidad debe ser un valor numérico")
            raise

    def __str__(self):
        #Recuperar los datos de la persona
        persona = self.titular
        print ("dentro de __str cuenta")
        print (persona)
        datos_persona = persona.mostrar()
        return (f'{datos_persona} tiene en su cuenta ${self.cantidad}')
    
    def mostrar(self):
        #Recuperar los datos de la persona
        datos_persona = self.titular.mostrar()
        return (f'{datos_persona} tiene en su cuenta ${self.cantidad}')


    #se espera un número float positivo. Si es negativo no se hace nada
    def ingresar(self, monto):
        if monto>0:
            self.cantidad += monto

    def retirar(self, monto):
        if monto>0:
            self.cantidad -= monto


################ CLASE CUENTA JOVEN ##########################
"""
“Cuenta Joven”,  deriva de la clase Cuenta. Cuando se crea esta nueva clase, 
además del titular y la cantidad se debe guardar una bonificación que estará expresada en 
tanto por ciento. Crear los siguientes métodos para la clase:
 Un constructor.
 Los setters y getters para el nuevo atributo.
 En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo 
tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es 
mayor de edad pero menor de 25 años y falso en caso contrario.
 Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
 El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la 
cuenta
"""
# recibe una Persona, un float y un entero (que representa un porcentaje: x ==> x*cantidad/100)
class CuentaJoven(Cuenta):
    def __init__ (self, titular, cantidad, bonificacion):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion

    ############# GETTERS ################
    @property
    def titular(self):
        return self._titular

    @property
    def cantidad(self):
        return self._cantidad

    @property
    def bonificacion(self):
        return self._bonificacion

    ############# SETTERS ################
    #espera un valor >=0
    @bonificacion.setter
    def bonificacion(self, bonif):
        self._bonificacion = bonif

    @titular.setter
    def titular(self, persona):
        #el titular debe ser mayor de edad y menor de 25
        #super().titular(persona)
        try:
            if persona is None:
                raise ErrorDeInicializacionDeAtributos
            elif self.es_titular_valido(persona):
                self._titular=persona
            else:
                #el titular no tiene la edad adecuada
                raise ErrorDeInicializacionDeAtributos
        except ErrorDeInicializacionDeAtributos as e:
                print("El titular es obligatorio y debe tener entre 18 y 25 años")
                raise
        
    @cantidad.setter
    def cantidad(self, cantidad):
        self._cantidad = cantidad

    ############# VALIDACIONES ################

    def es_titular_valido(self, persona):
        try:
            if persona.edad is None:
                msg="Error. Primero debe cargar la edad del titular."
                raise ErrorDeInicializacionDeAtributos
            elif persona.edad<18 or persona.edad>25:
                msg="El titular de la Cuenta Joven debe tener entre 18 y 25 años"
                raise ErrorDeInicializacionDeAtributos
        except ErrorDeInicializacionDeAtributos:
            print(msg)
            return False
        
        return True



    ############# OTROS MÉTODOS ################
    def retirar(self, monto):
        #validar que sea valido el titular
        persona = self.titular
        if self.es_titular_valido(persona):
            super().retirar(monto)

    def __str__(self):
        cuentabase=super().mostrar()
        return f'Cuenta Joven. {cuentabase}, bonificación: {self.bonificacion}%'

    def mostrar(self):
        return f'Cuenta Joven. Bonificación: {self.bonificacion}%'