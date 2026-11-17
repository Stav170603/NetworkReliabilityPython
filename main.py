

from network_graph import VERTICES, EDGES, TERMINALS
from connectivity import is_network_up
from monte_carlo import estimate_reliability


# ==========================================
# Part A-B: Network Information and Validation
# ==========================================

print("Network Reliability - Crude Monte Carlo")
print("Number of vertices:", len(VERTICES))
print("Number of edges:", len(EDGES))
print("Terminals:", TERMINALS)

# Calculate the degree of each vertex
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


# ==========================================
# Part C-D: Reliability Estimation Table
# ==========================================

# Simulation parameters
p_values = [
    0.1, 0.2, 0.3, 0.4, 0.5, 0.6,
    0.7, 0.8, 0.9, 0.95, 0.99
]

M_values = [1000, 10000]

# Display reliability results
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


# ==========================================
# Part E: Five Runs and Relative Error
# ==========================================

# Parameters for Part E
p = 0.9
N = 1000
num_runs = 5

print("\nPart E - Five Independent Runs")
print(f"p = {p}, N = {N}")

# Perform five independent estimations
five_results = []

for run in range(num_runs):
    R = estimate_reliability(p, N)
    five_results.append(R)
    print(f"Run {run + 1}: {R:.4f}")

# Calculate the mean estimated reliability
S = sum(five_results) / len(five_results)

# Calculate relative error using the lecture formula:
# re(S_hat) = sqrt((1 - S) / (S * N))
# S is estimated using the mean of the five runs

if S > 0:
    relative_error = ((1 - S) / (S * N)) ** 0.5
else:
    relative_error = None

# Display final results
print("\nPart E - Results")
print(f"Estimated reliability (S): {S:.4f}")

if relative_error is not None:
    print(f"Relative error: {relative_error:.6f}")
    print(f"Relative error (%): {relative_error * 100:.4f}%")
else:
    print("Relative error cannot be calculated when S = 0.")
