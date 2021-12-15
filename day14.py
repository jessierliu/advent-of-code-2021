"""
Day 14
"""

from collections import Counter

with open('data/day14.txt', 'r') as f:
    template, lines = f.read().split('\n\n')

rules = {line.split(' -> ')[0]: line.split(' -> ')[1] for line in
         lines.split('\n')}
pairs = Counter()
for i in range(len(template) - 1):
    if template[i:i + 2] not in pairs.keys():
        pairs[template[i:i + 2]] = 1
    else:
        pairs[template[i:i + 2]] += 1

for cur_step in range(40):

    for pair, count in zip(list(pairs.keys()), list(pairs.values())):

        if pair in rules.keys():
            pairs[pair] -= count
            new1 = pair[0] + rules[pair]
            new2 = rules[pair] + pair[1]

            pairs[new1] += count
            pairs[new2] += count

    if cur_step + 1 in [10, 40]:
        total = Counter()
        for key, val in pairs.items():
            total[key[1]] += val
        total[template[0]] += 1
        print(max(total.values()) - min(total.values()))
