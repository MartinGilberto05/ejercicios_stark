# Martin Gilberto Div. 1f
# desafio #00 de 

from data_stark import lista_personajes

# B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
def personaje():
    for lista in lista_personajes:
        print(lista['nombre'])
    return

# C. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
def nombre_altura():
    altura = None
    nombre = None
    for lista in lista_personajes:
        altura = float(lista['altura'])
        nombre = lista['nombre']
        print("nombre superHeroe: ", nombre, "y la altura: {:.2f}".format(altura),"mts")
    return

# D. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
def alto_maxi():
    altura_max = None
    nombre_max = None

    for lista in lista_personajes:
        if altura_max is None or (float(lista['altura']) > altura_max):
            altura_max = float(lista['altura'])
            nombre_max = lista['nombre']
    print( "El heroe mas alto es: " , nombre_max ,"\nCon una altura de: ",altura_max,"mts")
    return

# E. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
def alto_minimo():
    altura_min = None
    nombre_min = None

    for lista in lista_personajes:
        if altura_min is None or (float(lista['altura']) < altura_min):
            altura_min = float(lista['altura'])
            nombre_min = lista['nombre']
    print( "El heroe mas bajo es: ",nombre_min,"\nCon una altura de: ", altura_min,"mts")
    return

# F. Recorrer la lista y determinar la altura promedio de los superhéroes (PROMEDIO)
def altura_promedio():
    suma_alturas = 0
    cantidad_personajes = len(lista_personajes)

    for personaje in lista_personajes:
        altura = float(personaje['altura'])
        suma_alturas += altura

    promedio_alturas = suma_alturas / cantidad_personajes
    print("el promedio de altura es: {:.2f}".format(promedio_alturas)+" Mts")
    return promedio_alturas

# G. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)
def identidad_maxi():
    altura_max = None
    nombre_max = None
    ident_max = None

    for lista in lista_personajes:
        if altura_max is None or (float(lista['altura']) > altura_max):
            altura_max = float(lista['altura'])
            nombre_max = lista['nombre']
            ident_max = lista['identidad']
    print("El heroe mas alto es:",nombre_max,"\nCon una altura de:",altura_max,"mts""\nidentidad:",ident_max)
    return

# H. Calcular e informar cual es el superhéroe más y menos pesado.
def peso_maxi():
    peso_max = None
    nombre_max = None

    for lista in lista_personajes:
        if peso_max is None or (float(lista['peso']) > peso_max):
            peso_max = float(lista['peso'])
            nombre_max = lista['nombre']
    print( "\nEl heroe mas pesado es: " , nombre_max , "\nCon un peso de: {:.2f}".format(peso_max),"Kg")
    return

def peso_minimo():
    peso_min = None
    nombre_min = None

    for lista in lista_personajes:
        if peso_min is None or (float(lista['peso']) < peso_min):
            peso_min = float(lista['peso'])
            nombre_min = lista['nombre']
    print( "El heroe mas liviano es: ",nombre_min,"\nCon un peso de: {:.2f}".format(peso_min),"Kg")
    return



# Llamamos a las funciones para imprimir los valores deseados
def imprimir_funcion():
    personaje()
    nombre_altura()
    alto_maxi()
    alto_minimo()
    altura_promedio()
    identidad_maxi()
    peso_minimo()
    peso_maxi()

#imprimir_funcion()

# J. Construir un menú que permita elegir qué dato obtener

while True:
    print("Seleccione una opción:\n")
    print("1. Imprimir nombres de superhéroes")
    print("2. Imprimir nombres y alturas de superhéroes")
    print("3. Encontrar el superhéroe más alto")
    print("4. Encontrar el superhéroe más bajo")
    print("5. Calcular altura promedio de superhéroes")
    print("6. Encontrar el superhéroe más pesado")
    print("7. Encontrar el superhéroe más liviano")
    print("8. Imprimir todas las funciones")
    print("9. Salir\n")

    opcion = input("\nIngrese el número de opción deseado: ")

    if opcion == "1":
        personaje()
        continuar = input("\n¿Desea continuar? (S/N): ")
        if continuar.upper() == "N":
            break
    elif opcion == "2":
        nombre_altura()
        continuar = input("\n¿Desea continuar? (S/N): ")
        if continuar.upper() == "N":
            break
    elif opcion == "3":
        alto_maxi()
        continuar = input("\n¿Desea continuar? (S/N): ")
        if continuar.upper() == "N":
            break
    elif opcion == "4":
        alto_minimo()
        continuar = input("\n¿Desea continuar? (S/N): ")
        if continuar.upper() == "N":
            break
    elif opcion == "5":
        altura_promedio()
        continuar = input("\n¿Desea continuar? (S/N): ")
        if continuar.upper() == "N":
            break
    elif opcion == "6":
        peso_maxi()
        continuar = input("¿Desea continuar? (S/N): ")
        if continuar.upper() == "N":
            break
    elif opcion == "7":
        peso_minimo()
        continuar = input("¿Desea continuar? (S/N): ")
        if continuar.upper() == "N":
            break
    elif opcion == "8":
        imprimir_funcion()
        continuar = input("¿Desea continuar? (S/N): ")
        if continuar.upper() == "N":
            break
    elif opcion == "9":
        break
    else:
        print("Opción inválida. Intente nuevamente.")
