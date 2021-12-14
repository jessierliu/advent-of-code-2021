"""
Day 10
"""

with open('data/day10.txt', 'r') as f:
    lines = f.read().split('\n')

corrupt_points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}
closer_points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}
closers = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

corrupt_closers, autocomplete_scores = [], []
for line in lines:

    corrupt_line = False

    opened = []
    for c in line:
        if c in closers.keys():
            opened.append(c)
        elif c == closers[opened[-1]]:
            opened.pop();
        else:
            corrupt_closers.append(corrupt_points[c])
            corrupt_line = True
            break

    if not corrupt_line and len(opened) != 0:
        to_complete = [closers[o] for o in reversed(opened)]

        cur_score = 0
        for c in to_complete:
            cur_score *= 5
            cur_score += closer_points[c]

        autocomplete_scores.append(cur_score)

# Part 1
print(sum(corrupt_closers))

# Part 2
print(sorted(autocomplete_scores)[len(autocomplete_scores) // 2])
