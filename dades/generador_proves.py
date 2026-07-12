"""
Aquest arxiu, serveix per agafar l'arxiu de dades iris.csv i eliminar uns quant valors aleatòriament,
de manera que permetrà avaluar la funció de detecció de "forats" dintre dels arxius de dades abans de normalitzar.
"""

# Importar llibreries
import os
import pandas as pd
import numpy as np

arxiu = 'iris.csv'
# 1. Carregar l'arxiu original en un dataframe de pandas
df = pd.read_csv(arxiu)

# 2. Crear una còpia del df
df_buits = df.copy()

# 3. Escollir una columna i generar buits de manera aleatòria
# Modifica el 'frac' per simular diferents escenaris (0.1 = 10% de buits, 0.4 = 40%)
percentatge_buits = 0.15

valors_a_esborrar = (
    df_buits['SepalWidthCm']
    .sample(frac=percentatge_buits, random_state=42)
    .index
)
df_buits.loc[valors_a_esborrar, 'SepalWidthCm'] = np.nan

# 4. Guardar el nou arxiu per les pràctiques
nom_base, extensio = os.path.splitext(arxiu)
nou_arxiu = nom_base + '_amb_forats' + extensio
df_buits.to_csv(nou_arxiu, index=False)

# Mostrar resultats
print(f'Arxiu guardat correctament com a: {nou_arxiu}')
print(df_buits.isnull().sum())