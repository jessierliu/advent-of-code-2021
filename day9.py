"""
Day 9
"""

import copy
import numpy as np

with open('data/day9.txt', 'r') as f:
    heatmap = f.read().split('\n')

heatmap = np.stack(([np.array(list(line)).astype(int) for line in heatmap]),
                   axis=0)
row, col = heatmap.shape
low_points = []


def is_lowpoint(coords, return_adjacent=False):
    all_tests, successful_coords = [], []
    r, c = coords

    if r == 0:
        row_tests = [r + 1]
    elif r == row - 1:
        row_tests = [r - 1]
    else:
        row_tests = [r + 1, r - 1]

    if c == 0:
        col_tests = [c + 1]
    elif c == col - 1:
        col_tests = [c - 1]
    else:
        col_tests = [c + 1, c - 1]

    for i in row_tests:
        if heatmap[i, c] > heatmap[r, c]:
            all_tests.append(True)
            successful_coords.append([i, c])
        else:
            all_tests.append(False)

    for j in col_tests:
        if heatmap[r, j] > heatmap[r, c]:
            all_tests.append(True)
            successful_coords.append([r, j])
        else:
            all_tests.append(False)

    if return_adjacent:
        return all(all_tests), successful_coords
    else:
        return all(all_tests)


all_basins = []
for cur_r in range(row):
    for cur_c in range(col):

        if is_lowpoint([cur_r, cur_c]):
            low_points.append(heatmap[cur_r, cur_c])

            # If this is a low point, find the basin.
            _, next_coords = is_lowpoint([cur_r, cur_c], return_adjacent=True)
            cur_basin = [[cur_r, cur_c]]

            keep_looking = True
            while keep_looking:

                old_coords = copy.copy(next_coords)
                next_coords = []
                all_checks = []

                for combo in old_coords:
                    _, new_coords = is_lowpoint(combo, return_adjacent=True)

                    all_checks.append(len(new_coords))

                    if len(new_coords) != 0:
                        next_coords.extend(new_coords)
                        cur_basin.append(combo)
                    elif heatmap[combo[0], combo[1]] != 9:
                        cur_basin.append(combo)

                if sum(all_checks) == 0:
                    keep_looking = False

            cur_basin = np.unique([f'{a},{b}' for a, b in cur_basin])
            all_basins.append(cur_basin)

# Part 1
print((np.array(low_points) + 1).sum())

# Part 2
sorted_basins = sorted([len(b) for b in all_basins])
print(sorted_basins[-1] * sorted_basins[-2] * sorted_basins[-3])
