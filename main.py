import tsplib95 as tsplib
import draw_graph

def load_problem(path):
    return tsplib.load(path)

if __name__ == '__main__':
    problem_burma = load_problem("TSPLIB95Data/burma14.tsp")
    problem_berlin = load_problem("TSPLIB95Data/berlin52.tsp")
    graph_of_burma = problem_burma.get_graph()
    graph_of_berlin = problem_berlin.get_graph()
    draw_graph.draw(problem_burma)
    draw_graph.draw(problem_berlin)


