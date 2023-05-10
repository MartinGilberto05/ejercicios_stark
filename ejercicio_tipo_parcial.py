

import json
import re
import csv

# Leemos el archivo JSON y cargamos los datos en una lista de diccionarios
with open('data_stark.json', 'r') as f:
    heroes = json.load(f)['heroes']

# Función para imprimir la lista de héroes
def print_heroes(heroes):
    for hero in heroes:
        print(hero['nombre'])

# Función para ordenar la lista de héroes por altura o fuerza (según key)
def sort_heroes_by(heroes, key, reverse):
    sorted_heroes = sorted(heroes, key=lambda hero: hero[key], reverse=reverse)
    return sorted_heroes

# Función para calcular el promedio de cualquier key numérica y filtrar la lista
def filter_heroes_by_avg(heroes, key, condition):
    # Calculamos el promedio de la key especificada
    values = [hero[key] for hero in heroes]
    avg = sum(values) / len(values)
    
    # Filtramos los héroes según la condición especificada
    if condition == 'mayor':
        filtered_heroes = [hero for hero in heroes if hero[key] > avg]
    else:
        filtered_heroes = [hero for hero in heroes if hero[key] < avg]
    
    return filtered_heroes

# Función para buscar héroes por inteligencia
def search_heroes_by_intelligence(heroes, intelligence):
    # Utilizamos RegEx para hacer una búsqueda por inteligencia
    pattern = re.compile(intelligence, re.IGNORECASE)
    searched_heroes = [hero for hero in heroes if pattern.search(hero['intelligence'])]
    return searched_heroes

# Función para exportar la lista de héroes a un archivo CSV
def export_heroes_to_csv(heroes, filename):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['name', 'intelligence', 'height', 'strength'])
        for hero in heroes:
            writer.writerow([hero['name'], hero['intelligence'], hero['height'], hero['strength']])

# Menú principal
while True:
    print("Menú:")
    print("1. Listar los primeros N héroes")
    print("2. Ordenar y listar héroes por altura")
    print("3. Ordenar y listar héroes por fuerza")
    print("4. Filtrar héroes por promedio de una key numérica")
    print("5. Buscar héroes por inteligencia")
    print("6. Exportar lista de héroes a CSV")
    print("7. Salir")

    # Validamos la opción ingresada por el usuario
    option = input("Ingrese una opción: ")
    if not re.match("^[1-7]$", option):
        print("Opción inválida. Intente nuevamente.")
        continue

    option = int(option)

    if option == 1:
        # Listar los primeros N héroes
        n = input("Ingrese la cantidad de héroes a listar: ")
        if not re.match("^[1-9][0-9]*$", n):
            print("Cantidad inválida. Intente nuevamente.")
            continue
        
        n = int(n)
        if n > len(heroes):
            print("Cantidad supera el número máximo de héroes. Intente nuevamente.")
            continue

        first_n_heroes = heroes[:n]
        print_heroes(first_n_heroes)
        
    elif option == 2:
        # Ordenar y listar héroes por altura
        orden = input("Ingrese 'mayor' para ordenar de mayor a menor o 'menor' para ordenar de menor a mayor: ")
        if orden != 'mayor' and orden != 'menor':
            print("Opción inválida. Intente nuevamente.")
            continue
        
        reverse = orden == 'mayor'
        sorted_heroes = sort_heroes_by(heroes, 'height', reverse)
        print_heroes(sorted_heroes)
