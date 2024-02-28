import board


class Game:
    def __init__(self):
        self.board = board.Board(5, 5)
        self.players = ["X", "O"]

    def play(self):
        while True:
            self.board.print_board()
            self.board.make_move(self.players)


game = Game()
game.play()
