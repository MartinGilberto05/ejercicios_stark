from data_stark import lista_personajes

'''1.1. Crear la función ‘extraer_iniciales’ que recibirá como parámetro:
● nombre_heroe: un string con el nombre del personaje
La función deberá devolver a partir del parámetro recibido un nuevo string con
las iniciales del nombre del personaje seguidos por un punto (.)
● En el caso que el nombre del personaje contenga el artículo ‘the’ se
deberá omitir de las iniciales
● Se deberá verificar si el nombre contiene un guión ‘-’ y sólo en el caso
que lo tenga se deberá reemplazar por un espacio en blanco
La función deberá validar:
● Que el string recibido no se encuentre vacío
Devolver ‘N/A’ en caso de no cumplirse la validación

Ejemplo de la salida de la función para Howard the Duck:
H.D.'''
    
def extraer_iniciales(nombre_heroe:str)->str:
    
    if not nombre_heroe:
        return 'N/A'
    nombre_heroe = nombre_heroe.replace('-', ' ')
    nombre_heroe = nombre_heroe.replace('the', '')
    nombre_heroe = nombre_heroe.upper()
    palabras = nombre_heroe.split()
    if palabras[0].lower() == 'the':
        palabras = palabras[1:]
    iniciales = [palabra[0] for palabra in palabras]
    return '.'.join(iniciales) + '.'

#print(extraer_iniciales(""))

#---------------------------------------------------------------------->

'''1.2.	Crear la función ‘definir_iniciales_nombre’ la cual recibirá como parámetro:
●	heroe: un diccionario con los datos del personaje

La función deberá agregar una nueva clave al diccionario recibido como parámetro. 
La clave se deberá llamar ‘iniciales’ y su valor será el obtenido de llamar a la función ‘extraer_iniciales’
La función deberá validar:
●	Que el dato recibido sea del tipo diccionario
●	Que el  diccionario contengan la clave ‘nombre’  
En caso de encontrar algún error retornar False, caso contrario retornar True
'''

def definir_iniciales_nombre(heroe:dict):
    heroe = {'nombre': 'peter parker'}
    
    if type(heroe) != dict:
        return False
    if 'nombre' not in heroe.keys():
        return False
    heroe['iniciales'] = extraer_iniciales(heroe['nombre'])
    #print(heroe)
    return True
print(definir_iniciales_nombre('heroe'))
    
#---------------------------------------------------------------------------------------------->

''' 1.3.	Crear la función ‘agregar_iniciales_nombre’ la cual recibirá como parámetro:
●	lista_heroes: lista de personajes
	Se deberá validar:
●	Que lista_heroes sea del tipo lista
●	Que la lista contenga al menos un elemento
La función deberá iterar la lista_heroes pasándole cada héroe a la función definir_iniciales_nombre.
En caso que la función definir_iniciales_nombre() retorne False entonces se deberá detener la iteración e informar por pantalla el siguiente mensaje:
‘El origen de datos no contiene el formato correcto’ 
La función deberá devolver True en caso de haber finalizado con éxito o False en caso de que haya ocurrido un error'''

def agregar_iniciales_nombre(lista_heroe:list):
    lista_heroe = ['heroe']
    
    if type(lista_heroe) != list:
        print('No es una lista!!')
        return False
    
    if len(lista_heroe) ==0:
        print('no tiene elemento')
        return False
    
    for heroe in lista_heroe:
        if not definir_iniciales_nombre(heroe):
            print('El origen de datos no contiene el formato correcto')
            return False
    return True

print(agregar_iniciales_nombre('lista_heroe'))

#------------------------------------------------------------------------------------------------------------------------------------------------------------->

'''1.3.	Crear la función ‘stark_imprimir_nombres_con_iniciales’  la cual recibirá como parámetro:
●	lista_heroes: la lista de personajes
La función deberá utilizar la función agregar_iniciales_nombre’ para añadirle las iniciales a los diccionarios contenidos en la lista_heroes
Luego deberá imprimir la lista completa de los nombres de los personajes seguido de las iniciales encerradas entre paréntesis () 
	Se deberá validar:
●	Que lista_heroes sea del tipo lista
●	Que la lista contenga al menos un elemento
Delante de cada nombre se deberá agregar un asterisco ‘*’ (de forma de viñeta) seguido de un espacio.
Ejemplo de salida:
* Howard the Duck (H.D.)
* Rocket Raccoon (R.R.)
…
La función no retorna nada
'''
def stark_imprimir_nombres_con_iniciales(personaje):
    iniciales = ""
    nombres = personaje['nombre'].split()
for nombre in nombres:
    iniciales +=nombre[inicia 0]+"."

