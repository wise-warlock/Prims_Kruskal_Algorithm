import networkx as nx
import matplotlib.pyplot as plt

def create_graph(mst_edges, graph):
    # Create a NetworkX graph for the original graph
    G_original = nx.Graph()
    for u in range(len(graph)):
        for v in range(u + 1, len(graph)):
            if graph[u][v] != 0:
                G_original.add_edge(u, v, weight=graph[u][v])

    # Create a NetworkX graph for the MST
    G_mst = nx.Graph()
    for edge in mst_edges:
        G_mst.add_edge(edge[0], edge[1], weight=edge[2])

    return G_original, G_mst


def draw_graph(G_original, G_mst):
    # Draw the original graph
    pos = nx.spring_layout(G_original)
    nx.draw_networkx(G_original, pos, with_labels=True, node_color='lightblue', edge_color='gray')
    labels = nx.get_edge_attributes(G_original, 'weight')
    nx.draw_networkx_edge_labels(G_original, pos, edge_labels=labels)

    plt.title("Original Graph")
    plt.figure()

    # Draw the MST graph
    pos = nx.spring_layout(G_mst)
    nx.draw_networkx(G_mst, pos, with_labels=True, node_color='lightblue', edge_color='red')
    labels = nx.get_edge_attributes(G_mst, 'weight')
    nx.draw_networkx_edge_labels(G_mst, pos, edge_labels=labels)

    plt.title("MST")
    plt.figure()

def draw_delete_graph_for_runtime(G_original, G_mst):
    # Draw the original graph
    pos = nx.spring_layout(G_original)
    nx.draw_networkx(G_original, pos, with_labels=True, node_color='lightblue', edge_color='gray')
    labels = nx.get_edge_attributes(G_original, 'weight')
    nx.draw_networkx_edge_labels(G_original, pos, edge_labels=labels)

    plt.title("Original Graph")
    plt.clf()

    # Draw the MST graph
    pos = nx.spring_layout(G_mst)
    nx.draw_networkx(G_mst, pos, with_labels=True, node_color='lightblue', edge_color='red')
    labels = nx.get_edge_attributes(G_mst, 'weight')
    nx.draw_networkx_edge_labels(G_mst, pos, edge_labels=labels)

    plt.title("MST")
    plt.clf()