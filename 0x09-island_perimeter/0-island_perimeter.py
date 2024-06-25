#!/usr/bin/python3
"""
This module contains the function island_perimeter
which calculates the perimeter of an island in a grid.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island in the grid.

    Args:
        grid (list of list of int): A list of lists where 0 represents water
                                    and 1 represents land.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    def is_water_or_boundary(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return True  # Out of bounds is considered water
        return grid[r][c] == 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                if is_water_or_boundary(r - 1, c):  # Up
                    perimeter += 1
                if is_water_or_boundary(r + 1, c):  # Down
                    perimeter += 1
                if is_water_or_boundary(r, c - 1):  # Left
                    perimeter += 1
                if is_water_or_boundary(r, c + 1):  # Right
                    perimeter += 1

    return perimeter
