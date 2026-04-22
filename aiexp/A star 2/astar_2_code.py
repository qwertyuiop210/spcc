import heapq

graph = {}
heuristic = {}

n = int(input("Enter number of nodes: "))

# Input graph edges and heuristic values
for i in range(n):
    node = input("Enter node: ")
    h = int(input(f"Enter heuristic value for {node}: "))
    heuristic[node] = h

    m = int(input(f"Enter number of neighbours for {node}: "))
    neighbours = []

    for j in range(m):
        neighbour = input("Enter neighbour node: ")
        cost = int(input(f"Enter cost to {neighbour}: "))
        neighbours.append((neighbour, cost))

    graph[node] = neighbours

start = input("Enter start node: ")
goal = input("Enter goal node: ")


def a_star(start, goal):
    pq = []
    heapq.heappush(pq, (heuristic[start], 0, start, [start]))

    visited = set()

    while pq:
        f, g, node, path = heapq.heappop(pq)

        if node == goal:
            print("Path found:", path)
            print("Total cost:", g)
            return

        if node in visited:
            continue

        visited.add(node)

        for neighbour, cost in graph[node]:
            if neighbour not in visited:
                new_g = g + cost
                new_f = new_g + heuristic[neighbour]
                heapq.heappush(pq, (new_f, new_g, neighbour, path + [neighbour]))

    print("No path found")


a_star(start, goal)