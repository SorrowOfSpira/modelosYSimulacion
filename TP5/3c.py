import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la simulación
num_experimentos = 30
corridas_por_exp = 100
total_corridas = num_experimentos * corridas_por_exp
z = 2.57  # Valor Z para 99% de confianza

# Variables para almacenar resultados
tiempos_totales = []            
promedios_experimentos = []     

# Diccionario para contar cuántas veces cada tarea formó parte del camino crítico
criticidad = {letra: 0 for letra in 'ABCDEFGHIJ'}

# Bucle principal: 30 experimentos
for i in range(num_experimentos):
    tiempos_exp_actual = []
    
    # Bucle interno: 100 corridas por cada experimento
    for j in range(corridas_por_exp):
        
        # 1. Generación de tiempos para cada tarea U(min, max) en días
        A = np.random.uniform(2, 4)
        B = np.random.uniform(3, 5)
        C = np.random.uniform(1, 2)
        D = np.random.uniform(4, 8)
        E = np.random.uniform(3, 6)
        F = np.random.uniform(2, 5)
        G = np.random.uniform(2, 4)
        H = np.random.uniform(1, 3)
        I = np.random.uniform(2, 4)
        J = np.random.uniform(2, 3)
        
        # 2. Definición de las posibles rutas lógicas de construcción
        ruta1 = A + B + C + I + J          # Terreno -> Bases -> Cloacas -> Pisos -> Pintar
        ruta2 = A + B + D + E + I + J      # ... -> Paredes -> Techo -> Pisos -> Pintar
        ruta3 = A + B + D + E + F + J      # ... -> Paredes -> Techo -> Electricidad -> Pintar
        ruta4 = A + B + D + E + G + J      # ... -> Paredes -> Techo -> Gas -> Pintar
        ruta5 = A + B + D + H + J          # ... -> Paredes -> Aberturas -> Pintar
        
        # El tiempo total es el máximo de todas las rutas posibles (CPM)
        t_total = max(ruta1, ruta2, ruta3, ruta4, ruta5)
        tiempos_exp_actual.append(t_total)
        tiempos_totales.append(t_total)
        
        # 3. Evaluar la criticidad: A, B y J son cuellos de botella (están en todas las rutas)
        criticidad['A'] += 1
        criticidad['B'] += 1
        criticidad['J'] += 1
        
        # Sumamos criticidad a las tareas de la ruta que determinó el tiempo máximo
        if t_total == ruta1:
            criticidad['C'] += 1
            criticidad['I'] += 1
        elif t_total == ruta2:
            criticidad['D'] += 1
            criticidad['E'] += 1
            criticidad['I'] += 1
        elif t_total == ruta3:
            criticidad['D'] += 1
            criticidad['E'] += 1
            criticidad['F'] += 1
        elif t_total == ruta4:
            criticidad['D'] += 1
            criticidad['E'] += 1
            criticidad['G'] += 1
        elif t_total == ruta5:
            criticidad['D'] += 1
            criticidad['H'] += 1
            
    # Promedio del experimento actual
    promedios_experimentos.append(np.mean(tiempos_exp_actual))

# Cálculos Estadísticos
promedio_general = np.mean(promedios_experimentos)
desviacion_estandar = np.std(promedios_experimentos, ddof=1) 
error_estandar = desviacion_estandar / np.sqrt(num_experimentos)
limite_inf = promedio_general - (z * error_estandar)
limite_sup = promedio_general + (z * error_estandar)

# --- IMPRESIÓN DE RESULTADOS ---
print("--- Resultados de la Simulación de la Obra ---")
print(f"1. Tiempo Promedio de Finalización: {promedio_general:.2f} días")
print(f"   Intervalo de Confianza (99%): [{limite_inf:.2f} , {limite_sup:.2f}] días\n")

print("2. Porcentaje de Criticidad de cada tarea (sobre 3000 corridas):")
for tarea, conteo in criticidad.items():
    porcentaje = (conteo / total_corridas) * 100
    print(f"   Tarea {tarea}: {porcentaje:5.2f}%")

# --- GRÁFICOS ---
plt.figure(figsize=(14, 5))

# Histograma de las 3000 corridas
plt.subplot(1, 2, 1)
plt.hist(tiempos_totales, bins=30, color='mediumpurple', edgecolor='black')
plt.title('Distribución del Tiempo Total de Obra (3000 corridas)')
plt.xlabel('Tiempo de construcción (días)')
plt.ylabel('Frecuencia')

# Histograma de los 30 promedios
plt.subplot(1, 2, 2)
plt.hist(promedios_experimentos, bins=10, color='gold', edgecolor='black')
plt.title('Distribución de los Promedios (30 Experimentos)')
plt.xlabel('Tiempo Promedio (días)')
plt.ylabel('Frecuencia')

plt.tight_layout()
plt.show()