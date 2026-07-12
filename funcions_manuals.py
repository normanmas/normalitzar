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

            if not es_numero(valor) and not es_valor_buit(valor):
                columna_es_numerica = False

        if columna_es_numerica:
            columnes_numeriques.append(noms_columnes[posicio_columna])

    return columnes_numeriques


# Funció per avaluar si un valor és buit
def es_valor_buit(valor):
    valor_net = valor.strip()

    valors_buits = [
        "",
        "NA",
        "N/A",
        "NaN",
        "nan",
        "NULL",
        "None",
    ]

    return valor_net in valors_buits


# Funció per detectar el numbre de valors buits en les columnes pel seu tractament posterior
def analitzar_valors_buits_columnes_numeriques(
    files,
    conte_capcalera,
    columnes_numeriques
):

    if conte_capcalera:
        noms_columnes = files[0]
        files_dades = files[1:]
    else:
        files_dades = files
        noms_columnes = []

        for posicio in range(len(files[0])):
            noms_columnes.append(f"columna_{posicio + 1}")

    resum_buits = []

    for nom_columna in columnes_numeriques:
        posicio_columna = noms_columnes.index(nom_columna)

        total_files = len(files_dades)
        total_buits = 0

        for fila in files_dades:
            valor = fila[posicio_columna]

            if es_valor_buit(valor):
                total_buits += 1

        percentatge_buits = total_buits / total_files * 100

        if percentatge_buits == 0:
            recomanacio = "sense_buits"
        elif percentatge_buits >= 30 and percentatge_buits <= 50:
            recomanacio = "no_val_la_pena_normalitzar"
        elif percentatge_buits >= 5 and percentatge_buits <= 15:
            recomanacio = "preguntar_si_imputar"
        elif percentatge_buits > 15 and percentatge_buits < 30:
            recomanacio = "consultar_si_emplenar"
        elif percentatge_buits > 50:
            recomanacio = "descartar_columna"
        else:
            recomanacio = "pocs_buits"

        resum_columna = {
            "columna": nom_columna,
            "total_files": total_files,
            "total_buits": total_buits,
            "percentatge_buits": percentatge_buits,
            "recomanacio": recomanacio
        }

        resum_buits.append(resum_columna)

    return resum_buits


# Funció per detectar patron en les columnes numèriques amb buits.
def detectar_patro_buits(
        files,
        conte_capçalera,
        columnes_numeriques
):
    # Verificar si conté capçalera
    if conte_capçalera:
        noms_columnes = files[0]
        files_dades = files[1:]
    else:
        files_dades = files
        noms_columnes = []

        for posicio in range(len(files[0])):
            noms_columnes.append(f'columna_{posicio + 1}')

    patro_buits = []

    for nom_columna in columnes_numeriques:
        posicio_columna = noms_columnes.index(nom_columna)
        files_buides = []

        for posicio_fila, fila in enumerate(files_dades, start=1):
            valor = fila[posicio_columna]

            if es_valor_buit(valor):
                files_buides.append(posicio_fila)

        if files_buides:
            total_files = len(files_dades)
            primera_fila_buida = files_buides[0]
            ultima_fila_buida = files_buides[-1]
            amplada_patro = ultima_fila_buida - primera_fila_buida + 1
            percentatge_amplada = amplada_patro / total_files * 100

            if ultima_fila_buida <= total_files * 0.25:
                tipus_patro = "buits_al_principi"
            elif primera_fila_buida >= total_files * 0.75:
                tipus_patro = "buits_al_final"
            elif percentatge_amplada <= 30:
                tipus_patro = "buits_concentrats"
            else:
                tipus_patro = "buits_repartits"

            resum_columna = {
                "columna": nom_columna,
                "files_buides": files_buides,
                "primera_fila_buida": primera_fila_buida,
                "ultima_fila_buida": ultima_fila_buida,
                "total_buits": len(files_buides),
                "amplada_patro": amplada_patro,
                "percentatge_amplada": percentatge_amplada,
                "tipus_patro": tipus_patro
            }

            patro_buits.append(resum_columna)

    return patro_buits

# Funció per detectar si les columnes de l'arxiu ja estan normalitzades previament i no cal tornar a fer-ho.
"""
Queda pendent buscar algun mètode per poder discriminar les columnes categòriques com 0 o 1 (True o False)
Donat que ja hi són a un rang entre 0 i 1
Estaria basat en la detecció de valors de la columna binaris al 100%
"""
def detectar_columnes_normalitzades(
        files,
        conte_capcalera,
        columnes_numeriques
):
    # Indicar el rang per si conté capçalera
    if conte_capcalera:
        noms_columnes = files[0]
        files_dades = files[1:]
    else:
        files_dades = files
        noms_columnes = []

        for posicio in range(len(files[0])):
            noms_columnes.append(f"columna_{posicio + 1}")

    columnes_normalitzades = []

    for nom_columna in columnes_numeriques:
        posicio_columna = noms_columnes.index(nom_columna)
        valors = []

        for fila in files_dades:
            valor = fila[posicio_columna]

            if es_numero(valor):
                valors.append(float(valor))

        if not valors:
            continue

        valor_minim = min(valors)
        valor_maxim = max(valors)

        if valor_minim >= 0 and valor_maxim <= 1:
            resum_columna = {
                "columna": nom_columna,
                "valor_minim": valor_minim,
                "valor_maxim": valor_maxim,
                "tipus": "min_max"
            }

            columnes_normalitzades.append(resum_columna)

    return columnes_normalitzades