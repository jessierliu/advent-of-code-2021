"""
Day 6
"""

import copy

with open('data/day6.txt', 'r') as f:
    fish = f.read().split(',')
    fish = [int(f) for f in fish]

print_days = [80, 256]
total_days = 256

fish_counts = {i: fish.count(i) for i in range(9)}

for cur_day in range(total_days):

    loop_fish = copy.deepcopy(fish_counts)
    fish_counts = {i: 0 for i in range(9)}

    for key, val in loop_fish.items():
        if key == 0:
            fish_counts[8] = val
            fish_counts[6] = val
        else:
            fish_counts[key - 1] += val

    if cur_day + 1 in print_days:
        print(sum(list(fish_counts.values())))
