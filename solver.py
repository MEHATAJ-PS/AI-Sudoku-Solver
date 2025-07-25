def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def is_valid(board, num, pos):
    row, col = pos
    # Check row
    if num in board[row]:
        return False
    # Check col
    if num in [board[i][col] for i in range(9)]:
        return False
    # Check 3x3
    box_x = col // 3
    box_y = row // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num:
                return False
    return True

def solve(board):
    find = find_empty(board)
    if not find:
        return True
    row, col = find

    for i in range(1, 10):
        if is_valid(board, i, (row, col)):
            board[row][col] = i
            if solve(board):
                return True
            board[row][col] = 0
    return False

def is_board_correct(board):
    for i in range(9):
        row = [num for num in board[i] if num != 0]
        col = [board[j][i] for j in range(9) if board[j][i] != 0]
        if len(set(row)) != len(row) or len(set(col)) != len(col):
            return False

    for i in range(3):
        for j in range(3):
            nums = []
            for r in range(3):
                for c in range(3):
                    num = board[i*3 + r][j*3 + c]
                    if num != 0:
                        nums.append(num)
            if len(set(nums)) != len(nums):
                return False
    return True
