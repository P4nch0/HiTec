import collections
import networkx as nx

class SimpleGraph:
    def __init__(self):
        self.edges = {}

    def neighbors(self, id):
        return self.edges[id]


example_graph = SimpleGraph()
example_graph.edges = {
    'A': ['B'],
    'B': ['A', 'C', 'D'],
    'C': ['A'],
    'D': ['E', 'A'],
    'E': ['B']
}


class Queue:
    def __init__(self):
        self.elements = collections.deque()

    def empty(self):
        return len(self.elements) == 0

    def put(self, x):
        self.elements.append(x)

    def get(self):
        return self.elements.popleft()


def breadth_first_search_1(graph, start):
    # print out what we find
    frontier = Queue()
    frontier.put(start)
    visited = {}
    visited[start] = True
    print(example_graph.edges)

    while not frontier.empty():
        current = frontier.get()
        print("Visiting %r" % current)
        for next in graph.neighbors(current):
            if next not in visited:
                frontier.put(next)
                visited[next] = True

# breadth_first_search_1(example_graph, 'A')

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
    print(example_graph.edges)

    while not frontier.empty():
        current = frontier.get()
        print("Visiting %r" % current)
        for next in G.neighbors(current):
            if next not in visited:
                frontier.put(next)
                visited[next] = True

breadth_first_search('A')






