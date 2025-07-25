from generator import generate_board
from solver import solve, is_board_correct
from utils import print_board, get_user_input

if __name__ == "__main__":
    puzzle = generate_board()
    print("🧩 Generated Sudoku Puzzle:")
    print_board(puzzle)

    user_board = get_user_input(puzzle)

    print("\n✅ Your Entered Sudoku Solution:")
    print_board(user_board)

    print("\n🔍 Checking your solution...")
    if is_board_correct(user_board):
        print("🎉 Correct! Well done.")
    else:
        print("❌ Incorrect solution.")
        choice = input("Do you want to see the correct solution? (y/n): ").lower()
        if choice == 'y':
            solution = [row[:] for row in puzzle]
            if solve(solution):
                print("\n✔ Correct Solution:")
                print_board(solution)
            else:
                print("❗ No solution found.")
