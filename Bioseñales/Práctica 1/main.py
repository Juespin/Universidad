# Juan Esteban Pineda Lopera
# C.C 1001248691

######################## REPASO DE NUMPY ########################
# Se importa la librería numpy con el seudónimo np y la libreria
# matplotlib.pyplot con el seudónimo plt.
import numpy as np
import matplotlib.pyplot as plt

# Se crea un par de vectores a y b
a = np.array([3.1, 1, -0.5, -3.2, 6])
b = np.array([1, 3, 2.2, 5.1, 1])

# Se realiza la multiplicación escalar de a y b con el método  
# dot().
c = a.dot(b)
print("a•b =", c)

# Se implementa la multiplicación punto a punto de a y b.
c = a*b
print("a*b =", c)

# Se crea una matriz A 3x3.
A = np.array([[2, -1, -3], [4, 1.5, -2.5], [7.3, -0.9, 0.2]])

# Se obtiene la matriz transpuesta de A.
AT = np.transpose(A)
print("A^T =\n", AT)

# Ejemplificando las funciones ones, round, ceil y floor.
#  - ones: Crea una matriz o vector de unos, 
#          enteros o flotantes.
unit_matrix = np.ones((3, 3), int)
print("Matriz de unos:\n", unit_matrix)

#  - round: Redondea los elementos de una matriz o vector a 
#           cierta cantidad de decimales.
example_matrix = np.array([[1.234, 2.345, 3.456], 
                           [4.567, 5.678, 6.789]])
rounded_matrix = np.round(example_matrix, 2)
print("Matriz redondeada a 2 decimales:\n", rounded_matrix)

# - ceil: Redondea los elementos de una matriz o vector al
#         entero superior más cercano.
ceiled_matrix = np.ceil(example_matrix)
print("Matriz redondeada al entero superior más cercano:\n", 
      ceiled_matrix)

# - floor: Redondea los elementos de una matriz o vector al
#          entero inferior más cercano.
floored_matrix = np.floor(example_matrix)
print("Matriz redondeada al entero inferior más cercano:\n", 
      floored_matrix)

# Accediendo al valor de la primera fila, tercera columna de 
# la matriz A e imprimiendolo.
value = A[0, 2]
print("Valor de la primera fila, tercera columna de A:", 
      value)

# Imprimiendo la segunda fila de la matriz A.
row = A[1]
print("Segunda fila de A:", row)

# Imprimiendo las dimensiones de la matriz A.
dimensions = A.shape
print(f"Dimensiones de A: \n {dimensions[0]} filas y \
{dimensions[1]} columnas")

# Construyendo la función y[n] = sin(π * 0.12n) con n 
# entre 0 y 100.
def y_1(n):
    return np.sin(np.pi * 0.12 * n)

n_range = np.arange(0, 101)
y_1_values = y_1(n_range)

# Construyendo la función y2[n] = cos(2π * 0.03n)
def y_2(n):
    return np.cos(2 * np.pi * 0.03 * n)

y_2_values = y_2(n_range)

# Generando una tercera señal que es suma de las dos 
# anteriores:
# s[n] = y[n] + y2[n]
# y otra que es su producto:
# t[n] = y[n] * y2[n]

s_values = y_1_values + y_2_values
t_values = y_1_values * y_2_values

# Graficando en la misma figura las señales y[n] y y2[n]
def graph(n, signal1, signal2, name1, name2):
    plt.figure(figsize=(10,5))
    plt.plot(n, signal1, label=name1, color='black')
    plt.plot(n, signal2, label=name2, color='red')
    plt.xlabel('Valores de n')
    plt.xlim(np.min(n), np.max(n))
    plt.ylabel('Valores de las señales')
    plt.title(f'Señales {name1} y {name2}')
    plt.legend()
    plt.grid()
    plt.show()

graph(n_range, y_1_values, y_2_values, 'y[n]', 'y2[n]')

# # Graficando en la misma figura las señales s[n] y t[n]
graph(n_range, s_values, t_values, 's[n]', 't[n]')

######################### REPASO PANDAS #########################
# Se importa la librería Pandas con el pseudónimo pd.
import pandas as pd

# Función que recibe diccionario con las notas de los alumnos de 
# un curso y devuelve una seria con la nota mínima, máxima, media
# y la desbviación típica.

# Se crea diccionario con las notas de los alumnos.
notas = {
    'Alumno1': [4.5, 3.2, 4.8],
    'Alumno2': [3.8, 4.0, 4.5],
    'Alumno3': [4.0, 3.5, 4.2],
    'Alumno4': [2.5, 3.0, 3.5],
    'Alumno5': [4.2, 4.5, 4.8],
}

def notas_estadisticas(notas):
    # Se crea un DataFrame a partir del diccionario de notas.
    df = pd.DataFrame(notas)

    # Se calculan las estadísticas.
    min_nota = df.min()
    max_nota = df.max()
    mean_nota = df.mean()
    std_nota = df.std()

    # Se crea un nuevo DataFrame con las estadísticas.
    estadisticas = pd.DataFrame({
        'Mínima': min_nota,
        'Máxima': max_nota,
        'Media': mean_nota,
        'Desviación Típica': std_nota
    })

    return estadisticas

print(f"Estadísticas de las notas de los alumnos:\n{notas_estadisticas(notas)}")

# Se cargan los datos desde "datos.csv" en un DataFrame.
data = pd.read_csv("datos.csv", sep=";", header=0)

# Se imprime la primera y última fila del DF para conocer la 
# estructura de los datos.
print("Primeras filas del DataFrame:\n", data.head())
print("Últimas filas del DataFrame:\n", data.tail())

# Borrar la columna "Unnamed: 0" del DataFrame.
data = data.drop("Unnamed: 0", axis=1)

# Calcular el IMC con la formula IMC = peso(kg) / altura(m)^2,

# Intercambiando los datos de las columnas "Weight" y "Height".
data["Weight"], data["Height"] = data["Height"], data["Weight"]

# Conociendo que la altura se entrega en cm.
IMC = data["Weight"] / (data["Height"]/100)**2

# Agregando el IMC como nueva columna llamda "BMI".
data["BMI"] = IMC

# Categorizar los participantes según su IMC en:
#  - Bajo peso: IMC < 18.5
#  - Normal: 18.5 <= IMC < 25
#  - Sobrepeso: 25 <= IMC < 30
#  - Obesidad: IMC >= 30

def categorize_IMC(IMC):
    if IMC < 18.5:
        return "Bajo peso"
    elif IMC < 25:
        return "Normal"
    elif IMC < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"

for IMC in data["BMI"]:
    data["Category"] = data["BMI"].apply(categorize_IMC)

print("DataFrame con la columna BMI y Category:\n", data)