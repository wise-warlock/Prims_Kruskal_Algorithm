def prim_mst(graph):
    size = len(graph)
    in_mst = [False] * size  # Keeps track of visited vertices
    key_values = [float('inf')] * size  # Keeps track of the minimum weight of the edge
    parents = [-1] * size  # Keeps track of the parent of the vertex

    key_values[0] = 0  # Starting vertex
    mst_weight = 0  # Stores the weight of the MST
    result = []  # List to store the edges of the MST (u - starting vertex,v - end vertex, weight)
    for _ in range(size):
        u = min((v for v in range(size) if not in_mst[v]), key=lambda v: key_values[v])

        in_mst[u] = True  # Mark the vertex as visited

        if parents[u] != -1:  # Skip printing for the first vertex since it has no parent
            result.append((parents[u], u, graph[u][parents[u]]))
            mst_weight += graph[u][parents[u]]  # Add the weight of the edge to the MST
        for v in range(size):  # Update the key values and parents of the adjacent vertices of the current vertex
            if graph[u][v] < key_values[v] and not in_mst[v] and graph[u][v] != 0:
                key_values[v] = graph[u][v]
                parents[v] = u

    return result, mst_weight


def output(result, mst_weight, graph):
    print("Prim's Algorithm MST")
    for u, v, weight in result:
        print(f"{u}-{v} \t{weight}")

    print("Adjacency matrix for the original graph:")
    for row in graph:
        print(row)

    print("Adjacency lists for the original graph:")
    for i in range(len(graph)):
        adjacent_vertices = [j for j in range(len(graph)) if graph[i][j] != 0] #This is change the negative weight value
        print(f"Vertex {i}: {', '.join([str(v) for v in adjacent_vertices])}")

    print(f"Total weight of MST: {mst_weight}")


