def find(parent, i): #Find root of i
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y): #Union by rank
    xroot = find(parent, x)
    yroot = find(parent, y)
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def kruskal_mst(graph):
    size = len(graph)  # number of vertices
    edges = []  # list of edges
    vertex_data = [None] * size  # list of vertex data

    for u in range(size):  
        for v in range(u + 1, size):
            if graph[u][v] != 0:
                edges.append((graph[u][v], u, v))  # for each 2 vertices, add edge to list

    edges = sorted(edges, key=lambda item: item[0])  # sort edges by weight

    parent, rank = [], []  # parent and rank lists
    for node in range(size):  # initialize parent and rank lists
        parent.append(node)
        rank.append(0)

    result = []
    mst_weight = 0

    for weight, u, v in edges:
        x = find(parent, u)
        y = find(parent, v)
        if x != y:
            result.append((u, v, weight))
            union(parent, rank, x, y)
            mst_weight += weight

    return result, mst_weight

def output(result, mst_weight, graph):
    print("Kruskal's Algorithm MST")
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

