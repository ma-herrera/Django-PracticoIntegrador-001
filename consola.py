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