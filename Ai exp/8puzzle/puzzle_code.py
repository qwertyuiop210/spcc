import heapq

goal = [[1,2,3],
        [4,5,6],
        [7,8,0]]

# Heuristic: Misplaced tiles
def heuristic(state):
    return sum(
        1
        for i in range(3)
        for j in range(3)
        if state[i][j] != 0 and state[i][j] != goal[i][j]
    )

# Check solvability
def is_solvable(state):
    arr = [num for row in state for num in row if num != 0]
    inv = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                inv += 1
    return inv % 2 == 0

# Find blank
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Generate moves
def get_moves(state):
    x, y = find_blank(state)
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    children = []

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            children.append(new_state)

    return children

# A* Search
def a_star(start):
    pq = []
    visited = set()
    count = 0

    heapq.heappush(pq, (heuristic(start), 0, count, start, []))

    while pq:
        f, g, _, state, path = heapq.heappop(pq)

        if state == goal:
            return path + [state]

        state_tuple = tuple(map(tuple, state))

        if state_tuple in visited:
            continue

        visited.add(state_tuple)

        for child in get_moves(state):
            child_tuple = tuple(map(tuple, child))

            if child_tuple not in visited:
                count += 1
                new_g = g + 1
                new_f = new_g + heuristic(child)

                heapq.heappush(pq, (new_f, new_g, count, child, path + [state]))

    return None

# -------- MAIN --------
start = []
print("Enter initial state (use 0 for blank):")

for i in range(3):
    row = list(map(int, input().split()))
    start.append(row)

# Solvability check
if not is_solvable(start):
    print(" This puzzle is NOT solvable")
else:
    solution = a_star(start)

    if solution:
        print("\nSolution Steps:")
        for step in solution:
            for row in step:
                print(row)
            print()
        print("Total moves:", len(solution) - 1)
    else:
        print("No solution found")