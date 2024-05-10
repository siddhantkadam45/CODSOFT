import heapq

class PuzzleNode:
    def __init__(self, state, parent=None, move=None, depth=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = self.depth  # removed the heuristic call, it's calculated lazily

    def __lt__(self, other):
        return self.cost < other.cost

    def __eq__(self, other):
        return self.state == other.state

    def calculate_cost(self):
        # Calculate the total cost of the node (f(n) = g(n) + h(n))
        return self.depth + self.heuristic()

    def heuristic(self):
        # Manhattan distance heuristic
        total_distance = 0
        for i in range(3):
            for j in range(3):
                if self.state[i][j] != 0:
                    goal_row = (self.state[i][j] - 1) // 3
                    goal_col = (self.state[i][j] - 1) % 3
                    total_distance += abs(i - goal_row) + abs(j - goal_col)
        return total_distance

    def get_neighbors(self):
        neighbors = []
        zero_row, zero_col = self.find_zero()
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up
        for dr, dc in moves:
            new_row, new_col = zero_row + dr, zero_col + dc
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_state = [list(row) for row in self.state]
                new_state[zero_row][zero_col], new_state[new_row][new_col] = \
                    new_state[new_row][new_col], new_state[zero_row][zero_col]
                neighbors.append(PuzzleNode(new_state, parent=self, move=(dr, dc), depth=self.depth + 1))
        return neighbors

    def find_zero(self):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    return i, j

    def get_solution_path(self):
        path = []
        current = self
        while current:
            path.append((current.state, current.move))
            current = current.parent
        path.reverse()
        return path

def a_star(start_state):
    start_node = PuzzleNode(start_state)
    if start_node.heuristic() == 0:
        return start_node.get_solution_path()

    visited = set()
    priority_queue = []
    heapq.heappush(priority_queue, start_node)

    while priority_queue:
        current_node = heapq.heappop(priority_queue)
        visited.add(tuple(map(tuple, current_node.state)))

        for neighbor in current_node.get_neighbors():
            if tuple(map(tuple, neighbor.state)) not in visited:
                if neighbor.heuristic() == 0:
                    return neighbor.get_solution_path()
                heapq.heappush(priority_queue, neighbor)
    
    return None  # No solution found


# Final state
final_state = [[1, 2, 3],
               [4, 0, 5],
               [6, 7, 8]]
print("Final state:")
for row in final_state:
    print(row)


# Take input for start state from the user
print("Enter the start state of the puzzle (3x3 grid with numbers 0-8, separated by spaces):")
start_state = []
for i in range(3):
    row = list(map(int, input().split()))
    start_state.append(row)



solution = a_star(start_state)
if solution:
    print("Solution Found!")
    for i, (state, move) in enumerate(solution):
        print(f"Step {i+1}:")
        for row in state:
            print(row)
        print("Move:", move)
        print()
else:
    print("No solution found.")
