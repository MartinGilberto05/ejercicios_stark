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
        altura = lista['altura']
        nombre = lista['nombre']
        print("nombre superHeroe: ", nombre, "y la altura: ", altura)
    return

# D. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
def alto_maxi():
    altura_max = None
    nombre_max = None

    for lista in lista_personajes:
        if altura_max is None or (float(lista['altura']) > altura_max):
            altura_max = float(lista['altura'])
            nombre_max = lista['nombre']
    print( "El heroe mas alto es: ",nombre_max, "Con una altura de: ", altura_max)
    return

# E. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
def alto_minimo():
    altura_min = None
    nombre_min = None

    for lista in lista_personajes:
        if altura_min is None or (float(lista['altura']) < altura_min):
            altura_min = float(lista['altura'])
            nombre_min = lista['nombre']
    print( "El heroe mas bajo es: ",nombre_min, "Con una altura de: ", altura_min)
    return

# F. Recorrer la lista y determinar la altura promedio de los superhéroes (PROMEDIO)
def altura_promedio():
    suma_alturas = 0
    cantidad_personajes = len(lista_personajes)

    for personaje in lista_personajes:
        altura = float(personaje['altura'])
        suma_alturas += altura

    promedio_alturas = suma_alturas / cantidad_personajes

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
    print(' El heroe mas alto es:',nombre_max,'\n Con una altura de:',altura_max,'\nidentidad:',ident_max)
    return



# Llamamos a las funciones para imprimir los valores deseados
alto_maxi()
alto_minimo()
altura_promedio()
identidad_maxi()
