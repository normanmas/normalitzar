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

## Cicle de programació (18/7/26)  
L'aplicació realitzarà una sèrie de comprovacions i deteccions, per fer la proposta de normalització sols a als arxius que disponguin de columnes adients per normalitzar.  

Aquest procès es realitzarà en diferents fases:  
Fase 1 - Càrrega i validació
1. Triar arxiu
    Seleccionar un dels arxius proposat o triar un de nou.  
2. Llegir CSV
    Realitzar la lectura de l'arxiu. De moment sols CSV.
3. Detectar capçalera
    Detecció si l'arxiu ja disposa de capçalera. En cas negatiu se'n crea una de nova.
4. Verificar mínim 3 files
    Verificar que l'arxiu tingui un mínim de dades per poder treballar.

Fase 2 - Inspecció de dades  
5. Detectar columnes numèriques
    Separar les columnes numèriques de les que no són per poder normalitzar.
6. Detectar columnes ID / autonumèriques
    Descomptar les columnes que sí són numèriques però pertanyen a columnes identificadores del registre, donat que no s'han de normalitzar.
7. Detectar columnes categòriques numèriques
    Desmarcar les columnes considerades categòriques per normalitzar, considerant que deuen de ser enters i amb els valors repetits (pocs valors únicas sobre el total de valors).
8. Detectar valors buits
9. Detectar patró dels buits
10. Detectar columnes ja normalitzades

Fase 3 - Diagnòstic estadístic  
10. Detectar outliers
11. Analitzar distribució

Fase 4 - Decisions  
12. Decidir imputació / descartar
13. Triar algorisme de normalització

Fase 5 - Transformació  
14. Normalitzar
15. Guardar nou CSV


## Funcions creades  
1. minim_tres_files(). Detectar que l'ariu seleccionat conté un mínim de 3 files per poder normalitzar.
2. capcalera(). Detectar si l'arxiu conté una capçalera.
3. PENDENT D'ACTUALITZACIÓ EN FUNCIÓ DE LA SEVA EVOLUCIÓ....
