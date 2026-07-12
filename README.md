# Normalització de dades

## Objectiu educatiu

L'objectiu d'aquesta aplicació és aprendre i practicar els conceptes de
normalització de dades amb l'ajuda d'una IA.

En una primera fase, les operacions s'implementaran manualment.  
En una segona fase, es repetiran emprant llibreries especialitzades com `scikit-learn`.

Donada la finalitat d'aprenentatge de l'exercici, en la primera fase el codi no está optimitzat, per facilitar la seva lectura i és ple de comentaris.

Aquest exercici està escrit en català.  

## Datasets  

El directori `dades` inclou diversos datasets estàndard per fer les pràctiques:

- `iris.csv`: [Iris, UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/53/iris)
  (llicència CC BY 4.0).
- `cotxes.csv`: [Auto MPG, UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/9/auto+mpg)
  (llicència CC BY 4.0).
- `pinguins.csv`: [Palmer Penguins](https://github.com/allisonhorst/palmerpenguins)
  (dades amb llicència CC0).
- `propines.csv`: [Tips, repositori de dades d'exemple de Seaborn](https://github.com/mwaskom/seaborn-data/blob/master/tips.csv).
- `titanic.csv`: [Titanic: Machine Learning from Disaster, Kaggle](https://www.kaggle.com/c/titanic/data).

El programa també permet indicar la ruta d'un altre arxiu CSV.

## Cicle de programació (12/7/26)  
1. Triar arxiu
2. Llegir CSV
3. Detectar capçalera
4. Verificar mínim 3 files
5. Detectar columnes numèriques
6. Analitzar valors buits
7. Detectar si les columnes ja estan normalitzades
8. Decidir si cal imputar / descartar / normalitzar
9. Triar columna
10. Normalitzar

## Funcions creades  
1. minim_tres_files(). Detectar que l'ariu seleccionat conté un mínim de 3 files per poder normalitzar.
2. capcalera(). Detectar si l'arxiu conté una capçalera.
3. PENDENT D'ACTUALITZACIÓ EN FUNCIÓ DE LA SEVA EVOLUCIÓ....
