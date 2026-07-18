# Aplicació per aprendre els conceptes de normalitzar les dades.

# Importar llibreries
from pathlib import Path as Ruta
import subprocess
from funcions_manuals import (
    llegir_CSV,
    capcalera,
    minim_tres_files,
    detectar_columnes_numeriques,
    detectar_columnes_id,
    analitzar_valors_buits_columnes_numeriques,
    detectar_patro_buits,
    detectar_columnes_normalitzades,
    preparar_columnes_per_normalitzar,
    detectar_outliers,
    analitzar_distribucio,
    detectar_columnes_categoriques_numeriques
)

# Inicialitzar l'aplicació
# Neteja de pantalla (linux)
subprocess.run(["clear"])   # Es passa la comanda com una llista
# Procès de selecció de l'arxiu a normalitzar
print(
    "Aquesta aplicació normalitza arxius de dades per",
    "poder emprar-los en altres aplicacions, xarxes neuronals.")

directori_projecte = Ruta(__file__).resolve().parent    # Esbrinar directori actual
directori_dades = directori_projecte / "dades"

arxius = sorted(directori_dades.glob('*.csv'))

print('\n Arxius disponibles:')

for posicio, arxiu in enumerate(arxius,
                               start=1  # Indica començar el bucle en 1 ennloc de 0
                               ):
    print(f'{posicio}, {arxiu.name}')

print("\nTambé es pot introduir directament la ruta d'un altre arxiu.")

seleccio = input(
    'Tria un número, escriu una ruta o prem Intro per usar cotxes.csv: '
).strip()

if seleccio =='':
    ruta_arxiu = directori_dades / 'cotxes.csv' # Selecció genèrica

elif seleccio.isdigit():    # Han triat un número i es verifica que sigui vàlid
    numero = int(seleccio)
    if 1 <= numero <= len(arxius):  # El número està dintre del rang vàlid
        ruta_arxiu = arxius[numero-1]
    else:
        raise SystemExit("El número seleccionat no és vàlid.")
else:
    ruta_arxiu = Ruta(seleccio).expanduser()

if not ruta_arxiu.is_file():
    raise SystemExit(f"No s'ha trobat l'arxiu: {ruta_arxiu}")
print(f'\nArxiu seleccionat: {ruta_arxiu}')
files = llegir_CSV(ruta_arxiu)


# Verificar si el CSV té capçalera
conte_capcalera = capcalera(files)

if conte_capcalera:
    print("El CSV conté una capçalera.")
else:
    print("No s'ha detectat cap capçalera.")

# Verificar que l'arxiu té un mínim de tres files
if not minim_tres_files(files, conte_capcalera):
    raise SystemExit(
        "El CSV ha de contenir almenys 3 files de dades."
    )

# Detecció i caracterització de les columnes
# Identificar les columnes numèriques
columnes_numeriques = detectar_columnes_numeriques(
    files,
    conte_capcalera
)
print(f'Columnes numèriques detectades: {columnes_numeriques}')


# Detecció de columnes id o autonumèriques
# Aquest tipus de columnes NO cal normalitzar
columnes_id = detectar_columnes_id(
    files,
    conte_capcalera,
    columnes_numeriques
)
print('\n Columnes que semblen identificadors:')

if not columnes_id:
    print("No s'han detectat columnes ID.")

else:
    for columna in columnes_id:
        print(
            columna['columna'],
            ' - nom sembla ID:',
            columna['nom_sembla_id'],
            '- autonumèrica',
            columna['es_autonumerica']
        )

# Creació de la llista de columnes numèriques excepte les ID
noms_columnes_id = []
for columna in columnes_id:
    noms_columnes_id.append(columna['columna'])

columnes_per_analitzar = []
for columna in columnes_numeriques:
    if columna not in noms_columnes_id:
        columnes_per_analitzar.append(columna)
print("\nColumnes que es faran servir per l'anàlisi:")
print(columnes_per_analitzar)


# Detecció de columnes categòriques numèriques
# Aquestes columnes no s'han de normalitzar
columnes_categoriques = detectar_columnes_categoriques_numeriques(
    files,
    conte_capcalera,
    columnes_per_analitzar
)

print('\nColumnes numèriques que semblen categòriques:')

if not columnes_categoriques:
    print("No s'han detectat columnes categòriques numèriques.")
else:
    for columna in columnes_categoriques:
        print(
            columna['columna'],
            '- tipus',
            columna['tipus'],
            '- valors unics:',
            columna['valors_unics']
        )

# Creació de la nova llista per treballar, sense les columnes categòqiues
noms_columnes_categoriques = []

for columna in columnes_categoriques:
    noms_columnes_categoriques.append(columna['columna'])

columnes_continues = []

for columna in columnes_per_analitzar:
    if columna not in noms_columnes_categoriques:
        columnes_continues.append(columna)

print('\nColumnes contínues candidates a normalització:')
print(columnes_continues)


# Analitzar els valors buits en les columnes numèriques
resum_buits = analitzar_valors_buits_columnes_numeriques(
    files,
    conte_capcalera,
    columnes_continues
)

print("\nAnàlisi de valors buits en columnes numèriques:")

for resum in resum_buits:
    print(
        resum["columna"],
        "- buits:",
        resum["total_buits"],
        "- percentatge:",
        round(resum["percentatge_buits"], 2),
        "%",
        "- recomanació:",
        resum["recomanacio"]
    )

patro_buits = detectar_patro_buits(
    files,
    conte_capcalera,
    columnes_continues
)

print("\nPatró dels valors buits:")

if not patro_buits:
    print("No s'han detectat valors buits.")
else:
    for patro in patro_buits:
        print(
            patro["columna"],
            "- total buits:",
            patro["total_buits"],
            "- patró:",
            patro["tipus_patro"],
            "- primera fila:",
            patro["primera_fila_buida"],
            "- última fila:",
            patro["ultima_fila_buida"],
            "- amplada:",
            round(patro["percentatge_amplada"], 2),
            "%"
        )

# Bloc sobre columnes ja normalitzades
columnes_normalitzades = detectar_columnes_normalitzades(
    files,
    conte_capcalera,
    columnes_continues
)

print("\nColumnes que ja semblen normalitzades:")

if not columnes_normalitzades:
    print("No s'han detectat columnes normalitzades.")
else:
    for columna in columnes_normalitzades:
        print(
            columna["columna"],
            "- tipus:",
            columna["tipus"],
            "- mínim:",
            columna["valor_minim"],
            "- màxim:",
            columna["valor_maxim"]
        )


# Bloc sobre la detecció de outliers
resum_outliers = detectar_outliers(
    files,
    conte_capcalera,
    columnes_continues
)

print("\nAnàlisi d'outliers:")

for resum in resum_outliers:
    print(
        resum["columna"],
        "- outliers:",
        resum["total_outliers"],
        "- percentatge:",
        round(resum["percentatge_outliers"], 2),
        "%",
        "- límit inferior:",
        round(resum["limit_inferior"], 2),
        "- límit superior:",
        round(resum["limit_superior"], 2)
    )


# Bloc sobre la distribució
resum_distribucio = analitzar_distribucio(
    files,
    conte_capcalera,
    columnes_continues
)

print("\nAnàlisi de distribució:")

for resum in resum_distribucio:
    print(
        resum["columna"],
        "- mínim:",
        round(resum["valor_minim"], 2),
        "- màxim:",
        round(resum["valor_maxim"], 2),
        "- mitjana:",
        round(resum["mitjana"], 2),
        "- mediana:",
        round(resum["mediana"], 2),
        "- desviació típica:",
        round(resum["desviacio_tipica"], 2),
        "- distribució:",
        resum["tipus_distribucio"]
    )
