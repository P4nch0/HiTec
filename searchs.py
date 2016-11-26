import collections
import networkx as nx
import heapq

class Queue:
    def __init__(self):
        self.elements = collections.deque()

    def empty(self):
        return len(self.elements) == 0

    def put(self, x):
        self.elements.append(x)

    def get(self):
        return self.elements.popleft()


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]

G = nx.Graph()

G.add_nodes_from(['A', 'B', 'C', 'D', 'E'])
G.add_edge('A', 'B')

G.add_edge('B', 'C')
G.add_edge('B', 'D')

G.add_edge('A', 'C')

G.add_edge('D', 'E')
G.add_edge('D', 'A')

G.add_edge('E', 'B')


def breadth_first_search(start):
    # print out what we find
    frontier = Queue()
    frontier.put(start)
    visited = {}
    visited[start] = True
    print(G.edges())

    while not frontier.empty():
        current = frontier.get()
        print("Visiting %r" % current)
        for next in G.neighbors(current):
            if next not in visited:
                frontier.put(next)
                visited[next] = True

breadth_first_search('A')


def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)


def a_star_search(start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for next in G.neighbors(current):
            new_cost = cost_so_far[current] + cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                frontier.put(next, priority)
                came_from[next] = current

    return came_from, cost_so_far

came_from, cost_so_far = a_star_search((1, 4), (7, 8))
