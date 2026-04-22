# Input graph
graph = {}

n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input("Enter node: ").strip()
    neighbours = input(f"Enter neighbours of {node} separated by space: ").split()
    graph[node] = neighbours

# Ensure all neighbour nodes exist in graph
for node in list(graph):
    for neighbour in graph[node]:
        if neighbour not in graph:
            graph[neighbour] = []

start = input("Enter starting node: ").strip()

visited = set()

def dfs(node):
    if node not in visited:
        visited.add(node)
        print(node, end=" ")
        
        for neighbour in graph.get(node, []):
            dfs(neighbour)

# Run DFS
dfs(start)

# OPTIONAL: cover disconnected graph
for node in graph:
    if node not in visited:
        dfs(node)