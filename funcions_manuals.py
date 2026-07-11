# En aquest arxiu es crearan les funcions manuals de normalització

# Importar llibreries
import csv


# Funció per importar el CSV
def llegir_CSV(ruta_arxiu):
    with open(
        ruta_arxiu,
        mode='r',
        encoding='UTF-8',
        newline=''
    ) as arxiu:
        lector_csv = csv.reader(arxiu)
        files = list(lector_csv)
    return files

# Verificar si un valor és numèric
def es_numero(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False


# Funció per verificar si el CSV a normalitzar conté capçalera de variables
'''
Serà una funció aproximada, comparant la primera fila amb la segona.
Si la primera conté text i la segona conté números a les mateixes columnes, és que segurament hi ha capçalera.
'''
def capcalera(files):
    if len(files) < 2:
        return False

    primera_fila = files[0]
    segona_fila = files[1]
    coincidencies = 0

    for primer_valor, segon_valor in zip(primera_fila, segona_fila):
        primer_es_text = not es_numero(primer_valor)
        segon_es_numero = es_numero(segon_valor)

        if primer_es_text and segon_es_numero:
            coincidencies += 1
    
    return coincidencies > 0


# Funció per verificar el número mínim de tres files de dades
def minim_tres_files (files, conte_capcalera):
    nombre_files = len(files)
        
    # Es verifica que tingui capçalera
    if conte_capcalera:
        nombre_files -= 1

    return nombre_files >= 3


# Funció per detectar les columnes númeriques.
def detectar_columnes_numeriques(files, conte_capcalera):

    if not files:   # Verificar que hi han files
        return[]
    
    if conte_capcalera:     # Assignat els noms de capçalera de la primera fila
        noms_columnes = files[0]
        files_dades = files[1:]
    else:
        files_dades = files
        noms_columnes = []

        # Com no hi han noms de columnes, se n'assignen de nous
        for posicio in range(len(files[0])):
            noms_columnes.append(f"columna_{posicio + 1}")

    columnes_numeriques = []

    for posicio_columna in range(len(noms_columnes)):
        columna_es_numerica = True

        for fila in files_dades:
            valor = fila[posicio_columna]

            if not es_numero(valor):
                columna_es_numerica = False

        if columna_es_numerica:
            columnes_numeriques.append(noms_columnes[posicio_columna])

    return columnes_numeriques
