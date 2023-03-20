from persona import *


def leer_persona():
    try:
        persona1=Persona()
        nombre=input("Ingrese el nombre de la persona: ")
        persona1.nombre=nombre
        print("Ingrese la edad: ")
        persona1.edad=get_int()
        print("Ingrese el número de DNI: ")
        persona1.dni=get_int()
    except ErrorDeInicializacionDeAtributos as eid:
        print("Se ingresaron datos erróneos. No se pudo crear la persona")
        raise
    except Exception as exn:
        print (f'leer_persona: {exn}')
        raise
    else:
        return persona1
    
    #lee un entero en un ciclo hasta tener exito
def get_int():    
    while True:
        try:
            entero = int(input())
        except ValueError:
            print ("Error! Debe ingresar un número entero")
        else:
            break
    return entero

#lee un float positivo en un ciclo hasta tener exito
def get_positive_float():
    while True:
        try:
            numero=float(input("Ingrese un número positivo (puede tener decimales): "))
        except ValueError:
            print("Error de tipo de dato")
        else:
            if numero < 0:
                print("Error. Se ingresó un número negativo")
            else:
                break
    
    return numero