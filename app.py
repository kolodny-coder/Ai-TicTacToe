import time

from contracts import contract

import player
from utiils import *


class TicTacToe:

    def __init__(self, board=None):
        self.current_winner = None
        if board is None:
            self.board = self.initiate_board()
        else:
            self.board = board

    @contract
    def initiate_board(self) -> 'list[10]':
        return ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    def print_the_board(self):
        print('  |   |  ')
        print(self.board[1] + ' | ' + self.board[2] + ' | ' + self.board[3])
        print('  |   |  ')
        print('--+---+--  ')
        print('  |   |  ')
        print(self.board[4] + ' | ' + self.board[5] + ' | ' + self.board[6])
        print('  |   |  ')
        print('--+---+--  ')
        print('  |   |  ')
        print(self.board[7] + ' | ' + self.board[8] + ' | ' + self.board[9])
        print('  |   |  ')

    @contract
    def make_a_move(self, square: 'int,> 0,< 10', letter: 'str') -> 'bool':
        if self.board[square] == '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9':
            self.board[square] = letter
            # chcek for win
            if self.check_for_a_win():
                self.current_winner = letter

            return True
        return False

    @contract
    def check_for_a_win(self) -> 'bool':
        if (self.board[1] == self.board[5] == self.board[9]) or (
                self.board[3] == self.board[5] == self.board[7]) or (
                self.board[1] == self.board[2] == self.board[3]) or (
                self.board[1] == self.board[2] == self.board[3]) or (
                self.board[4] == self.board[5] == self.board[6]) or (
                self.board[7] == self.board[8] == self.board[9]) or (
                self.board[1] == self.board[4] == self.board[7]) or (
                self.board[2] == self.board[5] == self.board[8]) or (
                self.board[3] == self.board[6] == self.board[9]):
            return True
        else:
            return False

    @contract
    def check_if_there_are_any_empty_squares(self) -> 'bool':
        return any(str(i) in self.board for i in range(1, 10))

    @contract
    def calculate_the_number_of_empty_squares_on_the_board(self) -> 'int,>= 0, < 10 ':
        counter = 0
        for i in self.board:
            if i in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                counter += 1
        return counter

    @contract
    def return_the_available_moves_on_the_current_board_as_a_list_of_integers(self) -> 'list[N], N >= 0':
        available_moves_list = [int(i) for i in self.board if i in ['1', '2', '3', '4', '5', '6', '7', '8', '9']]
        return available_moves_list


@input_validator
def game_participants():
    while True:
        game_participates = int(input(
            'please choose (1-5)\n 1. human vs smart bot\n 2. human vs human\n 3. human vs random bot\n 4. smart bot vs random bot\n 5. smart bot vs smart bot '))

        if game_participates == 1:
            print('human vs smart bot\n')
            return 1
        elif game_participates == 2:
            print('human vs human\n')
            return 2
        elif game_participates == 3:
            print('human vs random bot\n')
            return 3
        elif game_participates == 4:
            print('smart bot vs random bot\n')
            return 4
        elif game_participates == 5:
            print('smart bot vs random bot\n')
            return 5
        elif game_participates == 6:
            print('the loop exited\n')
            return 6
        else:
            print('\n\nYou chose invalid option please choose a number between 1 - 5 try again \n\n')


def play(print_game=True, board=None):
    print('Welcome to Tic Tac Toe')
    game_on = True
    while game_on == True:
        choose_game_mode = game_participants()
        if choose_game_mode == 1:
            x_player = player.SmartComputerPlayer('X')
            o_player = player.HumanPlayer('O')
            game = TicTacToe(board)

        elif choose_game_mode == 2:
            x_player = player.HumanPlayer('X')
            o_player = player.HumanPlayer('O')
            game = TicTacToe()

        elif choose_game_mode == 3:

            x_player = player.RandomComputerPlayer('X')
            o_player = player.HumanPlayer('O')
            game = TicTacToe()

        elif choose_game_mode == 4:
            x_player = player.SmartComputerPlayer('X')
            o_player = player.RandomComputerPlayer('O')
            game = TicTacToe(board)

        elif choose_game_mode == 5:
            x_player = player.SmartComputerPlayer('X')
            o_player = player.SmartComputerPlayer('O')
            game = TicTacToe()

        # for testing purpose exit point
        elif choose_game_mode == 6:
            return 'Bye'


        else:
            x_player = None
            o_player = None
            game = TicTacToe()

        if print_game:
            game.print_the_board()

        letter = 'X'
        while game.calculate_the_number_of_empty_squares_on_the_board():
            if letter == 'O':
                square = o_player.get_move(game)
            else:
                square = x_player.get_move(game)
            if game.make_a_move(square, letter):
                if print_game:
                    print(letter + f' makes a move to {square}')
                    game.print_the_board()
                    print('')
                if game.current_winner:
                    if print_game:
                        print(letter + ' wins!')
                        return letter
                    # return letter # ends the loop and exists tha game
                letter = 'O' if letter == 'X' else 'X'  # switches player
            time.sleep(0)

        if print_game:
            print('It\'s a Tie!')
            return 'Tie'


if __name__ == '__main__':
    play()
