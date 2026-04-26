# Si es la primera vez usando el lenguaje, se deben instalar los siguientes modulos por la consola de julia
# import Pkg; Pkg.add("Distributions")
# import Pkg; Pkg.add("StatsPlots")

using Distributions
using Statistics
using StatsPlots

# 1. Definir la distribución de pesos (en gramos)
distribucionNormal = Normal(150, 20)
datos = rand(distribucionNormal, 100)

# 2. Cálculos solicitados
println("Media del peso: ", mean(datos), " g")
println("Desvío estándar: ", std(datos), " g")
println("Varianza: ", var(datos))

# 3. Gráfico
histogram(datos, 
    bins=15, 
    normalize=:pdf, 
    fillcolor=:green,
    fillalpha=0.4, 
    label="Pesos reales (Muestra)",
    title="Distribución del Peso de las Manzanas",
    xlabel="Peso (gramos)",
    ylabel="Densidad")

# Agregamos la curva teórica perfecta
plot!(distribucionNormal, 
    linecolor=:blue, 
    lw=3, 
    label="Distribución Teórica")