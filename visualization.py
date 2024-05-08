import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import transform_matrix
from os import path


def generate_and_save(problem):
    draw_graph(problem)
    create_table(problem)


def draw_graph(problem):
    path_of_file = './' + problem.name + '-graph.png'
    if not path.exists(path_of_file):
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
        plt.savefig(problem.name + '-graph', dpi=600)


def create_table(problem):
    path_of_file = './' + problem.name + '-table.png'
    if not path.exists(path_of_file):
        distance_matrix = transform_matrix.transform_low_diag_matrix_to_block_matrix(problem)
        col_and_index = list(problem.get_nodes())
        dataframe = pd.DataFrame(distance_matrix[0:], index=col_and_index, columns=col_and_index)
        fig, ax = plt.subplots()
        ax.axis('off')
        table = ax.table(cellText=dataframe.values,colLabels=dataframe.columns, rowLabels=dataframe.index, loc='center')
        table.auto_set_font_size(False)
        table.set_fontsize(4)
        table.scale(1, 1)
        plt.savefig(problem.name + '-table', dpi=600)
