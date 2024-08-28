#!/usr/bin/python3
"""N Queens Module"""
import sys

if len(sys.argv) != 2:
    print('Usage: nqueens N')
    exit(1)
try:
    n = int(sys.argv[1])
except ValueError:
    print('N must be a number')
    exit(1)
if n < 4:
    print('N must be at least 4')
    exit(1)

board = [[0] * n for i in range(n)]
column = set()
negDiag = set()
posDiag = set()


def print_solution(board):
    """print solution"""
    solution = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                solution.append([i, j])
    print(solution)


def check_place(r, c):
    if c in column or (r - c) in negDiag or (r + c) in posDiag:
        return False
    return True


def Nqueens_solution(row):
    """solve N Queens problem func"""
    if row == n:
        print_solution(board)
        return
    for col in range(n):
        if check_place(row, col):
            column.add(col)
            negDiag.add(row - col)
            posDiag.add(row + col)
            board[row][col] = 1

            Nqueens_solution(row + 1)

            column.remove(col)
            negDiag.remove(row - col)
            posDiag.remove(row + col)
            board[row][col] = 0


Nqueens_solution(0)
