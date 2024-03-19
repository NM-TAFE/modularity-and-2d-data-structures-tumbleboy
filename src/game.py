import board


class Game:
    def __init__(self):
        self.board = board.Board(1, 3)
        self.players = ["X", "O"]

    def play(self):
        while True:
            self.board.print_board()
            self.make_move(self.players)
            game_over = self.board.get_winner()
            if game_over:
                print(game_over)
                exit(0)

    def make_move(self, players) -> None:
        # count the empty spaces left, used to assign a new player each turn
        empty_space_count = sum(row.count(" ") for row in self.board.grid)

        # check for a tie
        if empty_space_count == 0:
            print("Game is tie.")
            exit(0)

        while True:
            player = players[0] if empty_space_count % 2 == 1 else players[1]
            # f string
            move = input("Next move for player " + player + " (0-" + str(self.board.count) + "): ")
            if self.move_is_valid(move):
                # this allows us to get 1 number from the user and calculate the row and col index's
                # instead of asking for a row and col index separately
                row_index = (int(move)) // self.board.width
                col_index = (int(move)) % self.board.width
                # assign the grid with the current player
                self.board.grid[row_index][col_index] = player
                break
            else:
                print("Invalid move, try again.")

    def move_is_valid(self, move) -> bool:
        if (move.isdigit() and
                0 <= int(move) <= self.board.count and
                self.board.space_is_empty(move)):
            return True
        else:
            return False


game = Game()
game.play()
