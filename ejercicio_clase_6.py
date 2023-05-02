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
    iniciales = [palabra[0] for palabra in palabras]
    return '.'.join(iniciales) + '.'

print(extraer_iniciales("pepe argento"))

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
    if type(heroe) !=dict or 'nombre' not in heroe:
        return False
    else:
        heroe['iniciales'] = extraer_iniciales(heroe['nombre'])
        return True
    
print(definir_iniciales_nombre(lista_personajes))
    

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

def agregar_iniciales_nombre(lista_heroes):
    if type(lista_heroes) != list or len(lista_heroes) == 0:
        for heroe in lista_heroes:
            iniciales = definir_iniciales_nombre(heroe)

            if not iniciales:
                print("El origen de datos no contiene el formato correcto")
            return False
    else:
        return True

print(agregar_iniciales_nombre(lista_personajes))


#------------------------------------------------------------------------------------------------------------------------------------------------------------->

'''1.4.	Crear la función ‘stark_imprimir_nombres_con_iniciales’  la cual recibirá como parámetro:
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
print('1.4')
def stark_imprimir_nombres_con_iniciales(lista_heroes):
    if type(lista_heroes) != list or len(lista_heroes) == 0:
        return
    agregar_iniciales_nombre(lista_heroes)
    
        
    for heroe in lista_heroes:
        print(f"* {heroe['nombre']} ({extraer_iniciales(heroe['nombre'])})")

#stark_imprimir_nombres_con_iniciales(lista_personajes)

#---------------------------------------------------------------------------------->
'''2.1. Crear la función ‘generar_codigo_heroe’ la cual recibirá como
parámetros:
● id_heroe: un entero que representa el identificador del héroe.
○ NOTA: el valor de id_heroe lo vamos a generar recién el punto
2.3. Para probar la función podes pasarle cualquier entero
● genero_heroe: un string que representa el género del héroe ( puede
tomar los valores ‘M’, ‘F’ o ‘NB’)
La función deberá generar un string con el siguiente formato:

GENERO-000…000ID
Es decir, el género recibido por parámetro seguido de un ‘-’ (guión) y por
último el identificador recibido. Todos los códigos generados deben tener
como máximo 10 caracteres (contando todos los caracteres, inclusive el
guión). Se deberá completar con ceros para que todos queden del mismo
largo
Algunos ejemplos:
F-00000001
M-00000002
NB-0000010
La función deberá validar:
● El identificador del héroe sea numérico.
● El género no se encuentre vacío y este dentro de los valores esperados
(‘M’, ‘F’ o ‘NB’)
En caso de no pasar las validaciones retornar ‘N/A’. En caso de verificarse
correctamente retornar el código generado'''

def generar_codigo_heroe(id_heroe:int, genero_heroe:str) -> str:
    if type(id_heroe)!= int or not genero_heroe or genero_heroe not in ('M', 'F', 'NB'):
        return 'N/A'
    codigo = f"{genero_heroe}-" + str(id_heroe).zfill(9)
    return codigo

#print(generar_codigo_heroe(1, 'F'))  # F-000000001
#print(generar_codigo_heroe(2, 'M'))  # M-000000002
#print(generar_codigo_heroe(10, 'NB'))  # NB-000000010
#print(generar_codigo_heroe('a', 'F'))  # N/A
#print(generar_codigo_heroe(3, 'X'))  # N/A

#----------------------------------------------------------------------------------------------->

'''2.2. Crear la función ‘agregar_codigo_heroe’ la cual recibirá como
parámetro:
● heroe: un diccionario con los datos del personaje
● id_heroe: un entero que representa el identificador del héroe.
○ NOTA: el valor de id_heroe lo vamos a generar recién el punto
2.3. Para probar la función podes pasarle cualquier entero
La función deberá agregar una nueva clave llamada ‘codigo_heroe’ al
diccionario ‘heroe’ recibido como parámetro y asignarle como valor un código
utilizando la función ‘generar_codigo_heroe’

La función deberá validar:
● Que el diccionario recibido como parámetro no se encuentre vacío.
● Que el código recibido mediante generar_codigo_heroe tenga
exactamente 10 caracteres
En caso de pasar las validaciones correctamente la función deberá retornar
True, en caso de encontrarse un error retornar False'''

def agregar_codigo_heroe(heroe: dict, id_heroe: int):

    if type(heroe) != dict:
        return False
    
    codigo_heroe = generar_codigo_heroe(id_heroe, heroe['genero'])
    if len(codigo_heroe) != 10:
        return False
    
    else:
        heroe['codigo_heroe'] = codigo_heroe
        return True

print(agregar_codigo_heroe(lista_personajes, 8))


'''2.3. Crear la función ‘stark_generar_codigos_heroes’ la cual recibirá como
parámetro:
● lista_heroes: la lista de personajes
La función deberá iterar la lista de personajes y agregarle el código a cada
uno de los personajes.
El código del héroe (id_heore) surge de la posición del mismo dentro de la
lista_heroes (comenzando por el 1).
Reutilizar la función agregar_codigo_heroe pasándole como argumentos el
héroe que se está iterando y el id_heroe
Una vez finalizado imprimir por pantalla un mensaje como el siguiente:
(## representa la cantidad de códigos generados):
Se asignaron ## códigos
* El código del primer héroe es: M-00000001
* El código del del último héroe es: M-00001224
La función deberá validar::
● La lista contenga al menos un elemento
● Todos los elementos de la lista sean del tipo diccionario

● Todos los elementos contengan la clave ‘genero’
En caso de encontrar algún error, informar por pantalla: ‘El origen de datos no
contiene el formato correcto’
La función no retorna ningún valor.'''

#def stark_generar_codigos_heroes(lista_heroes:list):
    