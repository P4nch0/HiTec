import random
import collections
import networkx as nx
import Student as std
import Team as tm
import math
import heapq

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
            G.add_node(n, name=colors[c]+' '+str(i+1), color=colors[c], number=(i+1),
                       members=[], score=math.floor(t.score()*.7), max=t.score())
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


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]


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
        if s.nat() == 'MEX':
            sc -= 1

        if len(G.node[current]['members']) < G.node[current]['max'] and not ins and sc >= 0:
            G.node[current]['members'].append(s.nat())
            G.node[current]['score'] = sc
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
            new_cost = cost_so_far[current] + G[current][next]['cost']
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                frontier.put(next, priority)
                came_from[next] = current


def print_graph():
    for i in range(0, num_teams*5):
        print(G.node[i]['name'] + ': ' + str(len(G.node[i]['members'])) + ' members - ' + str(G.node[i]['members']))
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
    # print('2. ')
    # print('0. End')
    op = int(input())

    # if op == 1:
    #     print_teams()
    # elif op == 2:
    #     new_student()
    if op == 1:
        test_bf()

menu()


# def bound_branch_assign(s):
#     costs = []
#     i = 0
#     for team in teams:
#         c = 0
#         students = team.get_list()
#         for student in students:
#             g = student.get_gender()
#             n = student.get_nat()
#             if g == s.get_gender():
#                 c += 1
#             if n == s.get_nat():
#                 c += 1
#         costs.append(c)
#         # print(costs[i])
#         i += 1
#     bound = min(costs)
#     index = costs.index(bound)
#
#     if not teams[index].is_full():
#         teams[index].add_student(s)
#     elif teams[index].is_full():
#         teams[index+1].add_student(s)
