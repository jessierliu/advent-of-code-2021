"""
Day 2
"""

with open('data/day2.txt', 'r') as f:
    instructions = f.read()
    instructions = [i.split(' ') for i in instructions.split('\n')]

# Part 1
depth, hpos = 0, 0

for direction, value in instructions:
    if direction == 'up':
        depth -= int(value)
    elif direction == 'down':
        depth += int(value)
    elif direction == 'forward':
        hpos += int(value)
    else:
        raise ValueError('invalid direction')

print(hpos * depth)

# Part 2
depth, hpos, aim = 0, 0, 0

for direction, value in instructions:
    if direction == 'up':
        aim -= int(value)
    elif direction == 'down':
        aim += int(value)
    elif direction == 'forward':
        hpos += int(value)
        depth += aim * int(value)
    else:
        raise ValueError('invalid direction')

print(hpos * depth)
