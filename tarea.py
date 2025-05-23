import pandas as pd
import numpy as np
from scipy import stats

def calcular_probabilidades(df):
    total = len(df)
    sobrevivientes = df[df['Survived'] == 1]
    return len(sobrevivientes) / total

def probabilidad_condicional(df, columna, valor):
    subset = df[df[columna] == valor]
    return subset['Survived'].mean()

def medidas_tendencia_central(df, columna):
    return {
        "media": df[columna].mean(),
        "mediana": df[columna].median(),
        "moda": df[columna].mode()[0]
    }

def medidas_dispersion(df, columna):
    return {
        "varianza": df[columna].var(),
        "desviacion_estandar": df[columna].std()
    }

def distribucion_categoria(df, columna):
    return df.groupby(columna)['Survived'].mean()


import seaborn as sns
import matplotlib.pyplot as plt

sns.barplot(data=df, x='Sex', y='Survived')
plt.title("Supervivencia por Género")
plt.show()

sns.catplot(data=df, x="Pclass", hue="Sex", y="Survived", kind="bar")
plt.title("Supervivencia por Clase y Sexo")
plt.show()

sns.histplot(data=df, x="Age", bins=30, hue="Survived", kde=True, multiple="stack")
plt.title("Distribución de Edad y Supervivencia")
plt.show()
