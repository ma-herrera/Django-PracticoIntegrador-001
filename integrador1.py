"""5. Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una
cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero
del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el
ejercicio tanto de manera iterativa como recursiva.
"""
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
