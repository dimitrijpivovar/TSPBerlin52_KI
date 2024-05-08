import tsplib95 as tsplib
import population


def load_problem(path):
    return tsplib.load(path)


if __name__ == '__main__':
    problem_gr24 = load_problem("TSPLIB95Data/gr24.tsp") #bounds 1272
    problem_gr17 = load_problem("TSPLIB95Data/gr17.tsp") #bounds 2085
    problem_gr24_opt = load_problem("TSPLIB95Data/gr24.opt.tour")
    #visualization.generate_and_save(problem_gr24)
    population = population.init_pop(nodes=list(problem_gr24.get_nodes()), population_size=100)




