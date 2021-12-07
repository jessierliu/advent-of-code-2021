"""
Day 3
"""

import copy

with open('data/day3.txt', 'r') as f:
    bitlines = f.read()
    bitlines = [list(b) for b in bitlines.split('\n')]

# Part 1
num_bits = len(bitlines[0])
gamma_rate, epsilon_rate = '', ''
num_majority = len(bitlines) / 2

for i in range(num_bits):

    pos_bits = [b[i] for b in bitlines]

    if pos_bits.count('1') > num_majority:
        gamma_rate += '1'
        epsilon_rate += '0'
    else:
        gamma_rate += '0'
        epsilon_rate += '1'

print(int(gamma_rate, 2) * int(epsilon_rate, 2))

# Part 2
oxy_rating = copy.copy(bitlines)
for cur_bit in range(num_bits):

    pos_bits = [b[cur_bit] for b in oxy_rating]
    num_majority = len(oxy_rating) / 2

    if pos_bits.count('1') >= num_majority:
        oxy_rating = [c for c in oxy_rating if c[cur_bit] == '1']
    else:
        oxy_rating = [c for c in oxy_rating if c[cur_bit] == '0']

    if len(oxy_rating) == 1:
        break

oxy_rating = ''.join(oxy_rating[0])

co2_rating = copy.copy(bitlines)
for cur_bit in range(num_bits):

    pos_bits = [b[cur_bit] for b in co2_rating]
    num_majority = len(co2_rating) / 2

    if pos_bits.count('0') <= num_majority:
        co2_rating = [c for c in co2_rating if c[cur_bit] == '0']
    else:
        co2_rating = [c for c in co2_rating if c[cur_bit] == '1']

    if len(co2_rating) == 1:
        break

co2_rating = ''.join(co2_rating[0])

print(int(co2_rating, 2) * int(oxy_rating, 2))
