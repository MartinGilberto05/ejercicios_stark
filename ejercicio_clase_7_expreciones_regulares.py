from data_stark import lista_personajes

import re
nombre_heroe = ""
def extraer_iniciales():
    nombre_heroe = {}
    for personaje in lista_personajes:
        nombre_heroe = personaje['nombre']   
        nombre_heroe = nombre_heroe.replace('-',' ')
        result = re.findall("(?!the)[A-Z]", nombre_heroe)
        
        inicial = '.'.join(result.upper()[0]for result in result)
        
    print(inicial + '.')
        
extraer_iniciales()