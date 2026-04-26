import numpy as np
import matplotlib.pyplot as plt

# 1. Generar 100 datos aleatorios (Media=150, Desvío=20)
np.random.seed(22) # Para que los resultados sean replicables
#*""" 
# np.random.normal, genera elementos que sigan la distribucion normal
# loc es la media a la qe queremos apuntar
# scale es el desvio estandar respecto al promedio
# size es la cantidad de elementos de la muestra
#  """
datos = np.random.normal(loc=150, scale=20, size=100)

# 2. Cálculos estadísticos
#np.mean suma los valores generados y luego los divide por la cantidad de valores
media = np.mean(datos)
#np.std que tan lejos esta cada dato del promedio
desvio = np.std(datos)
#np.var desvio estandar al cuadrado (se usa para analisis)

media = np.mean(datos)
desvio = np.std(datos)
varianza = np.var(datos)



print(f"Media: {media:.2f}")
print(f"Desvío Estándar: {desvio:.2f}")
print(f"Varianza: {varianza:.2f}")

plt.hist(datos, bins=20, color='green', edgecolor='black')
plt.title('Distribución de Pesos de Manzanas')
plt.xlabel('Gramos')
plt.ylabel('Frecuencia')
plt.show()
