"""
Day 8
"""

import numpy as np

with open('data/day8.txt', 'r') as f:
    lines = f.read().split('\n')

normal = {
    0: 'abcefg',
    1: 'cf',
    2: 'acdeg',
    3: 'acdfg',
    4: 'bcdf',
    5: 'abdfg',
    6: 'abdefg',
    7: 'acf',
    8: 'abcdefg',
    9: 'abcdfg',
}

normal_counts = {key: len(val) for key, val in normal.items()}
all_output_nums = []

for line in lines:
    digits, outputs = line.split(' | ')

    digits = digits.split(' ')

    new = {key: None for key in range(10)}

    for d in digits:
        if len(d) == normal_counts[1]:
            new[1] = d
        elif len(d) == normal_counts[4]:
            new[4] = d
        elif len(d) == normal_counts[7]:
            new[7] = d
        elif len(d) == normal_counts[8]:
            new[8] = d

    # find out which is 6, should be missing a letter in `1`
    for d in digits:
        if len(d) == normal_counts[6] and (new[1][0] not in d or new[1][1]
                                           not in d):
            new[6] = d

    # find 5, should be 1 less than `6`
    for d in digits:
        if len(d) == normal_counts[5]:
            if len(np.setdiff1d(list(new[6]), list(d))) == 1:
                new[5] = d

    # find 9, should be 1 more than `5`
    for d in digits:
        if len(d) == normal_counts[9]:
            if len(np.setdiff1d(list(d), list(new[5]))) == 1 and d not in \
                    new.values():
                new[9] = d

    # 0 is the last remaining 6 count
    for d in digits:
        if len(d) == normal_counts[0] and d not in new.values():
            new[0] = d

    # 2 and 5 should be opposite
    for d in digits:
        if len(d) == normal_counts[2]:
            if len(np.intersect1d(list(d), list(new[5]))) == 3 and d not in \
                    new.values():
                new[2] = d

    for d in digits:
        if d not in new.values():
            new[3] = d

    output_nums = []
    for o in outputs.split(' '):
        for key, val in new.items():
            if set(o) == set(val):
                output_nums.append(key)

    all_output_nums.append(output_nums)

# Part 1
print(sum([sum([i.count(j) for j in [1, 4, 7, 8]]) for i in all_output_nums]))

# Part 2
print(sum(int(''.join(map(str, i))) for i in all_output_nums))
