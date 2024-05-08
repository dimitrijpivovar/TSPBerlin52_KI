import sys


def get_weight_from_nodeX_to_nodeY(problem, nodeX, nodeY):
    return problem.get_weight(nodeX, nodeY)


def get_shortest_path_to_next_node(problem, nodeX):
    lowest_weight = sys.maxsize
    next_node = None
    for nodeY in problem.get_nodes():
        if nodeY != nodeX:
            if lowest_weight > get_weight_from_nodeX_to_nodeY(problem, nodeX, nodeY):
                lowest_weight = get_weight_from_nodeX_to_nodeY(problem, nodeX, nodeY)
                next_node = nodeY
    return lowest_weight, next_node


def get_weight_of_canonical_path(problem):
    sum_of_weights = 0
    nodeX = list(problem.get_nodes())[0]
    for i in range(0, len(list(problem.get_nodes()))):
        if i + 1 < len(list(problem.get_nodes())):
            nodeY = list(problem.get_nodes())[i + 1]
            sum_of_weights += get_weight_from_nodeX_to_nodeY(problem, nodeX, nodeY)
            nodeX = nodeY
    sum_of_weights += get_weight_from_nodeX_to_nodeY(problem, nodeX, list(problem.get_nodes())[0])
    return sum_of_weights
