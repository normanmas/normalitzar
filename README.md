# Normalització de dades

## Objectiu educatiu

L'objectiu d'aquesta aplicació és aprendre i practicar els conceptes de
normalització de dades amb l'ajuda d'una IA.

En una primera fase, les operacions s'implementaran manualment.  
En una segona fase, es repetiran emprant llibreries especialitzades com `scikit-learn`.

Donada la finalitat d'aprenentatge de l'exercici, en la primera fase el codi no está optimitzat, per facilitar la seva lectura i és ple de comentaris.  

A nivell conceptual l'exercici serà:  
 Valors buits → Outliers → Distribució → Algorisme


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

Es generen diferents version d'alguns datasets per poder fer proves.  
El programa també permet indicar la ruta d'un altre arxiu CSV.

## Cicle de programació (12/7/26)  
Fase 1 - Càrrega i validació
1. Triar arxiu
2. Llegir CSV
3. Detectar capçalera
4. Verificar mínim 3 files

Fase 2 - Inspecció de dades  
5. Detectar columnes numèriques
6. Detectar valors buits
7. Detectar patró dels buits
8. Detectar columnes ja normalitzades

Fase 3 - Diagnòstic estadístic  
9. Detectar outliers
10. Analitzar distribució

Fase 4 - Decisions  
11. Decidir imputació / descart
12. Triar algorisme de normalització

Fase 5 - Transformació  
13. Normalitzar
14. Guardar nou CSV

## Funcions creades  
1. minim_tres_files(). Detectar que l'ariu seleccionat conté un mínim de 3 files per poder normalitzar.
2. capcalera(). Detectar si l'arxiu conté una capçalera.
3. PENDENT D'ACTUALITZACIÓ EN FUNCIÓ DE LA SEVA EVOLUCIÓ....
