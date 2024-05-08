import random


def position_based(parent1, parent2):
    """
    Position Based Crossover
    Gilbert Syswerda: Schedule Optimization Using Genetic Algorithms.
    In: Lawrence Davis (Hrsg.): Handbook of Genetic Algorithms.
    Van Nostrand Reinhold, New York 1991, ISBN 0-442-00173-8, S. 332–349 (englisch).
    Bsp:
    parent1 = [1 2 3 4 5 6 7]
    parent2 = [7 6 5 4 3 2 1]
    gene_picker = [1 0 1 0 0 0 1]
    child_unfinished = [1 ? 3 ? ? ? 7]
    missing_genes = {2,4,5,6}
    missing_genes_in_order_of_parent2 = (6,5,4,2)
    child_finished = [1 6 3 5 4 2 7]
    :param parent1:
    :param parent2:
    :return:
    Ein Kind basieren auf den Pfaden der beiden Elternteile
    """
    gene_picker = []
    for _ in range(len(parent1)):
        gene_picker.append(random.randint(0, 1))
    child = []
    for i in range(len(parent1)):
        if gene_picker[i] == 1:
            child.append(parent1[i])
        else:
            child.append(None)
    missing_genes = []
    for gene in parent2:
        if gene not in child:
            missing_genes.append(gene)
    counter = 0
    for i in range(len(child)):
        if child[i] is None:
            child[i] = missing_genes[counter]
            counter = counter + 1

    return child
