import tsplib95 as tsplib
import draw_graph
import get_weights


def load_problem(path):
    return tsplib.load(path)


if __name__ == '__main__':
    problem_gr24 = load_problem("TSPLIB95Data/gr24.tsp") #bounds 1272
    problem_gr17 = load_problem("TSPLIB95Data/gr17.tsp") #bounds 2085
    problem_gr24_opt = load_problem("TSPLIB95Data/gr24.opt.tour")

    graph_of_gr24 = problem_gr24.get_graph()
    graph_of_gr17 = problem_gr17.get_graph()
    #draw_graph.draw(problem_gr24)
    #draw_graph.draw(problem_gr17)

    #canonical tour = tour von 1->2->3....->1
    print(problem_gr24.trace_canonical_tour())
    #eigene implementation von canonical tour
    weight_of_a_path = get_weights.get_weight_of_canonical_path(problem_gr24)
    print(weight_of_a_path)
