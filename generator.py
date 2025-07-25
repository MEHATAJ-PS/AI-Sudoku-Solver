import random
from solver import solve

def generate_board():
    board = [[0 for _ in range(9)] for _ in range(9)]

    # Fill diagonal boxes
    for i in range(0, 9, 3):
        fill_box(board, i, i)

    # Solve and then remove some cells
    solve(board)
    remove_cells(board, 40)
    return board

def fill_box(board, row, col):
    nums = list(range(1, 10))
    random.shuffle(nums)
    idx = 0
    for i in range(3):
        for j in range(3):
            board[row + i][col + j] = nums[idx]
            idx += 1

def remove_cells(board, count):
    while count > 0:
        i = random.randint(0, 8)
        j = random.randint(0, 8)
        if board[i][j] != 0:
            board[i][j] = 0
            count -= 1
