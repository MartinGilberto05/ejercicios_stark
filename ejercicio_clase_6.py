from data_stark import lista_personajes





def nombre_genero_m():
    nombre_heroe = lista_personajes["nombre"]
    iniciales = ""
    
    palabras = nombre_heroe.split()
    for palabra in palabras:
        iniciales += palabra["nombre"]

    print(iniciales)
    return 

nombre_genero_m()
