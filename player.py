
class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None

        while not valid_square:
            square = input(self.letter + '\'s turn.' + 'Input move(0-9)  ')
            try:
                val = int(square)
                if val not in game.return_the_available_moves_on_the_current_board():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Please try again ...')

        return val


