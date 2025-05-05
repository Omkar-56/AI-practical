import heapq

# Heuristic: Manhattan distance
def manhattan(state, goal):
    distance = 0
    for num in range(1, 9):  # tiles 1–8
        idx1 = state.index(num)
        row1 = idx1 // 3
        col1 = idx1 % 3

        idx2 = goal.index(num)
        row2 = idx2 // 3
        col2 = idx2 % 3

        distance += abs(row1 - row2) + abs(col1 - col2)
    return distance

# Generate neighboring states by moving the blank (0)
def get_neighbors(state):
    neighbors = []
    idx = state.index(0)
    row = idx // 3
    col = idx % 3

    directions = {
        'up': (row - 1, col),
        'down': (row + 1, col),
        'left': (row, col - 1),
        'right': (row, col + 1)
    }

    for move, (new_row, new_col) in directions.items():
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_idx = new_row * 3 + new_col
            new_state = list(state)
            new_state[idx], new_state[new_idx] = new_state[new_idx], new_state[idx]
            neighbors.append(tuple(new_state))

    return neighbors

# A* Search Algorithm
def a_star(start, goal):
    open_set = []
    heapq.heappush(open_set, (manhattan(start, goal), 0, start, []))
    visited = set()

    while open_set:
        f, g, current, path = heapq.heappop(open_set)
        if current in visited:
            continue
        visited.add(current)

        if current == goal:
            return path + [current]

        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                h = manhattan(neighbor, goal)
                heapq.heappush(open_set, (g + 1 + h, g + 1, neighbor, path + [current]))

    return None

# Print puzzle nicely
def print_puzzle(state):
    for i in range(0, 9, 3):
        row = [' ' if x == 0 else str(x) for x in state[i:i+3]]
        print(' '.join(row))
    print()

# Input helper
def input_puzzle(prompt):
    print(f"{prompt} (use 0 for the blank tile):")
    puzzle = []
    while len(puzzle) < 9:
        try:
            row = input(f"Enter row {len(puzzle)//3 + 1} (3 numbers): ").split()
            if len(row) != 3:
                print("Enter exactly 3 numbers.")
                continue
            puzzle += list(map(int, row))
        except ValueError:
            print("Invalid input. Use integers.")
    return tuple(puzzle)

# Main program
if __name__ == "__main__":
    start = input_puzzle("Enter START state")
    goal = input_puzzle("Enter GOAL state")

    print("\nSolving with A* Search...\n")
    solution = a_star(start, goal)

    if solution:
        print(f"Solution found in {len(solution) - 1} moves:\n")
        for step in solution:
            print_puzzle(step)
    else:
        print("No solution found.")
