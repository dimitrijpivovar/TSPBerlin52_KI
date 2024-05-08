import os

import imageio.v2 as imageio
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import transform_matrix
from os import path


def create_table(problem):
    path_of_file = './' + problem.name + '-table.png'
    if not path.exists(path_of_file):
        distance_matrix = transform_matrix.transform_low_diag_matrix_to_block_matrix(problem)
        col_and_index = list(problem.get_nodes())
        dataframe = pd.DataFrame(distance_matrix[0:], index=col_and_index, columns=col_and_index)
        fig, ax = plt.subplots()
        ax.axis('off')
        table = ax.table(cellText=dataframe.values, colLabels=dataframe.columns, rowLabels=dataframe.index,
                         loc='center')
        table.auto_set_font_size(False)
        table.set_fontsize(4)
        table.scale(1, 1)
        plt.savefig(problem.name + '-table', dpi=600)


def generate_graph(problem):
    G = nx.Graph()
    edge_labels = {}
    for edge in list(problem.get_edges()):
        if edge[0] != edge[1]:
            weight = problem.get_weight(*edge)
            G.add_edge(edge[0], edge[1], weight=weight)
            edge_labels[(edge[0], edge[1])] = weight
    return G, edge_labels


class Visualization:
    def __init__(self, problem):
        self.graph = generate_graph(problem)
        self.pos = nx.spring_layout(self.graph[0])

    def generate_and_save(self, problem):
        self.draw_graph(problem)
        create_table(problem)

    def draw_graph(self, problem):
        path_of_file = './' + problem.name + '-graph.png'
        if not path.exists(path_of_file):
            G, edge_labels = self.graph
            options = {
                "font_size": 1,
                "node_size": 10,
                "node_color": "red",
                "edgecolors": "black",
                "linewidths": 0.1,
                "width": 0.05,
            }
            nx.draw_networkx(G, self.pos, **options)

            nx.draw_networkx_edge_labels(G, pos=self.pos, edge_labels=edge_labels, font_size=1)

            ax = plt.gca()
            ax.margins(0.05)
            plt.axis("on")
            plt.savefig(problem.name + '-graph', dpi=600)

    def create_path_traversal_video(self, path_to_traverse, filename):
        G, edge_labels = self.graph
        plt.clf()
        nx.draw(G, self.pos, with_labels=True)
        plt.savefig("frame0.png")

        traversed_edges = set()
        for i in range(1, len(path_to_traverse)):
            plt.clf()
            traversed_edges.add(frozenset((path_to_traverse[i - 1], path_to_traverse[i])))

            colors = ['red' if frozenset(e) in traversed_edges else 'black' for e in G.edges()]
            width = [1 if frozenset(e) in traversed_edges else 0.05 for e in G.edges()]

            nx.draw(G, self.pos, with_labels=True,linewidths=0.1, edge_color=colors, width=width)
            plt.text(1, 1, f'Step: {i}', horizontalalignment='right', verticalalignment='top', transform=plt.gca().transAxes)
            plt.text(1, 0.95, f'Weight of Path: {i}', horizontalalignment='right', verticalalignment='top', transform=plt.gca().transAxes)
            plt.savefig(f"frame{i}.png")

        filenames = [f"frame{i}.png" for i in range(len(path_to_traverse))]

        with imageio.get_writer(filename + '.mp4', mode='I', fps=2) as writer:
            for filename in filenames:
                image = imageio.imread(filename)
                writer.append_data(image)

        for filename in filenames:
            os.remove(filename)
