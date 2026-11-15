
import random
from network_graph import EDGES
from connectivity import is_network_up

def estimate_reliability(p, M):
    r = 0

    for simulation in range(M):
        active_edges = []

        for edge in EDGES:
            x = random.random()

            if x <= p:
                active_edges.append(edge)

        if is_network_up(active_edges):
            r += 1

    R = r / M
    return R
