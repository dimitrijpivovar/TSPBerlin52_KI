import random

import numpy as np


def mutate(individual, mutation_probability):
    """
    Swapmutation
    Mutiert ein Individuum anhand der Mutationswahrscheinlichkeit (Teil der Praktikumsaufgabe)
    Wir wählen 2 zufällige Indizes die wir miteinander tauschen.
    :param individual:
    Individuum, welches mutiert werden soll
    :param mutation_probability:
    Mutationswahrscheinlichkeit
    :return:
    Ein neues Individuum mit mutierten Genen
    """
    threshold = random.random()
    if threshold < mutation_probability:
        first_index = np.random.randint(0, len(individual))
        second_index = np.random.randint(0, len(individual))
        individual[first_index], individual[second_index] = individual[second_index], individual[first_index]
        return individual


        


