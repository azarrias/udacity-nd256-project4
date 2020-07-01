from math import sqrt
from collections import deque

class Node:
    def __init__(self, _id):
        self.id = _id
        self.parent = None
        self.g_value = 0
        self.h_value = 0

    # sort using g + h costs
    def __lt__(self, other):
        return self.g_value + self.h_value < other.g_value + other.h_value

    def __eq__(self, other):
        return self.id == other.id

# implement A* seaarch algorithm
def shortest_path(M, start, goal):
    print("shortest path called")
    # use min heap for the priority queue
    start_node = Node(start)
    start_node.g_value = 0
    start_node.h_value = euclidean_distance(M, start, goal)
    open_set = {}
    closed_set = {}
    open_set[start] = start_node

    while len(open_set) > 0:
        current_node = sorted(open_set.values())[0]
        if current_node.id == goal:
            return calculate_path(current_node, start)
        open_set.pop(current_node.id)
        closed_set[current_node.id] = current_node
        # add neighbours of the current node
        for neighbour in M.roads[current_node.id]:
            if neighbour in closed_set:
                continue
            if neighbour in open_set:
                neighbour_node = open_set[neighbour]
                new_g_val = current_node.g_value + euclidean_distance(M, current_node.id, neighbour)
                if new_g_val < neighbour_node.g_value:
                    neighbour_node.parent = current_node
                    neighbour_node.g_value = new_g_val
            else:
                neighbour_node = Node(neighbour)
                neighbour_node.parent = current_node
                neighbour_node.h_value = euclidean_distance(M, neighbour, goal)
                neighbour_node.g_value = current_node.g_value + euclidean_distance(M, current_node.id, neighbour)
                open_set[neighbour] = neighbour_node

# use euclidean distance to the goal node to determine the h value
def euclidean_distance(M, node1, node2):
    x1, y1 = M._graph.node[node1]['pos']
    x2, y2 = M._graph.node[node2]['pos']
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# use stack to retrieve elements in reverse order
def calculate_path(current_node, start_node):
    path = deque()
    while current_node.id != start_node:
        path.appendleft(current_node.id)
        current_node = current_node.parent
    path.appendleft(current_node.id)
    return list(path)