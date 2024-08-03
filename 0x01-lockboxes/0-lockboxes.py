#!/usr/bin/python3
"""lock boxes Module"""


def canUnlockAll(boxes):
    """check if all boxes can be unlocked"""
    n_boxes = len(boxes)
    unlocked_boxes = dfs(boxes, 0)
    if len(unlocked_boxes) == n_boxes:
        return True
    return False


def dfs(boxes, start):
    """Depth-First Search Algorithm without recursion"""
    visited = set()
    stack = [start]

    while stack:
        box = stack.pop()
        if box not in visited:
            visited.add(box)
            for key in boxes[box]:
                if key not in visited and key < len(boxes):
                    stack.append(key)
    return visited
