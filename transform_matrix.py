import numpy as np


def transform_low_diag_matrix_to_block_matrix(problem):
    graph = problem.get_graph()
    distance_matrix = np.zeros((len(graph), len(graph)))
    for i in range(len(graph)):
        for j in range(len(graph)):
            distance_matrix[i][j] = problem.get_weight(i, j)
    return distance_matrix
