
from network_graph import VERTICES, EDGES, TERMINALS
from connectivity import is_network_up
from monte_carlo import estimate_reliability

# Network information
print("Network Reliability - Monte Carlo")
print("Number of vertices:", len(VERTICES))
print("Number of edges:", len(EDGES))
print("Terminals:", TERMINALS)

# Check the degree of each vertex
degree = {vertex: 0 for vertex in VERTICES}

for u, v in EDGES:
    degree[u] += 1
    degree[v] += 1

print("Vertex degrees:", degree)
print("All vertices have degree 3:", all(d == 3 for d in degree.values()))

# Check for duplicate edges
unique_edges = {tuple(sorted(edge)) for edge in EDGES}

print("No duplicate edges:", len(unique_edges) == len(EDGES))

# Test network connectivity
print("All edges UP:", is_network_up(EDGES))
print("All edges DOWN:", is_network_up([]))

# Parameters for reliability estimation
p_values = [
    0.1, 0.2, 0.3, 0.4, 0.5, 0.6,
    0.7, 0.8, 0.9, 0.95, 0.99
]

M_values = [1000, 10000]

# Display reliability results table
print("\nReliability Results")
print("Terminals:", TERMINALS)
print(f"{'p':<8} {'M=1000':<12} {'M=10000':<12}")
print("-" * 32)

for p in p_values:
    results = []

    for M in M_values:
        R = estimate_reliability(p, M)
        results.append(R)

    print(f"{p:<8} {results[0]:<12.4f} {results[1]:<12.4f}")
