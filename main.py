
from network_graph import VERTICES, EDGES, TERMINALS
from connectivity import is_network_up
from monte_carlo import estimate_reliability
print("Network Reliability - Monte Carlo")
print("Number of vertices:", len(VERTICES))
print("Number of edges:", len(EDGES))
print("Terminals:", TERMINALS)

# Count the number of edges connected to each vertex
degree = {vertex: 0 for vertex in VERTICES}

for u, v in EDGES:
    degree[u] += 1
    degree[v] += 1

print("Vertex degrees:", degree)
print("All vertices have degree 3:", all(d == 3 for d in degree.values()))

unique_edges = {tuple(sorted(edge)) for edge in EDGES}

print("No duplicate edges:", len(unique_edges) == len(EDGES))

# Test network connectivity
print("All edges UP:", is_network_up(EDGES))
print("All edges DOWN:", is_network_up([]))
print("Estimated reliability:", estimate_reliability(0.9, 1000))