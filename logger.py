def print_fittest_individual(evaluation, population):
    fittest_individual_of_generation, _ = evaluation.get_fittest_individual_for_population(population)
    print('Best individual: ', fittest_individual_of_generation)
    print('Weight: ', -evaluation.get_fitness_for_individual(fittest_individual_of_generation))


def print_generation_fitness(generation, fitness):
    print('Generation: ', generation, ' has a fitness of: ', fitness)
