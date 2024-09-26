#!/usr/bin/python3
"""island perimeter module"""


def island_perimeter(grid):
    """island perimeter func"""
    perimeter = 0
    h_len = len(grid)
    v_len = len(grid[0])
    for i in range(1, (h_len - 1)):
        for j in range(1, (v_len - 1)):
            if grid[i][j] == 1:
                if grid[i][j - 1] == 0:
                    perimeter += 1
                if grid[i][j + 1] == 0:
                    perimeter += 1
                if grid[i - 1][j] == 0:
                    perimeter += 1
                if grid[i + 1][j] == 0:
                    perimeter += 1
    return perimeter
