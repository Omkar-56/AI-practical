def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True

def solve_n_queens(board, row, n, solution):
    if row == n:
        solution.append(["".join(r) for r in board])
        return True  # found one solution

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 'Q'
            if solve_n_queens(board, row + 1, n, solution):
                return True  # stop after first solution
            board[row][col] = '.'  # backtrack
    return False

def print_solution(solution):
    print("\nOne valid solution:")
    for row in solution[0]:
        print(row)

def main():
    n = int(input("Enter the value of N (size of the chessboard): "))
    board = [['.' for _ in range(n)] for _ in range(n)]
    print(board)
    solution = []

    if solve_n_queens(board, 0, n, solution):
        print_solution(solution)
    else:
        print("No solution exists.")

if __name__ == "__main__":
    main()