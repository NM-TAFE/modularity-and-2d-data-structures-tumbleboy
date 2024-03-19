class Board:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.grid = self.create_2d_grid(self.height, self.width)
        self.count = (height * width) - 1 # get the total count of game squares generated

    @staticmethod
    def create_2d_grid(height, width) -> list[list[str]] | None:
        if height < 3 or width < 3:
            raise Exception("Invalid size, board must be at least 3x3")

        # Change into list comprehension, line 45
        grid = []
        for i in range(height):
            grid.append([])
            for j in range(width):
                grid[i].append(" ")
        return grid

    def print_board(self) -> None:
        last_row = self.height - 1
        last_col = self.width - 1
        row_index = 0
        for row in self.grid:
            col_index = 0
            # " | ".join([row])
            for col in row:
                # checks to see if we are at the last column, if so then don't print '|'
                if col_index == last_col:
                    print(col)
                    break
                else:
                    print(col, end=" | ")
                    col_index += 1
            if row_index == last_row:
                break
            else:
                print("---" * self.width)
                row_index += 1

    def space_is_empty(self, move) -> bool:
        row_index = (int(move)) // self.width
        col_index = (int(move)) % self.width
        if self.grid[row_index][col_index] == " ":
            return True
        else:
            return False

    def get_winner(self) -> str:
        return self.has_horizontal_winner() or self.has_vertical_winner() or self.has_diagonal_winner()

    def has_vertical_winner(self):
        if self.grid[0][0] == self.grid[1][0] == self.grid[2][0] != " ":
            self.print_board()
            return f"Player {self.grid[0][0]} has won!"
        elif self.grid[0][1] == self.grid[1][1] == self.grid[2][1] != " ":
            self.print_board()
            return f"Player {self.grid[0][1]} has"
        elif self.grid[0][2] == self.grid[1][2] == self.grid[2][2] != " ":
            self.print_board()
            return f"Player {self.grid[0][2]} has won!"

    def has_horizontal_winner(self) -> str:
        win_conditions = (0, 1, 2)
        for row in self.grid:
            if row[win_conditions[0]] == row[win_conditions[1]] == row[win_conditions[2]] != " ":
                self.print_board()
                return f"Player {row[win_conditions[0]]} has won!"

    def has_diagonal_winner(self) -> str:
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] != " ":
            self.print_board()
            return f"Player {self.grid[0][0]} has won!"

        elif self.grid[2][0] == self.grid[1][1] == self.grid[0][2] != " ":
            self.print_board()
            return f"Player {self.grid[2][0]} has won!"
