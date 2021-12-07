"""
Day 5
"""
import numpy as np

with open('data/day5.txt', 'r') as f:
    lines = f.read().split('\n')

starts, stops = [], []
for line in lines:
    start, stop = line.split(' -> ')
    starts.append(np.array(start.split(',')).astype(int))
    stops.append(np.array(stop.split(',')).astype(int))

starts = np.array(starts)
stops = np.array(stops)
n = max(starts.max(), stops.max())


def make_map(data=None, part=None):
    for (x1, y1), (x2, y2) in zip(starts, stops):

        if x1 == x2:
            j, k = min(y1, y2), max(y1, y2)
            for i in range(j, k + 1):
                data[i, x1] += 1

        elif y1 == y2:
            j, k = min(x1, x2), max(x1, x2)
            for i in range(j, k + 1):
                data[y1, i] += 1

        else:
            if part == 1:
                continue
            else:
                xs = np.linspace(x1, x2, abs(x1 - x2) + 1, dtype=int)
                ys = np.linspace(y1, y2, abs(y1 - y2) + 1, dtype=int)

                for x, y in zip(xs, ys):
                    data[y, x] += 1

    return data


# Part 1
sand = np.zeros((n + 1, n + 1))
sand = make_map(data=sand, part=1)
print(len(np.where(sand.flatten() >= 2)[0]))

# Part 2
sand = np.zeros((n + 1, n + 1))
sand = make_map(data=sand, part=2)
print(len(np.where(sand.flatten() >= 2)[0]))
