#!/usr/bin/python3
"""
Pascals triangle
"""


def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]  # First element in every row is always 1
        if i > 0:
            # Generate the rest of the row based on the previous row
            prev_row = triangle[i - 1]
            for j in range(1, i):
                row.append(prev_row[j - 1] + prev_row[j])
            row.append(1)  # Last element in every row is always 1
        triangle.append(row)
    return triangle


def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
