import random
from copy import deepcopy

# ---------- Helpers ----------

def is_valid_move(src, dst):
    """Check if top of src can be moved to dst."""
    if not src:
        return False
    if not dst:
        return True
    return src[-1] < dst[-1]


def generate_neighbors(state):
    """Generate all valid next states."""
    A, B, C = state
    rods = [list(A), list(B), list(C)]
    neighbors = []

    for i in range(3):
        for j in range(3):
            if i != j and is_valid_move(rods[i], rods[j]):
                new_rods = deepcopy(rods)
                disk = new_rods[i].pop()
                new_rods[j].append(disk)
                neighbors.append(tuple(tuple(r) for r in new_rods))

    return neighbors


def heuristic(state, n):
    """
    Count how many disks are correctly placed on goal rod C
    in proper order from bottom (n ... 1).
    """
    C = state[2]
    correct = 0
    expected = list(range(n, 0, -1))  # [n, n-1, ..., 1]
    for i in range(min(len(C), n)):
        if C[i] == expected[i]:
            correct += 1
        else:
            break
    return correct


def is_goal(state, n):
    return state[2] == tuple(range(n, 0, -1))


# ---------- Hill Climbing ----------

def hill_climb(start_state, n, max_sideways=50, max_steps=10000):
    current = start_state
    current_h = heuristic(current, n)
    sideways_moves = 0
    path = [current]

    for _ in range(max_steps):
        if is_goal(current, n):
            return path, True

        neighbors = generate_neighbors(current)
        # Evaluate neighbors
        scored = [(heuristic(s, n), s) for s in neighbors]
        best_h, best_state = max(scored, key=lambda x: x[0])

        if best_h > current_h:
            current = best_state
            current_h = best_h
            sideways_moves = 0
            path.append(current)

        elif best_h == current_h and sideways_moves < max_sideways:
            # Sideways move to escape plateau
            candidates = [s for h, s in scored if h == best_h]
            current = random.choice(candidates)
            sideways_moves += 1
            path.append(current)

        else:
            # Stuck in local optimum
            return path, False

    return path, False


# ---------- Pretty Print ----------

def print_state(state):
    A, B, C = state
    print(f"A: {list(A)}  B: {list(B)}  C: {list(C)}")


# ---------- Example ----------

if __name__ == "__main__":
    n = 3
    # Start: all disks on A (bottom->top: n..1)
    start = (tuple(range(n, 0, -1)), tuple(), tuple())

    path, success = hill_climb(start, n)

    print("Start State:")
    print_state(start)
    print("\nSteps:\n")

    for i, st in enumerate(path):
        print(f"Step {i}:")
        print_state(st)

    print("\nResult:", "Goal Reached ✅" if success else "Stuck in Local Optimum ❌")