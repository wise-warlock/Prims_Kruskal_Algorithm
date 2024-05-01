import networkx as nx
import matplotlib.pyplot as plt

def create_graph(result, graph):
    G_mst = nx.Graph()
    for u, v, weight in result:
        G_mst.add_edge(u, v, weight=weight)

    G_original = nx.Graph()
    for u in range(len(graph)):
        for v in range(u + 1, len(graph)):
            if graph[u][v] > 0:
                G_original.add_edge(u, v, weight=graph[u][v])

    return G_original, G_mst

def draw_graph(G_original, G_mst):
    pos_original = nx.spring_layout(G_original)
    nx.draw_networkx(G_original, pos_original, with_labels=True, node_color='lightblue', edge_color='gray')
    labels_original = nx.get_edge_attributes(G_original, 'weight')
    nx.draw_networkx_edge_labels(G_original, pos_original, edge_labels=labels_original)

    plt.title("Original Graph")
    plt.figure()

    pos_mst = nx.spring_layout(G_mst)
    nx.draw_networkx(G_mst, pos_mst, with_labels=True, node_color='lightblue', edge_color='red')
    labels_mst = nx.get_edge_attributes(G_mst, 'weight')
    nx.draw_networkx_edge_labels(G_mst, pos_mst, edge_labels=labels_mst)

    plt.title("MST")
    plt.show()