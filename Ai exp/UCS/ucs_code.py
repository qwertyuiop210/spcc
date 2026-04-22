INF = 9999

# Input
n = int(input("Enter number of nodes: "))
e = int(input("Enter number of edges: "))

# Initialize graph
graph = [[INF]*n for _ in range(n)]

print("Enter edges (from to cost):")
for _ in range(e):
    u, v, c = map(int, input().split())
    graph[u][v] = c

start = int(input("Enter start node: "))
goal = int(input("Enter goal node: "))

visited = [False]*n
parent = [-1]*n
cost = [INF]*n

cost[start] = 0
nodes_visited = 0

while True:
    min_cost = INF
    u = -1

    # Find node with minimum cost
    for i in range(n):
        if not visited[i] and cost[i] < min_cost:
            min_cost = cost[i]
            u = i

    if u == -1:
        break

    visited[u] = True
    nodes_visited += 1

    if u == goal:
        break

    # Update neighbors
    for v in range(n):
        if not visited[v] and graph[u][v] != INF:
            if cost[u] + graph[u][v] < cost[v]:
                cost[v] = cost[u] + graph[u][v]
                parent[v] = u

# Check if reachable
if not visited[goal]:
    print("Goal not reachable")
else:
    # Print path (reverse)
    path = []
    cur = goal
    while cur != -1:
        path.append(cur)
        cur = parent[cur]

    print("Path:", " ".join(map(str, path)))
    print("Total cost:", cost[goal])
    print("Nodes visited:", nodes_visited)