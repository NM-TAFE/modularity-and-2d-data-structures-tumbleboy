import board


class Game:
    def __init__(self):
        self.board = board.Board(3, 3)
        self.players = ["X", "O"]

    def play(self):
        while True:
            self.board.print_board()
            self.board.make_move(self.players)
            self.board.get_winner()


game = Game()
game.play()
