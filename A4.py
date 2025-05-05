def is_safe(board, row, column, n):
    for i in range(row):
        if board[i][column] == 'Q':
            return False
    x, y = row-1, column-1
    while(x >= 0 and y >= 0):
        if board[x][y] == 'Q':
            return False
        x -= 1
        y -= 1
    i, j = row-1, column+1
    while(i >= 0 and j < n):
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1
    return True
        
def n_queen(board, row, n, sol):
    
    if row == n:
        sol.append([" ".join(r) for r in board])
        return True
    for i in range(n):
        if is_safe(board, row, i, n):
            board[row][i] = 'Q'
            if (n_queen(board, row+1, n, sol)):
                return True
            board[row][i] = "_"
    return False

def prints(sol):
    for row in sol[0]:
        print(row)

def main():
    sol = []
    n = int(input("Enter the number of queens: "))
    board = [["_" for _ in range(n)] for _ in range(n)]
    print(board)

    if n_queen(board, 0, n, sol):
        prints(sol)
    else:
        print("No solution exists.")

main()