import tsplib95 as tsplib


def load_problem(path):
    return tsplib.load(path)


if __name__ == '__main__':
    problem = load_problem("TSPLIB95Data/berlin52.tsp")
    print(problem.render())
