# Normalització de dades

## Objectiu educatiu

L'objectiu d'aquesta aplicació és aprendre i practicar els conceptes de
normalització de dades amb l'ajuda d'una IA.

En una primera fase, les operacions s'implementaran manualment. En una segona
fase, es repetiran emprant llibreries especialitzades com `scikit-learn`.

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


## Funcions creades  
1. minim_tres_files(). Detectar que l'ariu seleccionat conté un mínim de 3 files per poder normalitzar.
2. capcalera(). Detectar si l'arxiu conté una capçalera.
