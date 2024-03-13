import board


class Game:
    def __init__(self):
        self.board = board.Board(3, 3)
        if self.board.grid is None:
            print("Invalid board size. Minimum size is 3x3")
            exit(0)
        self.players = ["X", "O"]

    def play(self):
        while True:
            self.board.print_board()
            self.board.make_move(self.players)
            self.board.get_winner()


game = Game()
game.play()
