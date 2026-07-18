# Normalització de dades

## Objectiu educatiu

L'objectiu d'aquesta aplicació és aprendre i practicar els conceptes de
normalització de dades amb l'ajuda d'una IA.

En una primera fase, les operacions s'implementaran manualment.  
En una segona fase, es repetiran emprant llibreries especialitzades com `scikit-learn`.

Donada la finalitat d'aprenentatge de l'exercici, en la primera fase el codi no està optimitzat, per facilitar la seva lectura i és ple de comentaris.  

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

Es generen diferents versions d'alguns datasets per poder fer proves.  
El programa també permet indicar la ruta d'un altre arxiu CSV.

## Cicle de programació (18/7/26)

L'aplicació realitza una sèrie de comprovacions i deteccions abans de proposar cap normalització.  
L'objectiu és evitar normalitzar columnes que no són adequades, com identificadors, categories numèriques o variables que ja estan normalitzades.

A nivell conceptual, el procés actual és:

```text
CSV → columnes numèriques → eliminar ID → eliminar categòriques → buits → outliers → distribució → decisió → normalització
```

### Fase 1 - Càrrega i validació

1. Triar arxiu  
   Seleccionar un dels arxius proposats o introduir manualment una ruta.

2. Llegir CSV  
   Llegir l'arxiu una sola vegada i guardar-ne el contingut en una llista de files.

3. Detectar capçalera  
   Detectar si l'arxiu disposa de capçalera.

4. Verificar mínim 3 files  
   Verificar que l'arxiu tingui un mínim de dades per poder treballar.

### Fase 2 - Inspecció de dades

5. Detectar columnes numèriques  
   Separar les columnes numèriques de les columnes de text.

6. Detectar columnes ID / autonumèriques  
   Excloure columnes com `PassengerId`, que són numèriques però només identifiquen registres.

7. Detectar columnes categòriques numèriques  
   Excloure columnes com `Survived`, `Pclass`, `SibSp` o `Parch`, que són numèriques però representen categories.

8. Crear llista de columnes contínues  
   Crear una llista final de columnes candidates a normalització.

### Fase 3 - Qualitat de dades

9. Detectar valors buits  
   Calcular el nombre i percentatge de valors buits per columna.

10. Detectar patró dels buits  
    Analitzar si els buits apareixen al principi, al final, concentrats o repartits.

11. Detectar columnes ja normalitzades  
    Comprovar si alguna columna contínua ja està en rang `0-1`.

### Fase 4 - Diagnòstic estadístic

12. Detectar outliers  
    Detectar valors extrems amb el mètode IQR.

13. Analitzar distribució  
    Calcular mínim, màxim, mitjana, mediana, desviació típica i tipus de distribució.

### Fase 5 - Decisions

14. Decidir imputació / descart  
    Decidir què fer amb columnes que tenen valors buits.

15. Triar algorisme de normalització  
    Recomanar una estratègia segons buits, outliers i distribució.

### Fase 6 - Transformació

16. Normalitzar  
    Aplicar la normalització manual.

17. Guardar nou CSV  
    Exportar el resultat en un nou arxiu.

## Estat actual del projecte

Actualment el programa ja permet:

- seleccionar un CSV del directori `dades`
- indicar una ruta manualment
- usar `cotxes.csv` per defecte
- llegir el CSV una sola vegada
- detectar si hi ha capçalera
- verificar que hi ha almenys 3 files de dades
- detectar columnes numèriques
- detectar columnes ID o autonumèriques
- detectar columnes categòriques numèriques
- crear una llista de columnes contínues candidates a normalització
- detectar valors buits
- classificar el percentatge de valors buits
- detectar patrons bàsics dels valors buits
- detectar columnes que ja semblen normalitzades
- detectar outliers amb IQR
- analitzar la distribució de les columnes contínues

Encara està pendent:

- decidir com imputar valors buits
- recomanar l'algorisme de normalització
- implementar normalització Min-Max manual
- implementar normalització Z-score manual
- implementar normalització robusta manual
- guardar un nou CSV normalitzat
- repetir el procés amb `scikit-learn`

## Funcions creades

### Càrrega i validació

- `llegir_CSV()`  
  Llegeix l'arxiu CSV i retorna les files com una llista de llistes.

- `capcalera()`  
  Detecta de manera aproximada si el CSV conté capçalera.

- `minim_tres_files()`  
  Verifica que el CSV tingui almenys 3 files de dades.

### Detecció de tipus de columnes

- `es_numero()`  
  Comprova si un valor es pot convertir a número.

- `detectar_columnes_numeriques()`  
  Detecta quines columnes són numèriques.

- `detectar_columnes_id()`  
  Detecta columnes que semblen identificadors o seqüències autonumèriques.

- `detectar_columnes_categoriques_numeriques()`  
  Detecta columnes numèriques que probablement representen categories.

### Valors buits

- `es_valor_buit()`  
  Detecta valors buits com `""`, `NA`, `N/A`, `NaN`, `NULL` o `None`.

- `analitzar_valors_buits_columnes_numeriques()`  
  Calcula el nombre i percentatge de valors buits per columna.

- `detectar_patro_buits()`  
  Analitza si els valors buits estan concentrats, repartits, al principi o al final.

### Normalització prèvia

- `detectar_columnes_normalitzades()`  
  Detecta si una columna ja sembla normalitzada en rang `0-1`.

- `preparar_columnes_per_normalitzar()`  
  Classifica columnes segons si es poden normalitzar, si tenen buits o si ja estan normalitzades.  
  Actualment encara no està integrada del tot en el flux principal.

### Outliers i distribució

- `calcular_quartil()`  
  Calcula quartils manualment.

- `detectar_outliers()`  
  Detecta outliers amb el mètode IQR.

- `calcular_mitjana()`  
  Calcula la mitjana.

- `calcular_mediana()`  
  Calcula la mediana.

- `calcular_desviacio_tipica()`  
  Calcula la desviació típica.

- `analitzar_distribucio()`  
  Analitza estadístics bàsics i classifica la distribució de cada columna.
