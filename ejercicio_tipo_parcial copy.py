

import json
import re
import csv

def parse_json_stark(nombre_archivo:str)->list:
    dic_json = {}  
    
    archivo = open(nombre_archivo,'r') #--------- abro el archivo original
    dic_json = json.load(archivo)  #-------- rescato el diccionario del original 
    archivo.close() #------------- cierro el archivo
    return dic_json['heroes'] #-------- saco el diccionario y tomo la clave del archivo original 

lista_heroes = parse_json_stark("data_stark.json") #----------- cree mi lista original
lista_aux = lista_heroes.copy()   #------creo una copia de la lista original 
#print(lista_heroes)


#1
def listar_n_heroe(cantidad:int, lista_aux:list):
    
    if(len(lista_aux) >= int(cantidad)):
            lista_auxiliar = [] #esto es una lista vacia
            for index in range(cantidad):
                heroe = lista_aux[index]['nombre']
                lista_auxiliar.append(heroe)
                print(heroe)
            resultado = lista_auxiliar
    else:
        resultado = False
    
    return resultado
#print(listar_n_heroe(5, lista_aux))

def sanitizar_flotante(lista_aux:str):
    for heroe in lista_aux:
        heroe['altura'] = float(heroe['altura'])
    
def normalizar_flotantes(lista:list[dict], llave:str):
    for i in lista:
        i[llave] = float(i[llave])

#2
def ardenar_y_listar(lista:list[dict], clave:str, tipo:str):
    bandera_swap = True
    while bandera_swap == True:
        bandera_swap = False
        for i in range(len(lista)-1):
            if tipo == 'ASC':
                if lista[i][clave] < lista[i+1][clave]:
                    aux = lista[i]
                    lista[i] = lista[i+1]
                    lista[i+1] = aux
                    bandera_swap = True
            elif tipo == 'DESC':
                if lista[i][clave] > lista[i+1][clave]:
                    aux = lista[i]
                    lista[i] = lista[i+1]
                    lista[i+1] = aux
                    bandera_swap = True
    return lista_aux


normalizar_flotantes(lista_aux, 'altura')
'''j = ardenar_y_listar(lista_aux, 'altura', 'DESC')
for i in j:'''
# print(f"nombre:{i['nombre']},'altura:{i['altura']}")

#3. Ordenar y Listar héroes por fuerza. Preguntar al usuario si lo quiere ordenar de manera ascendente (‘asc’) o descendente (‘desc’)

lista_aux = ardenar_y_listar(lista_aux, 'fuerza', 'ASC')

# 4. 
def calcular_promedio(lista:list[dict],llave)-> float:
    acum = 0
    cont = 0
    for i in lista:
        acum = acum + i[llave]
        cont = cont + 1
        
    promedio = acum / cont
    
    promedio = round(promedio,2)
    
    return promedio

def calcular_min_o_max_altura(lista:list[dict], llave:str, tipo:str, comparador: float):
    lista_min = []
    lista_max = []
    mayor = lista[0][llave]
    if tipo == 'mayor':
        for i in lista:
            if i['altura'] > comparador:
                lista_max.append(i['nombre'])
        print(lista_max)
    if tipo == 'menor':
        for i in lista:
            if i['altura'] < comparador:
                lista_min.append(i['nombre'])
        print(lista_min)

promedio = calcular_promedio(lista_aux, 'altura')
print("promedio:",promedio)
#calcular_min_o_max_altura(lista_aux, 'altura', 'mayor', 200)

#5
def buscar_heroes_por_inteligencia(lista:list[dict], clave:str, tipo:str):
    
    buscar_heroes = []
    for heroe in lista:
        if re.match(tipo,heroe[clave]):
            buscar_heroes.append(heroe)
    return buscar_heroes

tipo = "high"

#buscar_heroes_por_inteligencia(lista_aux, 'inteligencia', tipo)


#6
def guardar_archivo(nombre_archivo:str, lista:list):
    with open(nombre_archivo, 'w') as archivo:
        for i in lista:
            linea = f"{i['nombre']}, {i['identidad']}, {i['empresa']}, {i['altura']}, {i['peso']}, {i['genero']}, {i['color_ojos']}, {i['color_pelo']}, {i['fuerza']}, {i['inteligencia']}\n"
            
            archivo.write(linea)
            
#guardar_archivo('cakka.csv',lista_aux)

#menu
while True:
    print("Menú:")
    print("1. Listar los primeros N héroes")
    print("2. Ordenar y listar héroes por altura")
    print("3. Ordenar y listar héroes por fuerza")
    print("4. Filtrar héroes por promedio de una key numérica")
    print("5. Buscar héroes por inteligencia")
    print("6. Exportar lista de héroes a CSV")
    print("7. Salir")


    opcion = input("Ingrese una opción: ")
    if not re.match("^[1-7]$", opcion):
        print("Opción inválida. Intente nuevamente.")
        continue

    opcion = int(opcion)

    if opcion == 1:
        
        n = input("Ingrese la cantidad de héroes a listar: ")
        if not re.match("^[1-9][0-9]*$", n):
            print("Cantidad inválida. Intente nuevamente.")
            continue
        
        n = int(n)
        if n > len():
            print("Cantidad supera el número máximo de héroes. Intente nuevamente.")
            continue

        buscar_heroe = lista_aux[:n]
        print(listar_n_heroe(buscar_heroe))

    if opcion == 2:
         ardenar_y_listar() 