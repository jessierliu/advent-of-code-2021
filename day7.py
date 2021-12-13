"""
Day 7
"""

import numpy as np

with open('data/day7.txt', 'r') as f:
    positions = f.read().split(',')
    positions = np.array(positions).astype(int)

# Part 1
left, right = min(positions), max(positions)
all_costs = {}
for pos in range(left, right + 1):
    all_costs[pos] = np.abs(positions - pos).sum()

print(all_costs[min(all_costs, key=all_costs.get)])

# Part 2
all_costs = {}
for pos in range(left, right + 1):
    all_costs[pos] = np.sum(
        [sum(range(p + 1)) for p in np.abs(positions - pos)])

print(all_costs[min(all_costs, key=all_costs.get)])
