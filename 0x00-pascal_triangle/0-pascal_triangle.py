#!/usr/bin/python3
"""Pascal Trinagle Module"""


def pascal_triangle(n):
    """pascal triangle calculation

    Args
        n(int) : integer
    """
    pt_list = []
    if n <= 0:
        return pt_list
    col_list = []
    for row in range(n):
        if row <= 1:
            for col in range(row + 1):
                col_list.append(1)
            pt_list.append(col_list)
            col_list = []
        else:
            for col in range(row + 1):
                if col == 0 or col == row:
                    col_list.append(1)
                else:
                    col_list.append(pt_list[row - 1][col - 1] +
                                    pt_list[row - 1][col])
            pt_list.append(col_list)
            col_list = []
    return pt_list
