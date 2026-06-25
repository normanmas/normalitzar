# En aquest arxiu es crearan les funcions manuals de normalització

# Importar llibreries
import csv

# Funció per verificar el número mínim de tres files de dades
def minim_tres_files (ruta_arxiu, capçalera):
    with open(ruta_arxiu,
              mode='r',
              encoding='utf-8',
              newline=''
              ) as arxiu:
        lector_csv = csv.reader(arxiu)
        
        # Es verifica que tingui capçalera
        if capcalera:
            next(lector_csv, None)

        nombre_files = 0
        # Bucle per contar les files
        for fila in lector_csv:
            if fila:
                nombre_files +=1
            # Es retorna True a l'arribar a 3 files mínim. No cal llegir tot l'arxiu
            if nombre_files >=3:
                return True
    return False

# Funció per verificar si el CSV a normalitzar conté capçalera de variables
'''
Serà una funció aproximada, comparant la primera fila amb la segona.
Si la primera conté text i la segona conté números a les mateixes columnes, és que segurament hi ha capçalera.
'''
def es_numero(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

def capcalera(ruta_arxiu):
    with open(
        ruta_arxiu,
        mode='r',
        encoding='utf-8',
        newline=''
    ) as arxiu:
        lector_csv = csv.reader(arxiu)

        primera_fila = next(lector_csv, None)
        segona_fila = next(lector_csv, None)
    
    if primera_fila is None or segona_fila is None:
        return False
    
    coincidencies = 0
    for primer_valor, segon_valor in zip(primera_fila, segona_fila):
        primer_es_text = not es_numero(primer_valor)
        segon_es_numero = es_numero(segon_valor)

        if primer_es_text and segon_es_numero:
            coincidencies += 1
    
    return coincidencies > 0