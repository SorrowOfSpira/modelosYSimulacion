import numpy as np

# ==========================================================
# PUNTO 5: Intervalo de Confianza con Rigurosidad del 99%
# ==========================================================

# 0. Configuración (Media=5, Desvío=3, N=1000)
np.random.seed(42)
n = 1000
media_teorica = 5
desvio_teorico = 3

# 1. Generar la muestra
muestra = np.random.normal(loc=media_teorica, scale=desvio_teorico, size=n)

def calcular_intervalo_99(datos):
    # Cálculos muestrales
    x_barra = np.mean(datos)
    sigma = np.std(datos)
    n_size = len(datos)
    
    # 2. Aplicamos el Coeficiente Z exacto para 99% (de la tabla)
    z = 2.576
    
    # 3. Cálculo del Error Estándar (la desviación de la media)
    error_estandar = sigma / np.sqrt(n_size)
    
    # 4. Cálculo de los extremos contemplando la fórmula solicitada
    # X̄ ± Z * (σ / √n)
    margen_error = z * error_estandar
    inferior = x_barra - margen_error
    superior = x_barra + margen_error
    
    return inferior, superior, x_barra, sigma, z

# Ejecución
inf, sup, prom, ds, z_val = calcular_intervalo_99(muestra)

# 5. Presentación de resultados
print(f"{'--- ESTADÍSTICOS ---':^40}")
print(f"Media Muestral (X̄): {prom:.4f}")
print(f"Desvío Muestral (s): {ds:.4f}")
print(f"Valor Z (99% Confianza): {z_val}")
print(f"{'--- INTERVALO FINAL ---':^40}")
print(f"IC 99% = [{inf:.4f} , {sup:.4f}]")
print("-" * 40)

# Verificación
if inf <= media_teorica <= sup:
    print(f"RESULTADO: La media real ({media_teorica}) está DENTRO del intervalo.")
else:
    print(f"RESULTADO: La media real está FUERA del intervalo.")