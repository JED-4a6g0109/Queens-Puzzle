class QueensPuzzle:

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.checkerboard = [['.' for _ in range(cols)] for _ in range(rows)]
        self.solutions = []

    def is_valid(self, row, col, occupied_columns, occupied_left_diagonals, occupied_right_diagonals):
        if col in occupied_columns or (row - col) in occupied_left_diagonals or (row + col) in occupied_right_diagonals:
            return False
        return True

    def print_solve(self):
        print(f"共{len(self.solutions)}個解答")
        for solution in self.solutions:
            for row in solution:
                print(row)
            print()

    def handle(self):
        def backtrack(row, occupied_columns, occupied_left_diagonals, occupied_right_diagonals):
            if row == self.rows:
                self.solutions.append(["".join(r) for r in self.checkerboard])
                return

            for col in range(self.cols):
                if self.is_valid(row, col, occupied_columns, occupied_left_diagonals, occupied_right_diagonals):
                    self.checkerboard[row][col] = 'Q'
                    occupied_columns.add(col)
                    occupied_left_diagonals.add(row - col)
                    occupied_right_diagonals.add(row + col)
                    backtrack(row + 1,
                              occupied_columns=occupied_columns,
                              occupied_left_diagonals=occupied_left_diagonals,
                              occupied_right_diagonals=occupied_right_diagonals)
                    self.checkerboard[row][col] = '.'
                    occupied_columns.remove(col)
                    occupied_left_diagonals.remove(row - col)
                    occupied_right_diagonals.remove(row + col)

        backtrack(0, set(), set(), set())

    def print_board(self):
        print("\n".join(str(row) for row in self.checkerboard))


queens_puzzle = QueensPuzzle(4, 4)

queens_puzzle.handle()
queens_puzzle.print_solve()
