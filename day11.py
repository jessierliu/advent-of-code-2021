"""
Day 11
"""

import numpy as np

with open('data/day11.txt', 'r') as f:
    octo = f.read().split('\n')

octo = np.stack([np.array([int(i) for i in list(o)]) for o in octo])


def get_surrounding(x, y, dims=None):
    r = [x - 1, x - 1, x - 1, x, x, x + 1, x + 1, x + 1]
    c = [y - 1, y, y + 1, y - 1, y + 1, y - 1, y, y + 1]
    w, z = [], []
    for cur_r, cur_c in zip(r, c):
        if cur_r < 0 or cur_r >= dims[0] or cur_c < 0 or cur_c >= dims[1]:
            continue
        else:
            w.append(cur_r)
            z.append(cur_c)

    return tuple([np.array(w), np.array(z)])


total_flashes = []
for cur_step in range(225):

    # step 1
    octo += 1

    did_flash = np.full(octo.shape, False)

    idx = np.where(octo > 9)
    e2f = list(did_flash[idx].flatten()).count(False)

    # some flashed
    while e2f != 0:

        for a, b in zip(*idx):
            if not did_flash[a, b]:
                did_flash[a, b] = True

                # increase surrounding
                jdx = get_surrounding(a, b, dims=octo.shape)
                octo[jdx] += 1

        idx = np.where(octo > 9)
        e2f = list(did_flash[idx].flatten()).count(False)

    # set flashed to 0
    jdx = np.where(did_flash)
    octo[jdx] = 0
    total_flashes.append(len(jdx[0]))

    if did_flash.flatten().all():
        # Part 2
        print(cur_step + 1)

# Part 1
print(sum(total_flashes[:100]))
