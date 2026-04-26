import numpy as np
import matplotlib.pyplot as plt

# 0. Semilla para que los gráficos no cambien cada vez que corres el código
np.random.seed(42)

lam = 3
param_scale = 1/lam  # En NumPy, scale = 1/lambda

# 1. Generación de las tres muestras
muestra_100 = np.random.exponential(scale=param_scale, size=100)
muestra_1000 = np.random.exponential(scale=param_scale, size=1000)
muestra_10000 = np.random.exponential(scale=param_scale, size=10000)

# 2. Configuración de los gráficos (3 subplots en una fila)
fig, axs = plt.subplots(1, 3, figsize=(18, 5))

# Gráfico para N = 100
axs[0].hist(muestra_100, bins=20, color='lightcoral', edgecolor='black', density=True)
axs[0].set_title('Muestra N=100')
axs[0].set_ylabel('Densidad')

# Gráfico para N = 1000
axs[1].hist(muestra_1000, bins=30, color='lightseagreen', edgecolor='black', density=True)
axs[1].set_title('Muestra N=1000')

# Gráfico para N = 10000
axs[2].hist(muestra_10000, bins=50, color='cornflowerblue', edgecolor='black', density=True)
axs[2].set_title('Muestra N=10000')

# Ajustes estéticos finales
for ax in axs:
    ax.set_xlabel('Valor')
    ax.grid(axis='y', alpha=0.3)


# Punto 4
muestras = [muestra_100, muestra_1000, muestra_10000]
nombres = ["N=100", "N=1000", "N=10000"]

print(f"{'Muestra':<10} | {'Media':<10} | {'Desvío Std':<10} | {'Varianza':<10}")
print("-" * 50)

for i in range(len(muestras)):
    datos = muestras[i]
    media = np.mean(datos)
    desvio = np.std(datos)
    varianza = np.var(datos)
    
    print(f"{nombres[i]:<10} | {media:<10.4f} | {desvio:<10.4f} | {varianza:<10.4f}")

# Comparación con valores teóricos
print("\n--- Valores Teóricos Esperados ---")
print(f"Media: {1/3:.4f}, Desvío: {1/3:.4f}, Varianza: {1/9:.4f}")


plt.suptitle(r'Efecto del Tamaño de la Muestra en la Distribución Exponencial ($\lambda=3$)')
plt.tight_layout()
plt.show()

