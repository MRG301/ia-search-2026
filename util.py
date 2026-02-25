# util.py
# -------
# Utilidades básicas para proyectos de búsqueda (sin typing).
# Incluye: Stack, Queue, PriorityQueue y Manhattan Distance.

import heapq
from collections import deque


class Stack:
    """Pila LIFO (ideal para DFS)."""
    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def isEmpty(self):
        return len(self.data) == 0


class Queue:
    """Cola FIFO (ideal para BFS). Implementación eficiente con deque."""
    def __init__(self):
        self.data = deque()

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.popleft()

    def isEmpty(self):
        return len(self.data) == 0


class PriorityQueue:
    """
    Cola de prioridad (min-heap).
    pop() devuelve el item con menor prioridad numérica.
    """
    def __init__(self):
        self.heap = []
        self.count = 0  # desempate estable

    def push(self, item, priority):
        entry = (priority, self.count, item)
        heapq.heappush(self.heap, entry)
        self.count += 1

    def pop(self):
        (priority, count, item) = heapq.heappop(self.heap)
        return item

    def isEmpty(self):
        return len(self.heap) == 0


def manhattanDistance(xy1, xy2):
    """Distancia Manhattan: |x1-x2| + |y1-y2|."""
    return abs(xy1[0] - xy2[0]) + abs(xy1[1] - xy2[1])