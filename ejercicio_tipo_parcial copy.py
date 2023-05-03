

import json
import re
import csv

def parse_json_stark(nombre_archivo:str)->list:
    dic_json = {}
    
    archivo = open(nombre_archivo,'r')
    dic_json = json.load(archivo)
    archivo.close()
    return dic_json['heroes']

lista_heroes = parse_json_stark("data_stark.json")
lista_aux = lista_heroes.copy()
#print(lista_heroes)


#1
def listar_n_heroe(cantidad:int, lista_heroes:list):
    
    if(len(lista_aux) >= cantidad):
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
def ardenar_y_listar(lista:list[dict], clave:str, tipo = 'ASC'):
    bandera_swap = True
    while bandera_swap == True:
        bandera_swap = False
        for i in range(len(lista)-1):
            if tipo == 'ASC':
                if(lista[i][clave] < lista[i+1][clave]):
                    aux = lista[i]
                    lista[i] = lista[i]
                    lista[i] = aux
                    bandera_swap = True
            elif tipo == 'DESC':
                if(lista[i][clave] > lista[i+1][clave]):
                    aux = lista[i]
                    lista[i] = lista[i]
                    lista[i] = aux
                    bandera_swap = True
    return lista_aux


normalizar_flotantes(lista_aux, 'altura')
#print(ardenar_y_listar(lista_aux, 'altura', 'asc'))

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
                lista_max.append(i['nombre'])
    print(lista_min)

promedio = calcular_promedio(lista_aux, 'altura')
calcular_min_o_max_altura(lista_aux, 'altura', 'mayor', 180)

