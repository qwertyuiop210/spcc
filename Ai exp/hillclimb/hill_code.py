import copy

# Initial state
def initial_state(n):
    return [list(range(n, 0, -1)), [], []]

# Goal check
def is_goal(state, n):
    return state[2] == list(range(n, 0, -1))

# Heuristic: number of disks in goal rod
def heuristic(state):
    return len(state[2])

# Generate valid moves
def generate_neighbors(state):
    neighbors = []

    for i in range(3):
        if not state[i]:
            continue

        for j in range(3):
            if i != j:
                if not state[j] or state[i][-1] < state[j][-1]:
                    new_state = copy.deepcopy(state)
                    disk = new_state[i].pop()
                    new_state[j].append(disk)
                    neighbors.append(new_state)

    return neighbors


# Hill Climbing with sideways moves
def hill_climbing(n):
    current = initial_state(n)
    visited = []
    step = 0

    sideways_limit = 10
    sideways_count = 0

    print("\nInitial State:", current)

    while not is_goal(current, n):
        visited.append(current)
        neighbors = generate_neighbors(current)

        best_neighbor = None
        best_h = heuristic(current)

        for neighbor in neighbors:
            if neighbor not in visited:
                h = heuristic(neighbor)

                # Better move
                if h > best_h:
                    best_h = h
                    best_neighbor = neighbor
                    sideways_count = 0

                # Sideways move
                elif h == best_h and sideways_count < sideways_limit:
                    best_neighbor = neighbor
                    sideways_count += 1

        if best_neighbor is None:
            print("\n❌ Stuck at Local Optimum")
            return

        current = best_neighbor
        step += 1
        print(f"Step {step}: {current} | h(n) = {heuristic(current)}")

    print("\n✅ Goal Reached!")


# -------- MAIN --------
n = int(input("Enter number of disks: "))
hill_climbing(n)