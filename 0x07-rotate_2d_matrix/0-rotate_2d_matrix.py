#!/usr/bin/env python3
"""rotate 2d matrix module"""


def rotate_2d_matrix(matrix):
    """rotate 2d matrix func"""
    matrix_copy = [row[:] for row in matrix]
    ln = len(matrix)
    x = ln - 1
    for i in range(ln):
        for j in range(ln):
            matrix[i][j] = matrix_copy[x - j][i]
