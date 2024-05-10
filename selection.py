import random
from evaluation import Evaluation


class Selection:
    def __init__(self, evaluationProblem):
        self.evaluation = evaluationProblem

    def parent_above_average_selection(self, population):
        """
        :param:
        population: Die Population der aktuellen Generation
        :return:
        Ein zufällig gewähltes Individuum, welches einen überdurchschnittlichen Fitnesswert hat. Dieses Individuum wird zum
        Crossover verwendet um einen (hoffentlich) einen Nachfahren mit höherer Fitness zu erzeugen.
        """
        sum_of_fitness = 0
        for i in range(len(population)):
            sum_of_fitness += self.evaluation.get_fitness_for_individual(population[i])
        avg_fitness_of_population = sum_of_fitness / len(population)
        potential_parents = list(filter(lambda individual:
                                        self.evaluation.get_fitness_for_individual(
                                            individual) > avg_fitness_of_population,
                                        population))
        return potential_parents[random.randint(0, len(potential_parents) - 1)]

    def parent_tournament_selection(self, population):
        """
        :return:
        Individual mit der besten Fitness aus 30 zufällig ausgesuchten Individuals
        """
        potential_parents = []
        for i in range(30):
            potential_parents.append(population[random.randint(0, len(population) - 1)])
        return self.evaluation.get_fittest_individual_for_population(potential_parents)

    def survival_selection(self, population, percentage):
        """
        Geben einen prozentuellen Wert an population der aktuellen Generation an die nächste weiter.
        Survival of the Fittest
        :param population:
        :param percentage:
        :return:
        Überlebende Individals, die Teil der nächsten Generation werden.
        """
        absolute_value = int(len(population) * percentage)
        return self.evaluation.get_x_fittest_individuals_for_population(population=population, x=absolute_value)
