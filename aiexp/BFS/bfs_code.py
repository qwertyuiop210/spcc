from collections import deque

graph = {}

n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input("Enter node: ").strip()
    neighbours = input(f"Enter neighbours of {node} separated by space: ").split()
    graph[node] = neighbours

# Ensure all nodes exist
for node in list(graph):
    for neighbour in graph[node]:
        if neighbour not in graph:
            graph[neighbour] = []

start = input("Enter starting node: ").strip()


def bfs(graph, start, visited):
    queue = deque()

    visited.add(start)
    queue.append(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbour in graph.get(node, []):
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


# ✅ Global visited
visited = set()

# Run BFS from start node
bfs(graph, start, visited)

# Handle disconnected graph
for node in graph:
    if node not in visited:
        bfs(graph, node, visited)