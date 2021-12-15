"""
Day 13
"""

import numpy as np
import matplotlib.pyplot as plt

with open('data/day13.txt', 'r') as f:
    coords, instructions = f.read().split('\n\n')

instructions = instructions.split('\n')
coords = np.stack(np.array(c.split(',')).astype(int) for c in coords.split(
    '\n'))
nrow, ncol = max(coords[:, 1]), max(coords[:, 0])
dots = np.zeros((nrow + 1, ncol + 1))

for cur_dot in range(coords.shape[0]):
    dots[coords[cur_dot, 1], coords[cur_dot, 0]] += 1

# folds = [int(i.split('=')[-1]) for i in instructions]

fold_dots = np.copy(dots)
for i, line in enumerate(instructions):

    direction, num = line.split('=')
    num = int(num)

    if direction[-1] == 'x':
        fold_dots = fold_dots[:, :num] + np.fliplr(fold_dots[:, num + 1:])
    else:
        fold_dots = fold_dots[:num, :] + np.flipud(fold_dots[num + 1:, :])

    if i == 0:
        print(fold_dots.astype(bool).sum())

plt.imshow(fold_dots.astype(bool))
plt.show()
