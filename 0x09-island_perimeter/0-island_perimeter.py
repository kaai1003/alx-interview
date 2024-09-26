#!/usr/bin/python3
"""island perimeter module"""


def island_perimeter(grid):
    """island perimeter func"""
    perimeter = 0
    h_len = len(grid)
    w_len = len(grid[0])
    for i in range(h_len):
        for j in range(w_len):
            if grid[i][j] == 1:
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                if i == (h_len - 1) or grid[i + 1][j] == 0:
                    perimeter += 1
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                if j == (w_len - 1) or grid[i][j + 1] == 0:
                    perimeter += 1
    return perimeter
