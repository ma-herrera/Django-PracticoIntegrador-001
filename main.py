from integrador1 import maximo_comun_divisor, minimo_comun_multiplo, string_to_dictionary, palabra_mas_repetida, get_int

from persona import *


seguir="S"
while seguir=="S":

    print ("1- Calcular MCD y mcm")
    print ("2- Frecuencia de palabras en una cadena de caracteres")
    print ("3- Leer un entero iterando hasta que sea correcto")
    print ("4- Crear una Persona")

    opcion=int(input("Ingrese la opcion elegida: "))

    if opcion==1:

        r="S"
        while (r != "N"):
            a = int(input("Ingrese un número entero positivo: "))
            b = int(input("Ingrese otro número entero positivo: "))

            print (maximo_comun_divisor(a,b))
            print (minimo_comun_multiplo(a,b))
            r=input("Calcular otro MCD y mcm? S/N: ")
    elif opcion==2:
        r="S"
        while (r != "N"):
            cadena = input("Ingrese una lista de strings separados por espacios en blanco: ")
            dict=string_to_dictionary(cadena)
            if dict!={}:
                tupla=palabra_mas_repetida(dict)
                print("La palabra más repetida es: ", tupla[0])
                print("La frecuencia es: ", tupla[1])
            else:
                print("Ingrese una cadena no vacía")
                
            r=input("Calcular otra frecuencia? S/N: ")

    elif opcion==3:
        r="S"
        while (r != "N"):
            entero=get_int()
            print("El número ingresado es: ", entero)
                
            r=input("Leer otro entero? S/N: ")
            
    elif opcion==4:
        r="S"
        while (r != "N"):
            # nombre=input("Ingrese el nombre de la persona: ")
            # print("Ingrese la edad de la persona: ")
            # edad=get_int()
            
            persona1=Persona()
PENDIENTE
            #Cuando queremos asignar los atributos tenemos que validar que no se haya producido una excepcion y si sucedió volver a leer hasta obtener un valor correcto. La excepcion puede ser por valores nulos, edad negativa  o longitud de DNI erronea

            nombre=input("Ingrese el nombre de la persona: ")

            persona1.nombre=nombre
            print(persona1)
                
            persona1.edad=get_int()
            print(persona1)

            persona1.dni=get_int()
            print(persona1)

            r=input("Crear otra persona? S/N: ")


    seguir=input("continuar? S/N: ")