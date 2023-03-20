# from integrador1 import get_positive_float
from consola import get_positive_float, get_int
from consola import leer_persona
from cexception import *
from cuenta import *
from persona import *

# PREGUNTAS:
"""
1) Por qué usar ELSE en las exepciones y no meter todo el código dentro del TRY?
2)Cómo se deben organizar las clases dentro de los archivos? Un archivo por clase? Mas de una clase dentro del mismo archivo?
3) Dónde meter las funciones de lectura y escritura de objetos de una clase?
4) En funciones de validacion que pueden fallar por mas de una causa es mejor devolver estados o definir excepciones custom? (por ejemplo si el error se puede dar por valor nulo o por valor negativo)
5)             print(cuenta)
            print (cuenta.mostrar())
            Si mostrar es un metodo de cuenta, como imprimo por consola sin hacerlo dentro de la clase cuenta? Cual es la manera correcta de manejar la entrada/salida de objetos?
    en este caso __str__ no serviria igual que mostrar y se le hace el print al objeto directamente?
"""

while True:

    while True:
        opcion=input ("Ingrese el tipo de cuenta que quiere crear. 1: Cuenta común, 2:Cuenta Joven, S:Salir: ")
        if opcion in ["1", "2"]:
            break

    if opcion=="1":
        #Creamos la persona que sera titular de la cuenta
        # persona1=Persona()
        #La excepcion puede ser por valores nulos, edad negativa  o longitud de DNI erronea
        try:
            #Creamos la persona que sera titular de la cuenta
            persona1=leer_persona()
            print(persona1)

            #obtener el saldo
            cantidad = get_positive_float()

            cuenta = Cuenta(persona1, cantidad)
            print(cuenta)
            print (cuenta.mostrar())
            
        except ErrorDeInicializacionDeAtributos as eid:
            # print(eid)
            print("No se pudo crear la cuenta")
        except Exception as exn:    
            print (f'main {exn}')

    if opcion=="2":
    #Creamos la persona que sera titular de la cuenta
    #La excepcion puede ser por valores nulos, edad no comprendida entre 18 y 25  o longitud de DNI erronea
        try:
            #Crear cuenta joven con atributos en null
            cuenta=CuentaJoven(None, None, None)
            #Creamos la persona que sera titular de la cuenta
            cuenta.titular=leer_persona()
            # print(cuenta.titular)

            #obtener el saldo
            cuenta.cantidad = get_positive_float()
            print("Ingrese la bonificacion: ")
            cuenta.bonificacion = get_int() #faltaria validar que sea >0
            print(cuenta)
            print (cuenta.mostrar())
            
        except ErrorDeInicializacionDeAtributos as eid:
            # print(eid)
            print("No se pudo crear la cuenta")
            continue
        except Exception as exn:    
            print (f'main {exn}')
        
    #Cuenta creada. Operamos con la cuenta
    while True:

        while True:
            operacion=input ("Ingrese la operacion que desea realizar. 1: Ingreso, 2:Retiro: ")
            if operacion in ["1", "2"]:
                break 

        print("ingrese monto: ")
        monto = get_positive_float()

        if operacion == "1":
            #deposito
            cuenta.ingresar(monto)
        else:
            cuenta.retirar(monto)

        print(cuenta.mostrar())
        print(cuenta)
    
        seguir=input("continuar operando con la cuenta? S/N: ")
        if seguir!="S":
            break

    seguir=input("continuar creando cuentas? S/N: ")
    if seguir!="S":
        break
