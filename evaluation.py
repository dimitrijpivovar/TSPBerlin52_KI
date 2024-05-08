import transform_matrix


class Evaluation:
    def __init__(self, problem):
        self.distance_matrix = transform_matrix.transform_low_diag_matrix_to_block_matrix(problem)

    def get_fitness_for_individual(self, individual):
        """
        Als Teil der Evaluation benötigen wir die Fitness.
        Fitness ist die Summe der Gewichte der Pfade in einem Individuum.
        Optimale Fitness ist das gegebene Bounds (gr17 2085, gr24 1272)
        Für gr24 ist die optimale Route
        individual = np.array([15, 10, 2, 6, 5, 23, 7, 20, 4, 9, 16, 21, 17, 18, 14, 1, 19, 13, 12, 8, 22, 3, 11, 0])
        :return:
        """
        fitness = 0
        for i in range(len(individual)):
            fitness += self.distance_matrix[individual[i - 1]][individual[i]]
        """
        Ich negiere Fitness hier, damit eine größere Fitness besser bewertet werden kann.
        Fitness ist die Summe der Weights aller Pfade im Individum. Wir wollen eine niedrige Summe der Weights.
        Die beste Fitness die für gr24 erreicht werden kann ist -1272.
        """
        return -fitness

    def get_fitness_for_population(self, population):
        """
        Kleine Helperfunction, überwiegend für debug zwecke
        :param population:
        :return:
        """
        fitness = 0
        for individual in population:
            fitness += self.get_fitness_for_individual(individual)
        return fitness

    def get_fittest_individual_for_population(self,population):
        max_fitness = self.get_fitness_for_individual(population[0])
        index_of_fittest_individual = 0
        for i in range(len(population)):
            if max_fitness < self.get_fitness_for_individual(population[i]):
                max_fitness = self.get_fitness_for_individual(population[i])
                index_of_fittest_individual = i
        return population[index_of_fittest_individual]

    def get_x_fittest_individuals_for_population(self, population, x):
        fittest_individuals = []
        temp_population = population.copy()
        for i in range(x):
            fittest_individuals.append(self.get_fittest_individual_for_population(temp_population))
            del temp_population[i]
        return fittest_individuals
