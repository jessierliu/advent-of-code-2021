"""
Day 1
"""

with open('data/day1.txt', 'r') as f:
    depths = f.read()
    depths = [int(d) for d in depths.split('\n')]

# Part 1
changes = [1 if depths[i + 1] - depths[i] > 0 else 0 for i in
           range(len(depths) - 1)]
print(changes.count(1))

# Part 2
sums = [sum(depths[i:i + 3]) for i in range(len(depths) - 2)]
changes = [1 if sums[i + 1] - sums[i] > 0 else 0 for i in range(len(sums) - 1)]
print(changes.count(1))
