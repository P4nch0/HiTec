import collections
import networkx as nx


class Queue:
    def __init__(self):
        self.elements = collections.deque()

    def empty(self):
        return len(self.elements) == 0

    def put(self, x):
        self.elements.append(x)

    def get(self):
        return self.elements.popleft()


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






