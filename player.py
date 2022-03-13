import math
import random

from contracts import contract



class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    @contract
    def get_move(self, game) -> 'int,> 0, < 10':
        valid_square = False
        val = None

        while not valid_square:
            square = input(self.letter + '\'s turn.' + 'Input move(0-9)  ')
            try:
                val = int(square)
                if val not in game.return_the_available_moves_on_the_current_board_as_a_list_of_integers():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Please try again ...')
            except Exception as e:
                print(e)
                break

        return val


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    @contract
    def get_move(self, game) -> 'int,> 0,< 10':
        return random.choice(game.return_the_available_moves_on_the_current_board_as_a_list_of_integers())


class SmartComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.return_the_available_moves_on_the_current_board_as_a_list_of_integers()) == 9:
            square = random.choice(game.return_the_available_moves_on_the_current_board_as_a_list_of_integers())
        else:
            square = self.minmax(game, self.letter)['position']
        return square

    def minmax(self, state, player):
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'

        # first we want to check if the previous move is a winner
        if state.current_winner == other_player:
            return {'position': None, 'score': 1 * (
                    state.calculate_the_number_of_empty_squares_on_the_board() + 1) if other_player == max_player else -1 * (
                    state.calculate_the_number_of_empty_squares_on_the_board() + 1)}
        elif not state.check_if_there_are_any_empty_squares():
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}  # each score should be maximized
        else:
            best = {'position': None, 'score': math.inf}  # each score should be minimized

        for possible_move in state.return_the_available_moves_on_the_current_board_as_a_list_of_integers():
            state.make_a_move(possible_move, player)
            sim_score = self.minmax(state, other_player)  # simulation a game after making a move

            # undo move
            state.board[possible_move] = str(possible_move)
            state.current_winner = None
            sim_score['position'] = possible_move # this represents the move optimal to next move

            if player == max_player:  # X is max player
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score

        return best
