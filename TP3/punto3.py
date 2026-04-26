import numpy as np
import matplotlib.pyplot as plt

# 0. Configuración inicial
np.random.seed(42)

# ==========================================================
# PARTE 1: Función de Transformación (Lambda = 12)
# ==========================================================
u_base = np.random.uniform(0, 1, 1000)

def transformar_exponencial(u_datos, lam):
    return -np.log(u_datos) / lam

exponencial_transformada = transformar_exponencial(u_base, 12)

plt.figure(figsize=(8, 5))
plt.hist(exponencial_transformada, bins=30, color='mediumpurple', edgecolor='black')
# Usamos r'' para evitar el SyntaxWarning con \lambda
plt.title(r'Punto 3.a/b: Variable Exponencial por Transformada Inversa ($\lambda=12$)')
plt.xlabel('Valor generado')
plt.ylabel('Frecuencia')
plt.grid(alpha=0.3)
plt.show()

# ==========================================================
# PARTE 2: Comparación de muestras (Lambda = 3)
# ==========================================================
param_scale = 1/3

m_100 = np.random.exponential(scale=param_scale, size=100)
m_1000 = np.random.exponential(scale=param_scale, size=1000)
m_10000 = np.random.exponential(scale=param_scale, size=10000)

fig, axs = plt.subplots(1, 3, figsize=(18, 5))

# Gráfico 1: N=100
axs[0].hist(m_100, bins=20, color='lightcoral', edgecolor='black')
axs[0].set_title('Muestra N=100')

# Gráfico 2: N=1000
axs[1].hist(m_1000, bins=30, color='lightseagreen', edgecolor='black')
axs[1].set_title('Muestra N=1000')

# Gráfico 3: N=10000
axs[2].hist(m_10000, bins=50, color='cornflowerblue', edgecolor='black')
axs[2].set_title('Muestra N=10000')

# Título general con r'' también por precaución
plt.suptitle(r'Comparación de Distribuciones Exponenciales ($\lambda=3$)')
plt.tight_layout()
plt.show()