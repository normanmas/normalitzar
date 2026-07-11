# Aplicació per aprendre els conceptes de normalitzar les dades.

# Importar llibreries
from pathlib import Path as Ruta
from funcions_manuals import (
    llegir_CSV,
    capcalera,
    minim_tres_files,
    detectar_columnes_numeriques
)

# Consultar sistema de normalització
print(
    "Aquesta aplicació normalitza arxius de dades per ",
    "poder emprar-los en altres aplicacions.")

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
    if 1 <= numero <= len(arxius):
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

# Identificar les columnes numèriques
columnes_numeriques = detectar_columnes_numeriques(
    files,
    conte_capcalera
)

print(f'Columnes numèriques detectades: {columnes_numeriques}')
