import networkx as nx
import matplotlib.pyplot as plt


def draw(problem):
    G = nx.Graph()
    edge_labels = {}
    for edge in list(problem.get_edges()):
        if edge[0] != edge[1]:
            weight = problem.get_weight(*edge)
            G.add_edge(edge[0], edge[1], weight=weight)
            edge_labels[(edge[0], edge[1])] = weight

    pos = {}
    graph = problem.get_graph()
    for position in graph:
        pos[position] = [100 * x for x in graph.nodes[position]['coord']]

    options = {
        "font_size": 1,
        "node_size": 10,
        "node_color": "red",
        "edgecolors": "black",
        "linewidths": 0.1,
        "width": 0.2,
    }
    nx.draw_networkx(G, pos, **options)

    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=1)

    ax = plt.gca()
    ax.margins(0.05)
    plt.axis("off")
    plt.savefig(problem.name, dpi=600)
    plt.show()
