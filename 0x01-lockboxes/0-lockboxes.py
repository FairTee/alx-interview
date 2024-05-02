#!/usr/bin/python3
"""Module for lockboxes."""


from typing import List


def canUnlockAll(boxes: List[List[int]]) -> bool:
    """
    Determine if all the boxes can be opened.

    Args:
        boxes (List[List[int]]): List of lists where each inner list
                                  represents a box and contains keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes:
        return False

    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    queue = [0]

    while queue:
        box = queue.pop(0)
        for key in boxes[box]:
            if key < n and not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)
