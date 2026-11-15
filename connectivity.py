
from network_graph import VERTICES, TERMINALS

def is_network_up(active_edges):
    parent = {vertex: vertex for vertex in VERTICES}

    def find(vertex):
        if parent[vertex] != vertex:
            parent[vertex] = find(parent[vertex])
        return parent[vertex]

    def union(a, b):
        root_a = find(a)
        root_b = find(b)

        if root_a != root_b:
            parent[root_b] = root_a

    for u, v in active_edges:
        union(u, v)
    root = find(TERMINALS[0])

    return all(find(terminal) == root for terminal in TERMINALS)