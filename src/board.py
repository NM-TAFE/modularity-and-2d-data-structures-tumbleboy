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
        while True:
            player = players[0] if self.grid.count(" ") % 2 == 1 else players[1]
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
        if move.isdigit() and 0 <= int(move) <= self.count:
            return True
        else:
            return False

