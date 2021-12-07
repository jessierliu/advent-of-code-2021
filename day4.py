"""
Day 4
"""

import ast
import copy

with open('data/day4.txt', 'r') as f:
    bingo = f.read()

bingo = bingo.split('\n\n')
call_nums = ast.literal_eval('[' + bingo[0] + ']')

boards = []
for raw_board in bingo[1:]:
    board = raw_board.strip(' ').split('\n')
    board = [ast.literal_eval(b.strip(' ').replace('  ', ' ').replace(
        ' ', ',')) for b in board]
    boards.append([list(b) for b in board])


def check_winning(data=None):
    nwin = len(data)

    # Make cols
    cols = [[row[c] for row in data] for c in range(len(data[0]))]

    # Count rows
    row_count = [row.count(True) for row in data]

    # Count cols
    col_count = [col.count(True) for col in cols]

    if col_count.count(nwin) >= 1 or row_count.count(nwin) >= 1:
        return True
    else:
        return False


# Part 1
play_boards = copy.copy(boards)
winning_board = None

for cur_num in call_nums:

    for board in play_boards:
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == cur_num:
                    board[r][c] = True

    for board in play_boards:
        if check_winning(data=board):
            winning_board = board
            break

    if winning_board is not None:
        break

flat_win = list(sum([tuple(b) for b in winning_board], ()))
flat_win = sum(f for f in flat_win if f != True)
print(cur_num * flat_win)

# Part 1
play_boards = copy.copy(boards)
winning_boards = [None for _ in boards]
winning_order = [None for _ in boards]

for cur_num in call_nums:

    for board in play_boards:
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == cur_num:
                    board[r][c] = True

    for cur_board, board in enumerate(play_boards):
        if check_winning(data=board):
            winning_boards[cur_board] = True
            winning_order[cur_board] = winning_boards.count(True)

    if all(winning_boards):
        break

max_index = winning_order.index(max(winning_order))
flat_win = list(sum([tuple(b) for b in play_boards[max_index]], ()))
flat_win = sum(f for f in flat_win if f != True)
print(cur_num * flat_win)
