import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
from scipy.stats import geom
from scipy.stats import poisson

# Parámetros de la distribución
n_binom = 100
p_binom = 0.35

p_geom = 0.08

Lamb = 30

# Tamaños de las muestras
sizes = [10**2, 10**3, 10**4, 10**5]

for size in sizes:
    # Generar la muestra
    r_binom = binom.rvs(n_binom, p_binom, size=size)
    r_geom = geom.rvs(p_geom,size = size)
    r_poisson = poisson.rvs(Lamb,size = size)

    #print(r_binom ,"\n", r_geom ,"\n", r_poisson)

    # Diagrama de cajas para r_binom
    plt.subplot(2, 3, 1)
    plt.boxplot(r_binom)
    plt.title(f'Diagrama de cajas para n_binom={size}')
    plt.xlabel('Distribución binomial')
    plt.ylabel('Value')

    # Diagrama de cajas para r_geom
    plt.subplot(2, 3, 2)
    plt.boxplot(r_geom)
    plt.title(f'Diagrama de cajas para r_geom, size={size}')
    plt.xlabel('Distribución geométrica')
    plt.ylabel('Value')

    # Diagrama de cajas para r_poisson
    plt.subplot(2, 3, 3)
    plt.boxplot(r_poisson)
    plt.title(f'Diagrama de cajas para r_poisson, size={size}')
    plt.xlabel('Distribución de Poisson')
    plt.ylabel('Value')

    # Histograma para r_binom
    plt.subplot(2, 3, 4)
    plt.hist(r_binom, bins=np.arange(min(r_binom), max(r_binom) + 1), edgecolor='black')
    plt.title(f'Histograma para n_binom={size}')
    plt.xlabel('Value')
    plt.ylabel('Frequency')

    # Histograma para r_geom
    plt.subplot(2, 3, 5)
    plt.hist(r_geom, bins=np.arange(min(r_geom), max(r_geom) + 1), edgecolor='black')
    plt.title(f'Histograma para r_geom, size={size}')
    plt.xlabel('Value')
    plt.ylabel('Frequency')

    # Histograma para r_poisson
    plt.subplot(2, 3, 6)
    plt.hist(r_poisson, bins=np.arange(min(r_poisson), max(r_poisson) + 1), edgecolor='black')
    plt.title(f'Histograma para r_poisson, size={size}')
    plt.xlabel('Value')
    plt.ylabel('Frequency')

    plt.tight_layout()
    plt.show()

   
    print("--------------------------------------------------")
    print(f"Resultados para r_binom={size}")
    print("--------------------------------------------------")
    # Mediana and moda for r_binom
    median = np.median(r_binom)
    mode = np.argmax(np.bincount(r_binom))
    print(f'Mediana: {median}')
    print(f'Moda: {mode}')

    # Media empírica y teórica for r_binom
    empirical_mean = np.mean(r_binom)
    theoretical_mean = n_binom * p_binom
    print(f'Media empírica: {empirical_mean}')
    print(f'Media teórica: {theoretical_mean}')

    # Varianza empírica y teórica for r_binom
    empirical_variance = np.var(r_binom)
    theoretical_variance = n_binom * p_binom * (1 - p_binom)
    print(f'Varianza empírica: {empirical_variance}')
    print(f'Varianza teórica: {theoretical_variance}')

    print("--------------------------------------------------")
    print(f"Resultados para r_geom, size={size}")
    print("--------------------------------------------------")
    # Mediana and moda for r_geom
    median = np.median(r_geom)
    mode = np.argmax(np.bincount(r_geom))
    print(f'Mediana: {median}')
    print(f'Moda: {mode}')

    # Media empírica y teórica for r_geom
    empirical_mean = np.mean(r_geom)
    theoretical_mean = 1 / p_geom
    print(f'Media empírica: {empirical_mean}')
    print(f'Media teórica: {theoretical_mean}')

    # Varianza empírica y teórica for r_geom
    empirical_variance = np.var(r_geom)
    theoretical_variance = (1 - p_geom) / (p_geom ** 2)
    print(f'Varianza empírica: {empirical_variance}')
    print(f'Varianza teórica: {theoretical_variance}')

    print("--------------------------------------------------")
    print(f"Resultados para r_poisson, size={size}")
    print("--------------------------------------------------")
    # Mediana and moda for r_poisson
    median = np.median(r_poisson)
    mode = np.argmax(np.bincount(r_poisson))
    print(f'Mediana: {median}')
    print(f'Moda: {mode}')

    # Media empírica y teórica for r_poisson
    empirical_mean = np.mean(r_poisson)
    theoretical_mean = Lamb
    print(f'Media empírica: {empirical_mean}')
    print(f'Media teórica: {theoretical_mean}')

    # Varianza empírica y teórica for r_poisson
    empirical_variance = np.var(r_poisson)
    theoretical_variance = Lamb
    print(f'Varianza empírica: {empirical_variance}')
    print(f'Varianza teórica: {theoretical_variance}')