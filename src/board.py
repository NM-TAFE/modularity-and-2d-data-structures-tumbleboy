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

        if height > 10 or width > 10:
            raise Exception("Invalid size, board max size is 10x10")

        # create grid
        grid = [[" "for _ in range(width)] for _ in range(height)]
        return grid

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
        for col in range(self.width):
            # if there are any empty spaces in the first row, continue to next col
            if self.grid[0][col] == " ":
                continue

            # create a set by looping through each row, looking at the current col index
            if len(set(row[col] for row in self.grid)) == 1:
                return f"Player {self.grid[0][col]} won"

    def has_horizontal_winner(self) -> str:
        for row in range(self.height):
            # if there are any empty spaces left, continue to next row
            if self.grid[row][0] == " ":
                continue

            # use set to store each character in row
            # if set 1 it only contains 1 type of data, all nothing or one of the player pieces
            if len(set(self.grid[row])) == 1:
                return f"Player {self.grid[row][0]} won"

    def has_diagonal_winner(self) -> str:
        # checks if there is a player piece in top left corner
        if self.grid[0][0] != " ":
            if len(set(self.grid[i][i] for i in range(self.width))) == 1:
                return f"Player {self.grid[0][0]} has won"

        # checks if there is a player piece in bottom left corner
        # use negative indexing to count from right side instead of left
        if self.grid[-1][0] != " ":
            # count from bottom row upwards
            if len(set(self.grid[self.height - i - 1][i] for i in range(self.width))) == 1:
                return f"Player {self.grid[-1][0]} has won!"
