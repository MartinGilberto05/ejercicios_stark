from data_stark import lista_personajes

# A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
def nombre_genero_m():
    for nombres_m in lista_personajes:
        if nombres_m['genero'] == 'M':
            print(nombres_m['nombre'])
    return nombres_m


# B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
def nombre_genero_f():
    for nombres_m in lista_personajes:
        if nombres_m['genero'] == 'F':
            print(nombres_m['nombre'])
    return nombres_m


# C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
def alto_maxi_m():
    altura_max = None
    nombre_max = None

    for genero_m in lista_personajes:
        if genero_m['genero'] == 'M':
            if altura_max is None or (float(genero_m['altura']) > altura_max):
                altura_max = float(genero_m['altura'])
                nombre_max = genero_m['nombre']
    print( "El heroe mas alto genero M es: " , nombre_max ,"\nCon una altura de: ",altura_max,"mts")
    return

# D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
def alto_maxi_f():
    altura_max = None
    nombre_max = None

    for genero_f in lista_personajes:
        if genero_f['genero'] == 'F':
            if altura_max is None or (float(genero_f['altura']) > altura_max):
                altura_max = float(genero_f['altura'])
                nombre_max = genero_f['nombre']
    print( "El heroe mas alto genero F es: " , nombre_max ,"\nCon una altura de: ",altura_max,"mts")
    return

# E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M
def alto_min_m():
    altura_max = None
    nombre_max = None

    for genero_m in lista_personajes:
        if genero_m['genero'] == 'M':
            if altura_max is None or (float(genero_m['altura']) < altura_max):
                altura_max = float(genero_m['altura'])
                nombre_max = genero_m['nombre']
    print( "El heroe mas alto genero M es: " , nombre_max ,"\nCon una altura de: ",altura_max,"mts")
    return

# F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F
def alto_min_f():
    altura_max = None
    nombre_max = None

    for genero_f in lista_personajes:
        if genero_f['genero'] == 'F':
            if altura_max is None or (float(genero_f['altura']) < altura_max):
                altura_max = float(genero_f['altura'])
                nombre_max = genero_f['nombre']
    print( "El heroe mas alto genero F es: " , nombre_max ,"\nCon una altura de: ",altura_max,"mts")
    return

#
def altura_promedio_m():
    suma_alturas = 0
    cantidad_personajes = len(lista_personajes)

    for genero_m in lista_personajes:
        if genero_m['genero'] == 'M':
            altura = float(genero_m['altura'])
            suma_alturas += altura

    promedio_alturas = suma_alturas / cantidad_personajes
    print("el promedio de altura en gener M es: {:.2f}".format(promedio_alturas)+" Mts")
    return promedio_alturas


def altura_promedio_f():
    suma_alturas = 0
    cantidad_personajes = len(lista_personajes)

    for genero_f in lista_personajes:
        if genero_f['genero'] == 'F':
            altura = float(genero_f['altura'])
            suma_alturas += altura

    promedio_alturas = suma_alturas / cantidad_personajes
    print("el promedio de altura en gener F es: {:.2f}".format(promedio_alturas)+" Mts")
    return promedio_alturas

# Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)








# J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
def color_de_ojos():
    color_ojos = {}
    
    for lista in lista_personajes:
        color = lista['color_ojos']
        
        color_ojos[color] = color_ojos.get(color,0) + 1
        
    for color, cantidad  in color_ojos.items():
        print("color de ojos:", color, "cantidad de heroes:", cantidad)
    return

def color_de_pelo():
    color_pelo = {}
    
    for lista in lista_personajes:
        color = lista['color_pelo']
        if color in color_pelo:
            color_pelo[color] += 1
        else:
            color_pelo[color] = 1
        
    for color in color_pelo:
        cantidad = color_pelo[color]
        print("color de pelo:", color, "cantidad de heroes:", cantidad)
    return









#nombre_genero_m()
#nombre_genero_f()
#alto_maxi_m()
#alto_maxi_f()
#alto_min_f()
#alto_min_m()
#altura_promedio_m()
#altura_promedio_f()
#color_de_ojos()
color_de_pelo()