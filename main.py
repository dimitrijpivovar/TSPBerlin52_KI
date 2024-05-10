import tsplib95 as tsplib

from evaluation import Evaluation
from selection import Selection
from visualization import Visualization
from population import init_pop
import mutation
import crossover


def load_problem(path):
    return tsplib.load(path)


if __name__ == '__main__':
    problem_gr24 = load_problem("TSPLIB95Data/gr24.tsp")  #bounds 1272
    problem_gr17 = load_problem("TSPLIB95Data/gr17.tsp")  #bounds 2085
    problem_gr24_opt = load_problem("TSPLIB95Data/gr24.opt.tour")
    evaluation = Evaluation(problem_gr24)
    selection = Selection(evaluation)
    visualization_gr24 = Visualization(problem_gr24)
    visualization_gr17 = Visualization(problem_gr17)

    visualization_gr24.generate_and_save()
    visualization_gr17.generate_and_save()
    generation_size = 200
    population_size = 100
    population = init_pop(nodes=list(problem_gr24.get_nodes()), population_size=population_size)

    print('Best individual: ', evaluation.get_fittest_individual_for_population(population))
    print('Weight: ', -evaluation.get_fitness_for_individual(evaluation.get_fittest_individual_for_population(population)))
    visualization_gr24.create_path_traversal_video(filename='traverse_first_gen',
                                              path_to_traverse=evaluation.get_fittest_individual_for_population(population))

    for i in range(generation_size):
        print('Generation: ', i, ' has a fitness of: ', evaluation.get_fitness_for_population(population))
        new_population = []
        for individual in selection.survival_selection(population=population, percentage=0.1):
            new_population.append(individual)
        for _ in range(population_size - len(new_population)):
            parent1 = selection.parent_tournament_selection(population=population)
            parent2 = selection.parent_tournament_selection(population=population)
            child = crossover.position_based(parent1=parent1, parent2=parent2)
            mutation.mutate(individual=child, mutation_probability=0.33)
            new_population.append(child)
        population = new_population
    print('Best individual: ', evaluation.get_fittest_individual_for_population(population))
    print('Weight: ', -evaluation.get_fitness_for_individual(evaluation.get_fittest_individual_for_population(population)))
    visualization_gr24.create_path_traversal_video(filename='traverse_last_gen',
                                              path_to_traverse=evaluation.get_fittest_individual_for_population(population))

