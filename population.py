import numpy as np


def get_random_permutation(nodes):
    """
    Wir liefern eine zufällige Permutation zurück, die als Individuum einer Population zu verstehen ist.
    Eine Permutation ist eine Anordnung von Objekten aus einer Menge nodes
    :param
    nodes: Die Nodes des Problemgraphen. gr17 hat 17 Nodes, gr24 hat 24 Nodes.
    """
    return np.random.permutation(nodes)


def init_pop(nodes, population_size):
    """
    Mit dieser Population werden wir eine Evaluation machen und danach Parents auswählen
    Ablaufdiagram siehe 3. Vorlesung Seite 23.
    :param:
    nodes: Die Nodes des Problemgraphen. gr17 hat 17 Nodes, gr24 hat 24 Nodes.
    population_size: Die Größe der gewünschten Population.
    :return:
    Array der Größe population_size, Inhalt sind zufällig generierte Individuals
    """
    population = []
    for _ in range(population_size):
        individual = get_random_permutation(nodes)
        population.append(individual)
    return population
