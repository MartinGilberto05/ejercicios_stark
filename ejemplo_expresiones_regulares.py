import re

nombre = "Howard the Duck"
nombre = nombre.replace('-',' ')
#                  condicion // el texto en donde buscar
result = re.findall("(?!the)[A-Z]", nombre)

inicial = '.'.join(result.upper()for result in result)
print(inicial + '.')
