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
    altura_min = None
    nombre_min = None

    for genero_m in lista_personajes:
        if genero_m['genero'] == 'M':
            if altura_min is None or (float(genero_m['altura']) < altura_min):
                altura_min = float(genero_m['altura'])
                nombre_min = genero_m['nombre']
    print( "El heroe mas alto genero M es: " , nombre_min ,"\nCon una altura de: ",altura_min,"mts")
    return

# F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F
def alto_min_f():
    altura_min = None
    nombre_min = None

    for genero_f in lista_personajes:
        if genero_f['genero'] == 'F':
            if altura_min is None or (float(genero_f['altura']) < altura_min):
                altura_min = float(genero_f['altura'])
                nombre_min = genero_f['nombre']
    print( "El heroe mas alto genero F es: " , nombre_min ,"\nCon una altura de: ",altura_min,"mts")
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

# I Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)
def identidad():
    altura_max = None
    nombre_max = None
    altura_min = None
    nombre_min = None
    altura_max_f = None
    nombre_max_f = None
    nombre_min_f = None
    altura_min_f = None

    for genero in lista_personajes:
        if genero['genero'] == 'M':
            if altura_max is None or (float(genero['altura']) > altura_max):
                altura_max = float(genero['altura'])
                nombre_max = genero['identidad']
            elif altura_min is None or (float(genero['altura']) < altura_min):
                altura_min = float(genero['altura'])
                nombre_min = genero['identidad']
                
        if genero['genero'] == 'F':
            if altura_max_f is None or (float(genero['altura']) > altura_max_f):
                altura_max_f = float(genero['altura'])
                nombre_max_f = genero['identidad']
            elif altura_min_f is None or (float(genero['altura']) > altura_min_f):
                altura_min_f = float(genero['altura'])
                nombre_min_f = genero['identidad']
        
        
    print( "El heroe mas alto genero M es: " , nombre_max ,"Con una altura de: ",altura_max,"mts")
    print( "El heroe mas bajo genero M es: " , nombre_min ,"Con una altura de: ",altura_min,"mts")
    print( "El heroe mas bajo genero F es: " , nombre_max_f ,"Con una altura de: ",altura_max_f,"mts")
    print( "El heroe mas bajo genero F es: " , nombre_min_f ,"Con una altura de: ",altura_min_f,"mts")
    return
    





# J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
def color_de_ojos():
    color_ojos = {}
    
    for lista in lista_personajes:
        color = lista['color_ojos']
        if color in color_ojos:
            color_ojos[color] += 1
        else:
            color_ojos[color] = 1
            
    for color in color_ojos:
        cantidad = color_ojos[color]
        print("color de ojos:", color, "cantidad de heroes:", cantidad)
    return

# K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
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

# L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’).
def tipo_de_inteligencia():
    inteligencia = {}
    
    for lista in lista_personajes:
        intel = lista['inteligencia']
        if intel == "":
            intel= "No Tiene"
        if intel in inteligencia:
            inteligencia[intel] += 1
        else:
            inteligencia[intel] = 1
            
    for intel in inteligencia:
        cantidad = inteligencia[intel]
        print("inteligencia ", intel, "cantidad de heroes:", cantidad)
    return

# M. Listar todos los superhéroes agrupados por color de ojos.
def superheroes_por_color_de_ojos():
    heroe_color_ojos = {}
    for lista in lista_personajes:
        color_de_ojos = lista["color_ojos"]
        if color_de_ojos  in heroe_color_ojos:
            heroe_color_ojos[color_de_ojos].append(lista["nombre"])
        else:
            heroe_color_ojos[color_de_ojos] = [lista['nombre']]

    for color in heroe_color_ojos:
        print(f"\nColor de ojos {color}: ")
        for heroe in heroe_color_ojos[color]:
            print(f"- {heroe} ")
    return

# N. Listar todos los superhéroes agrupados por color de pelo.
def superheroes_por_color_de_pelo():
    heroe_color_pelo = {}
    for lista in lista_personajes:
        color_de_pelo = lista["color_pelo"]
        if color_de_pelo  in heroe_color_pelo:
            heroe_color_pelo[color_de_pelo].append(lista["nombre"])
        else:
            heroe_color_pelo[color_de_pelo] = [lista['nombre']]

    for color in heroe_color_pelo:
        print(f"\nColor de pelo {color}: ")
        for heroe in heroe_color_pelo[color]:
            print(f"- {heroe} ")
    return

# O. Listar todos los superhéroes agrupados por tipo de inteligencia
def superheroes_por_color_de_ojos():
    heroe_color_ojos = {}
    for lista in lista_personajes:
        color_de_ojos = lista["color_ojos"]
        if color_de_ojos  in heroe_color_ojos:
            heroe_color_ojos[color_de_ojos].append(lista["nombre"])
        else:
            heroe_color_ojos[color_de_ojos] = [lista['nombre']]

    for color in heroe_color_ojos:
        print(f"\nColor de ojos {color}: ")
        for heroe in heroe_color_ojos[color]:
            print(f"- {heroe} ")
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
#color_de_pelo()
#color_de_ojos()
#tipo_de_inteligencia()
#superheroes_por_color_de_ojos()
identidad()