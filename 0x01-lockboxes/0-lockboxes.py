#!/usr/bin/python3
"""lock boxes Module"""


def canUnlockAll(boxes):
    """check if all boxes can be unlocked"""
    n_boxes = len(boxes)
    unlocked_boxes = dfs(boxes, 0)
    if len(unlocked_boxes) == n_boxes:
        return True
    return False


def dfs(boxes, start, visited=None):
    """Depth-First Search Algorithm"""
    if visited is None:
        visited = set()
    visited.add(start)
    for key in boxes[start]:
        if key not in visited and key < len(boxes):
            dfs(boxes, key, visited)
    return visited
