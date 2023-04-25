nombre_archivo = ""

#archivo = open(nombre_archivo, modo)

'''archivo = open('data_stark.py', 'r+')
texto = archivo.read()
print('el contenido ddel archivo es: ' + texto)
archivo.close()'''


'''# solo ves la cantidad de caracteres que pusiste en el parentecis 
archivo = open('data_stark.py', 'r+')
texto = archivo.read(10) 
print('el contenido del archivo es: ' + texto)
archivo.close()


#recorre todas la lista 
archivo = open('data_stark.py', 'r+')
lista_lineas = archivo.readlines()
for linea in lista_lineas:
    print(linea, end="")
archivo.close()


#lee una sola linea haasta el final
archivo = open('data_stark.py', 'r+')
print(archivo.tell())
linea = archivo.readline()
print(linea,end="")
print(archivo.tell())
archivo.close()
'''

'''archivo = open('data.txt', 'w')
archivo.write('primer linea de texto \n')
archivo.write('segunda linea de texto \n')
archivo.write('tercera linea de texto \n')
archivo.close()'''

'''archivo = open('archivo.txt', 'w')
lineas_texto = ['Primer linea de texto\n',
'segunda linea\n',
'tercera linea\n']
archivo.writelines(lineas_texto)
archivo.close()'''

archivo = open('archivo.txt', 'r+')
archivo.seek(11)
print(archivo.tell()) #Esta en el byte 11
linea = archivo.readline()
print(linea,end="") # Hola mundo
archivo.close()
