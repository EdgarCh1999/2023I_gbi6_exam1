#_________________ Función 1
import numpy
def build_population(N, p):
# Crea una lista vacía para almacenar la población
    population = []
# Repite N veces para crear N individuos
    for i in range(N):
    # Establece el primer alelo en "A"
        allele1 = "A"
        # Genera un número aleatorio y verifica si es mayor que p
        if numpy.random.rand() > p:
             # Si es mayor que p, cambia el primer alelo a "a"
            allele1 = "a"
            # Establece el segundo alelo en "A"
        allele2 = "A"
        # Genera otro número aleatorio y verifica si es mayor que p
        if numpy.random.rand() > p:
            # Si es mayor que p, cambia el segundo alelo a "a"
            allele2 = "a"
         # Agrega la tupla de alelos a la lista de población
        population.append((allele1, allele2))
     # Devuelve la lista de población
    return population

#_________________ Función 2
def compute_frequencies(population):
     # Cuenta el número de individuos con genotipo "AA" en la población
    AA = population.count(("A", "A"))
     # Cuenta el número de individuos con genotipo "Aa" en la población
    Aa = population.count(("A", "a"))
     # Cuenta el número de individuos con genotipo "aA" en la población
    aA = population.count(("a", "A"))
    # Cuenta el número de individuos con genotipo "aa" en la población
    aa = population.count(("a", "a"))
     # Devuelve un diccionario con la frecuencia de cada genotipo
    return({"AA": AA, "aa": aa, "Aa": Aa, "aA": aA})

#_________________ Función 3
import numpy as np
def reproduce_population(population):
    new_generation = []
    N = len(population)
    for i in range(N):
        dad = np.random.randint(N)
        mom = np.random.randint(N)
        chr_mom = np.random.randint(2)
        offspring = (population[mom][chr_mom], population[dad][1 - chr_mom])
        new_generation.append(offspring)
    return new_generation

#_________________ Función 4
def simulate_drift(N, p):
    my_pop = build_population(N, p)
    fixation = False
    num_generations = 0
    while fixation == False:
        genotype_counts = compute_frequencies(my_pop)
        if (genotype_counts["AA"] == N or genotype_counts["aa"] == N):
            print("An allele reached fixation at generation", num_generations)
            print("The genotype counts are")
            print(genotype_counts)
            fixation == True
            break
        my_pop = reproduce_population(my_pop)
        num_generations += 1
    return num_generations, genotype_counts
