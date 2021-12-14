"""
Day 12
"""

import copy

import numpy as np

with open('data/day12.txt', 'r') as f:
    lines = f.read().split('\n')

tunnels = {}
for line in lines:
    key, val = line.split('-')

    if key in tunnels.keys():
        tunnels[key].append(val)
    else:
        tunnels[key] = [val]

    if val in tunnels.keys():
        tunnels[val].append(key)
    else:
        tunnels[val] = [key]


def get_small_count(loop, allow_twice=False):
    caves = np.unique(loop)
    lower_caves = [c for c in caves if c.islower() and c not in ['start',
                                                                 'end']]
    if len(lower_caves) == 0:
        return True

    lower_counts = [loop.count(c) for c in lower_caves]

    if len(lower_caves) == 0:
        return True

    if allow_twice:
        twice = lower_counts.count(2)
        more_than = len(np.where(np.array(lower_counts) > 2)[0])

        if twice <= 1 and more_than == 0:
            return True
        else:
            return False

    else:
        more_than = len(np.where(np.array(lower_counts) > 1)[0])
        if more_than == 0:
            return True
        else:
            return False


for rule in [False, True]:
    paths = [['start']]
    num_incomplete = sum([False if p[-1] == 'end' else True for p in paths])

    while num_incomplete != 0:

        old_paths = copy.deepcopy(paths)

        for cur_path in old_paths:
            if cur_path[-1] == 'end':
                continue

            if cur_path.count('start') > 1:
                paths.remove(cur_path)
                continue

            num_new_paths = len(tunnels[cur_path[-1]])

            starter_path = copy.copy(cur_path)
            potential_paths = [starter_path + [p] for p in
                               tunnels[cur_path[-1]]]
            valid_paths = [p for p in potential_paths if
                           get_small_count(p, allow_twice=rule)]
            paths.remove(cur_path)
            paths.extend(valid_paths)

        num_incomplete = sum(
            [False if p[-1] == 'end' else True for p in paths])

    print(len(paths))
