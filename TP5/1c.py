import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la simulación
num_experimentos = 30
corridas_por_exp = 100
total_corridas = num_experimentos * corridas_por_exp
z = 2.57  # Valor Z para 99% de confianza indicado en el enunciado

# Variables para almacenar resultados
tiempos_totales = []            # Guardará los tiempos de las 3000 corridas
promedios_experimentos = []     # Guardará los 30 promedios
cont_critico_sup = 0
cont_critico_med = 0
cont_critico_inf = 0

# Bucle principal: 30 experimentos
for i in range(num_experimentos):
    tiempos_exp_actual = []
    
    # Bucle interno: 100 corridas por cada experimento
    for j in range(corridas_por_exp):
        # Generación de tiempos para el Acceso Superior [U(2,4) + U(3,6) + U(2,5)]
        A = np.random.uniform(2, 4)
        B = np.random.uniform(3, 6)
        C = np.random.uniform(2, 5)
        t_sup = A + B + C
        
        # Generación de tiempos para el Acceso Medio [U(3,6) + U(2,5)]
        D = np.random.uniform(3, 6)
        E = np.random.uniform(2, 5)
        t_med = D + E
        
        # Generación de tiempos para el Acceso Inferior [U(4,8) + U(3,7)]
        F = np.random.uniform(4, 8)
        G = np.random.uniform(3, 7)
        t_inf = F + G
        
        # El tiempo total del proyecto es el máximo de las tres rutas (todas ocurren en paralelo)
        t_total = max(t_sup, t_med, t_inf)
        tiempos_exp_actual.append(t_total)
        tiempos_totales.append(t_total)
        
        # 2. Evaluar qué acceso fue el crítico (cuál determinó el fin del proyecto)
        if t_total == t_sup:
            cont_critico_sup += 1
        elif t_total == t_med:
            cont_critico_med += 1
        else:
            cont_critico_inf += 1
            
    # Promedio del experimento actual
    promedios_experimentos.append(np.mean(tiempos_exp_actual))

# 1. Cálculos Estadísticos: Tiempo promedio de finalización y el IC (99%)
promedio_general = np.mean(promedios_experimentos)
# Desviación estándar muestral de las medias
desviacion_estandar = np.std(promedios_experimentos, ddof=1) 
# Error estándar y límites del Intervalo de Confianza
error_estandar = desviacion_estandar / np.sqrt(num_experimentos)
limite_inf = promedio_general - (z * error_estandar)
limite_sup = promedio_general + (z * error_estandar)

# --- IMPRESIÓN DE RESULTADOS ---
print("--- Resultados de la Simulación del Desayuno ---")
print(f"1. Tiempo Promedio de Finalización: {promedio_general:.2f} minutos")
print(f"   Intervalo de Confianza (99%): [{limite_inf:.2f} , {limite_sup:.2f}] minutos\n")

print("2. Porcentaje de Criticidad de cada acceso (sobre 3000 corridas):")
print(f"   Acceso Superior: {(cont_critico_sup / total_corridas) * 100:.2f}%")
print(f"   Acceso Medio:    {(cont_critico_med / total_corridas) * 100:.2f}%")
print(f"   Acceso Inferior: {(cont_critico_inf / total_corridas) * 100:.2f}%\n")

# 3. Gráficos de Histogramas
plt.figure(figsize=(14, 5))

# Histograma de las 3000 corridas
plt.subplot(1, 2, 1)
plt.hist(tiempos_totales, bins=30, color='skyblue', edgecolor='black')
plt.title('Distribución del Tiempo Total (3000 corridas)')
plt.xlabel('Tiempo del proyecto (minutos)')
plt.ylabel('Frecuencia')

# Histograma de los 30 promedios
plt.subplot(1, 2, 2)
plt.hist(promedios_experimentos, bins=10, color='salmon', edgecolor='black')
plt.title('Distribución de los Promedios (30 Experimentos)')
plt.xlabel('Tiempo Promedio (minutos)')
plt.ylabel('Frecuencia')

plt.tight_layout()
plt.show()