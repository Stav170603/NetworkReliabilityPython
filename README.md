
# Network Reliability - Crude Monte Carlo (CMC)

## Project Overview

This project estimates network reliability using the
Crude Monte Carlo (CMC) simulation method.

The network consists of 20 vertices and 30 edges.
All vertices are perfectly reliable, and each edge
operates independently with probability p.

The network is considered operational (UP) when
all three terminals (2, 7, 18) are connected.

## Project Files

- `network_graph.py` - Defines the vertices, edges, and terminals.
- `connectivity.py` - Checks terminal connectivity using DSS (Union-Find).
- `monte_carlo.py` - Implements the Monte Carlo simulation.
- `main.py` - Runs the simulations, displays results, and performs tests.

## Simulation Method

For each simulation:
1. Generate a random number for each edge.
2. Determine whether each edge is UP or DOWN based on probability p.
3. Check whether all three terminals are connected using Union-Find.
4. Count the simulation as successful if the network is UP.

Repeat the process M times.

Estimated reliability:

R = r / M

where:
- r is the number of successful simulations.
- M is the total number of simulations.

## Simulation Parameters

The following probabilities are evaluated:

p = 0.1, 0.2, 0.3, 0.4, 0.5, 0.6,
    0.7, 0.8, 0.9, 0.95, 0.99

Sample sizes:
- M = 1000
- M = 10000

## Part E - Relative Error

Five independent runs are performed using:
- p = 0.9
- M = 1000

The mean reliability is calculated from the five runs.

The estimated relative error is calculated using
the formula presented in the lecture:

re(S_hat) = sqrt((1 - S) / (S * N))

where S is estimated using the mean reliability
and N = 1000.

## How to Run

Python is required. No external libraries are needed.

Open a terminal in the project directory and run:

```bash
python main.py
```

## Tests

The program includes:
- Network structure validation.
- Connectivity tests using Union-Find.
- Edge case tests for p = 0 and p = 1.

## Output

The program displays:
- Network information.
- Reliability results for different p and M values.
- Five independent reliability estimates.
- Mean reliability and estimated relative error.
- Edge case and connectivity test results.
