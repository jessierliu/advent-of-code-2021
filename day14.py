"""
Day 14
"""

import copy

import numpy as np

with open('data/day14.txt', 'r') as f:
    template, lines = f.read().split('\n\n')

rules = {line.split(' -> ')[0]: line.split(' -> ')[1] for line in
         lines.split('\n')}
template = list(template)

for cur_step in range(40):

    counter = 0
    new_template = copy.copy(template)

    for i in range(len(new_template) - 1):
        pair = f'{new_template[i]}{new_template[i + 1]}'

        if pair in rules.keys():
            template.insert(i + 1 + counter, rules[pair])
            counter += 1

    if cur_step + 1 in [10, 40]:
        elements, counts = np.unique(template, return_counts=True)
        print(max(counts) - min(counts))
