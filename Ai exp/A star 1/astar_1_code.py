import sys

MAX = 20

# Input
n = int(input("Enter number of nodes: "))

# Initialize graph
graph = [[0]*n for _ in range(n)]

edges = int(input("Enter number of edges: "))

print("Enter edges (u v cost):")
for _ in range(edges):
    u, v, c = map(int, input().split())
    graph[u][v] = c

# Heuristic values
print("Enter heuristic values:")
heuristic = list(map(int, input().split()))

start = int(input("Enter start node: "))
goal = int(input("Enter goal node: "))

# Initialize arrays
visited = [0]*n
parent = [-1]*n
g = [sys.maxsize]*n
f = [sys.maxsize]*n


def find_min_f():
    min_val = sys.maxsize
    index = -1

    for i in range(n):
        if not visited[i] and f[i] < min_val:
            min_val = f[i]
            index = i
    return index


def print_path(goal):
    path = []

    while goal != -1:
        path.append(goal)
        goal = parent[goal]

    print("Path:", end=" ")
    for node in reversed(path):
        print(node, end=" ")


def a_star(start, goal):
    # Initialize
    for i in range(n):
        g[i] = sys.maxsize
        f[i] = sys.maxsize
        visited[i] = 0
        parent[i] = -1

    g[start] = 0
    f[start] = heuristic[start]

    while True:
        current = find_min_f()

        if current == -1:
            print("Path not found")
            return

        if current == goal:
            print("\nGoal reached!")
            print_path(goal)
            print("\nTotal cost:", g[goal])
            return

        visited[current] = 1

        for i in range(n):
            if graph[current][i] != 0:
                temp_g = g[current] + graph[current][i]

                if temp_g < g[i]:
                    g[i] = temp_g
                    f[i] = g[i] + heuristic[i]
                    parent[i] = current


# Run A*
a_star(start, goal)