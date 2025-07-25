def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(board[i][j] if board[i][j] != 0 else ".", end=" ")
        print()

def get_user_input(puzzle):
    print("\n✍️ Enter your solution for the blank cells.")
    user_board = [row[:] for row in puzzle]

    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                while True:
                    try:
                        val = int(input(f"Row {i+1}, Col {j+1} (1-9): "))
                        if val in range(1, 10):
                            user_board[i][j] = val
                            break
                        else:
                            print("Invalid input. Enter a number 1-9.")
                    except ValueError:
                        print("Enter a valid integer.")
    return user_board
