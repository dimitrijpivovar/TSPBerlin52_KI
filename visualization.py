import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import transform_matrix


def generate_and_save(problem):
    draw_graph(problem)
    create_table(problem)


def draw_graph(problem):
    G = nx.Graph()
    edge_labels = {}
    for edge in list(problem.get_edges()):
        if edge[0] != edge[1]:
            weight = problem.get_weight(*edge)
            G.add_edge(edge[0], edge[1], weight=weight)
            edge_labels[(edge[0], edge[1])] = weight

    options = {
        "font_size": 1,
        "node_size": 10,
        "node_color": "red",
        "edgecolors": "black",
        "linewidths": 0.1,
        "width": 0.2,
    }
    nx.draw_networkx(G, **options)

    nx.draw_networkx_edge_labels(G, pos=nx.spring_layout(G), edge_labels=edge_labels, font_size=1)

    ax = plt.gca()
    ax.margins(0.05)
    plt.axis("on")
    plt.savefig(problem.name, dpi=600)
    plt.show()


def create_table(problem):
    distance_matrix = transform_matrix.transform_low_diag_matrix_to_block_matrix(problem)
    dataframe = pd.DataFrame(distance_matrix[0:])
    fig, ax = plt.subplots()
    ax.axis('off')
    table = ax.table(cellText=dataframe.values, loc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(4)
    table.scale(1, 1)

    plt.savefig('table.png', dpi=600)
