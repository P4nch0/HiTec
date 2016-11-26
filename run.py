import random
import collections
import networkx as nx
import Student as std
import Team as tm

teams = []
colors = ['Orange', 'Red', 'Yellow', 'Green', 'Purple']
total = 0
G = nx.Graph()


def fill_teams():
    global expected, num_teams
    expected = 0
    num_teams = 0
    while expected <= 0:
        expected = int(input("Number of expected students (>1): "))

    while num_teams <= 0 or num_teams > 9:
        num_teams = int(input("Number of teams per color (1-9): "))
    n = 0
    for c in range(0, 5):
        for i in range(0, num_teams):
            t = tm.Team(expected, num_teams)
            t.set_color(colors[c])
            t.set_num(i+1)
            # fill graph
            G.add_node(n, name=colors[c]+' '+str(i+1), color=colors[c], number=(i+1), members=[], score=t.score())
            n += 1
            teams.append(t)

    # create edges once the nodes are created
    n = 0
    for c in range(0, 5):
        for i in range(0, num_teams):
            G.add_edge(n, num_teams)
            if n < 5*num_teams-1:
                G.add_edge(n, n+1)
            n += 1

    # print_graph()


class Queue:
    def __init__(self):
        self.elements = collections.deque()

    def empty(self):
        return len(self.elements) == 0

    def put(self, x):
        self.elements.append(x)

    def get(self):
        return self.elements.popleft()


def breadth_first_search(start, s):
    # print out what we find
    frontier = Queue()
    frontier.put(start)
    visited = {}
    visited[start] = True
    ins = False
    while not frontier.empty():
        current = frontier.get()
        # print("Visiting %r" % current)
        # print(G.node[current])
        sc = G.node[current]['score']
        # print(str(sc))
        # print(s.nat(), s.nat() == 'MEX')
        sc -= 1

        if len(G.node[current]['members']) < G.node[current]['score'] and not ins:
            G.node[current]['members'].append(s)
            ins = True
            for next in G.neighbors(current):
                if next not in visited:
                    frontier.put(next)
                    visited[next] = True

        else:
            # G.node[current]['members'].append(s)
            for next in G.neighbors(current):
                if next not in visited:
                    frontier.put(next)
                    visited[next] = True


def print_graph():
    for i in range(0, num_teams*5):
        print(G.node[i]['name'] + ': ' + str(len(G.node[i]['members'])) + ' members - ' + str(G.node[i]['score']))
    # print('-------------------')


def test_bf():
    nats = ['MEX', 'MEX', 'MEX', 'MEX', 'MEX', 'MEX', 'MEX', 'USA', 'DEU', 'NLD', 'FRA', 'KOR', 'AUS', 'BEL', 'ESP']
    gen = ['Male', 'Female']

    for i in range(0, expected):
        s = std.Student('A0120'+str(i), 'Std'+str(i), 'Lst'+str(i),
                        gen[random.randint(0, 1)], nats[random.randint(0, 14)])
        breadth_first_search(random.randint(0, num_teams*5-1), s)
    print_graph()


def menu():
    fill_teams()
    # op = 1

    # while op != 0:
    # print('1. Print teams')
    # print('2. New student')
    print('1. Test Breadth First')
    print('2. ')
    # print('0. End')
    op = int(input())

    # if op == 1:
    #     print_teams()
    # elif op == 2:
    #     new_student()
    if op == 1:
        test_bf()

menu()

# fill_teams()
# def breadth_first_search(start):
#     # print out what we find
#     frontier = Queue()
#     frontier.put(start)
#     visited = {}
#     visited[start] = True
#     print(G.edges())
#
#     while not frontier.empty():
#         current = frontier.get()
#         print("Visiting %r" % current)
#         for next in G.neighbors(current):
#             if next not in visited:
#                 frontier.put(next)
#                 visited[next] = True
#
# breadth_first_search(0)

