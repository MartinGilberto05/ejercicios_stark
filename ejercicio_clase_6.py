from data_stark import lista_personajes


def extraer_iniciales(nombre_heroe):
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

print(extraer_iniciales("Howard the Duck"))

