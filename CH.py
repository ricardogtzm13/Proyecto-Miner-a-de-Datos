import pandas as pd
from scipy.stats import chi2_contingency

# Cargar el archivo CSV
data = pd.read_csv('C:/Users/RICARDO/Desktop/8vo Semestre/Mineria de datos/nuevo_dataset.csv')

# Seleccionar las columnas que se utilizarán para el análisis
column1 = 'COLUMNA 1'
column2 = 'COLUMNA 2'

# Crear una tabla de contingencia utilizando las dos columnas
contingency_table = pd.crosstab(data[column1], data[column2])

# Calcular el valor de chi-cuadrado y el p-valor
chi2, p, _, _ = chi2_contingency(contingency_table)

# Calcular el coeficiente de contingencia de Tschuprow
tschuprow = (chi2 / (chi2 + len(data))) ** 0.5

# Imprimir los resultados
print(f'Valor de chi-cuadrado: {chi2}')
print(f'Coeficiente de contingencia de Tschuprow: {tschuprow}')
