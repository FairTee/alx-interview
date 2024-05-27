#!/usr/bin/python3
import sys


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at board[row][col].
    This function is called when "col" queens
    are already placed in columns from 0 to col -1.
    """
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, col, results):
    """
    Solve the N-Queens problem using backtracking.
    """
    if col >= len(board):
        results.append(board_to_result(board))
        return

    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            solve_nqueens_util(board, col + 1, results)
            board[i][col] = 0  # backtrack


def board_to_result(board):
    """
    Convert the board to the required output format.
    """
    result = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                result.append([i, j])
    return result


def solve_nqueens(n):
    """
    Solve the N-Queens problem and print the solutions.
    """
    board = [[0 for _ in range(n)] for _ in range(n)]
    results = []
    solve_nqueens_util(board, 0, results)
    results.sort()  # Sort the results
    for result in results:
        print(result)


def main():
    """
    Main function to handle input and output.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(n)


if __name__ == "__main__":
    main()
