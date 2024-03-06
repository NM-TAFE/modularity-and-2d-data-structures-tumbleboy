class Board:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.grid = self.create_2d_grid(self.height, self.width)
        self.count = (height * width) - 1 # get the total count of game squares generated

    @staticmethod
    def create_2d_grid(height, width) -> list[list[str]]:
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

    def make_move(self, players) -> None:
        # count the empty spaces left, used to assign a new player each turn
        empty_space_count = sum(row.count(" ") for row in self.grid)

        while True:
            player = players[0] if empty_space_count % 2 == 1 else players[1]
            move = input("Next move for player " + player + " (0-" + str(self.count) + "): ")
            if self.move_is_valid(move):
                # this allows us to get 1 number from the user and calculate the row and col index's
                # instead of asking for a row and col index separately
                row_index = (int(move)) // self.width
                col_index = (int(move)) % self.width
                # assign the grid with the current player
                self.grid[row_index][col_index] = player
                break
            else:
                print("Invalid move, try again.")

    def move_is_valid(self, move) -> bool:
        if (move.isdigit() and
                0 <= int(move) <= self.count and
                self.space_is_empty(move)):
            return True
        else:
            return False

    def space_is_empty(self, move) -> bool:
        row_index = (int(move)) // self.width
        col_index = (int(move)) % self.width
        if self.grid[row_index][col_index] == " ":
            return True
        else:
            return False

    def get_winner(self):
        return self.has_horizontal_winner() or self.has_vertical_winner()

    def has_vertical_winner(self):
        if self.grid[0][0] == self.grid[1][0] == self.grid[2][0] != " ":
            self.print_board()
            print(f"Player {self.grid[0][0]} has won!")
            exit(0)
        elif self.grid[0][1] == self.grid[1][1] == self.grid[2][1] != " ":
            self.print_board()
            print(f"Player {self.grid[0][1]} has won!")
            exit(0)
        elif self.grid[0][2] == self.grid[1][2] == self.grid[2] != " ":
            self.print_board()
            print(f"Player {self.grid[0][2]} has won!")
            exit(0)

    def has_horizontal_winner(self):
        win_conditions = (0, 1, 2)
        for row in self.grid:
            if row[win_conditions[0]] == row[win_conditions[1]] == row[win_conditions[2]] != " ":
                self.print_board()
                print(f"Player {row[win_conditions[0]]} has won!")
                exit(0)

    def has_diagonal_winner(self):
        ...
