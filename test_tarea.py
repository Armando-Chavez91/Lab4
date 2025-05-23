import tarea
import pandas as pd

df = pd.DataFrame({
    "Survived": [1, 0, 1, 1],
    "Sex": ["male", "female", "female", "male"],
    "Age": [22, 38, 26, 35],
    "Pclass": [3, 1, 3, 2]
})

def test_probabilidad_basica():
    assert tarea.calcular_probabilidades(df) == 0.75

def test_probabilidad_condicional():
    assert tarea.probabilidad_condicional(df, "Sex", "female") == 0.5

