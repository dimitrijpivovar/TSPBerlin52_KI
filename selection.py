import evaluation
import random


def parent_selection(population, problem):
    """
    :param:
    population: Die Population der aktuellen Generation
    :return:
    Ein zufällig gewähltes Individuum, welches einen überdurchschnittlichen Fitnesswert hat. Dieses Individuum wird zum
    Crossover verwendet um einen (hoffentlich) einen Nachfahren mit höherer Fitness zu erzeugen.
    """
    sum_of_fitness = 0
    for i in range(len(population)):
        sum_of_fitness += evaluation.get_fitness(population[i], problem)
    avg_fitness_of_population = sum_of_fitness / len(population)
    potential_parents = list(filter(lambda individual:
                                    evaluation.get_fitness(individual, problem) > avg_fitness_of_population,
                                    population))
    return potential_parents[random.randint(0, len(potential_parents) - 1)]
