import transform_matrix


def get_fitness_for_individual(individual, problem):
    """
    Als Teil der Evaluation benötigen wir die Fitness.
    Fitness ist die Summe der Gewichte der Pfade in einem Individuum.
    Optimale Fitness ist das gegebene Bounds (gr17 2085, gr24 1272)
    Für gr24 ist die optimale Route
    individual = np.array([15, 10, 2, 6, 5, 23, 7, 20, 4, 9, 16, 21, 17, 18, 14, 1, 19, 13, 12, 8, 22, 3, 11, 0])
    :return:
    """
    distance_matrix = transform_matrix.transform_low_diag_matrix_to_block_matrix(problem)
    fitness = 0
    for i in range(len(individual)):
        fitness += distance_matrix[individual[i - 1]][individual[i]]
    """
    Ich negiere Fitness hier, damit eine größere Fitness besser bewertet werden kann.
    Fitness ist die Summe der Weights aller Pfade im Individum. Wir wollen eine niedrige Summe der Weights.
    Die beste Fitness die für gr24 erreicht werden kann ist -1272.
    """
    return -fitness


def get_fitness_for_generation(population, problem):
    """
    Kleine Helperfunction, überwiegend für debug zwecke
    :param population:
    :param problem:
    :return:
    """
    fitness = 0
    for individual in population:
        fitness += get_fitness_for_individual(individual, problem)
    return fitness
