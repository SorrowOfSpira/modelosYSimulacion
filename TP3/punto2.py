import numpy as np
import matplotlib.pyplot as plt

# Configuración de la semilla para repetibilidad
np.random.seed(42)
n = 1000

# 1. Generación de datos
uniforme = np.random.uniform(low=0, high=1, size=n)
normal = np.random.normal(loc=0, scale=1, size=n)
poisson = np.random.poisson(lam=6, size=n)
exponencial = np.random.exponential(scale=3/4, size=n)

# 2. Creación de gráficos (Subplots para ver todos juntos)
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Histograma Uniforme
axs[0, 0].hist(uniforme, bins=20, color='lightblue', edgecolor='black')
axs[0, 0].set_title('Distribución Uniforme (0, 1)')

# Histograma Normal
axs[0, 1].hist(normal, bins=20, color='lightgreen', edgecolor='black')
axs[0, 1].set_title('Distribución Normal (0, 1)')

# Histograma Poisson
axs[1, 0].hist(poisson, bins=15, color='salmon', edgecolor='black')
axs[1, 0].set_title('Distribución Poisson (λ=6)')

# Histograma Exponencial
axs[1, 1].hist(exponencial, bins=20, color='wheat', edgecolor='black')
axs[1, 1].set_title('Distribución Exponencial (Media=34)')

plt.tight_layout()
plt.show()