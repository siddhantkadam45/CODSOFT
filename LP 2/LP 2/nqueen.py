class NQueens:
    def __init__(self, n):
        self.n = n
        self.board = [-1] * n
        self.solution_count = 0

    def is_safe(self, row, col):
        for prev_row in range(row):
            if (
                self.board[prev_row] == col
                or abs(self.board[prev_row] - col) == abs(prev_row - row)
            ):
                return False
        return True

    def solve(self, row):
        if row == self.n:
            self.print_solution()
            self.solution_count += 1
            return

        for col in range(self.n):
            if self.is_safe(row, col):
                self.board[row] = col
                self.solve(row + 1)
                self.board[row] = -1

    def print_solution(self):
        print(f"Solution {self.solution_count}:")
        for row in range(self.n):
            line = ["Q" if col == self.board[row] else "." for col in range(self.n)]
            print(" ".join(line))
        print()

    def find_solutions(self):
        self.solve(0)


# Example usage for N = 8
n_queens_solver = NQueens(8)
n_queens_solver.find_solutions()
