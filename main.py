from integrador1 import get_int, get_positive_float
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
"""

seguir="S"
while seguir=="S":

    print ("1- Crear Persona")
    print ("2- Crear Cuenta")
    print ("3- Crear Cuenta Joven")

    opcion=int(input("Ingrese la opcion elegida: "))

    if opcion==1:
        r="S"
        while (r != "N"):
            # nombre=input("Ingrese el nombre de la persona: ")
            # print("Ingrese la edad de la persona: ")
            # edad=get_int()
            
            persona1=Persona()
            #Cuando queremos asignar los atributos tenemos que validar que no se haya producido una excepcion y si sucedió volver a leer hasta obtener un valor correcto. La excepcion puede ser por valores nulos, edad negativa  o longitud de DNI erronea
            try:
                persona1=leer_persona()

            except ErrorDeInicializacionDeAtributos as eid:
                # print(eid)
                print("No se pudo incicializar la persona")
            except Exception as exn:
                print (exn)

    elif opcion==2:
        r="S"
        while (r != "N"):
            
            #Creamos la persona que sera titular de la cuenta
            # persona1=Persona()
            #La excepcion puede ser por valores nulos, edad negativa  o longitud de DNI erronea
            try:
                #Creamos la persona que sera titular de la cuenta
                persona1=leer_persona()
                print(persona1)

                #obtener el saldo
                cantidad = get_positive_float()
                cuenta1 = Cuenta(persona1, cantidad)
                print(cuenta1)
                print (cuenta1.mostrar())
                
            except ErrorDeInicializacionDeAtributos as eid:
                # print(eid)
                print("No se pudo crear la cuenta")
            except Exception as exn:    
                print (f'main {exn}')
            
            #Operamos con la cuenta
            

            r=input("Crear otra cuenta? S/N: ")




    seguir=input("continuar? S/N: ")