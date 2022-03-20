import unittest
from io import StringIO
from unittest.mock import MagicMock, patch

import app
import player
from error_classes import LogicError


class TestPlayer(unittest.TestCase):

    @patch('builtins.input')
    def test_human_get_move_happy_path(self, mock_input: MagicMock):
        mock_input.return_value = '3'
        game = app.TicTacToe()
        game.board = ['#',
                      '1', '2', '3',
                      'X', '5', '6',
                      'X', 'O', 'O'
                      ]
        human_player = player.HumanPlayer('X')
        res = human_player.get_move(game)
        self.assertTrue(3, res)

    @patch('builtins.input')
    def test_human_get_move_sad_path(self, input_mock: MagicMock):
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            input_mock.side_effect = ['3', '4', '5']
            game = app.TicTacToe()
            game.board = ['#',
                          '1', '2', 'X',
                          'X', '5', '6',
                          'X', 'O', 'O'
                          ]
            human_player = player.HumanPlayer('X')
            res = human_player.get_move(game)
            self.assertTrue(5, res)
            self.assertEqual(fakeOutput.getvalue(),
                             'Invalid square. Please try again ...\nInvalid square. Please try again ...\n')

    def test_check_random_computer_player_get_move_returns_valid_value_happy_path_no_assert(self):
        # test with no assert only check the contract validation :)
        game = app.TicTacToe()
        game.board = ['#',
                      '1', '2', '3',
                      '4', '5', '6',
                      '7', '8', '9'
                      ]
        random_comp_player = player.RandomComputerPlayer('X')
        random_comp_player.get_move(game)

    def test_check_random_computer_player_get_move_returns_value_in_range_of_10_to_4_happy_path(self):
        # test with no assert only check the contract validation :)
        game = app.TicTacToe()
        game.board = ['#',
                      'X', 'X', 'O',
                      'O', '5', '6',
                      '7', '8', '9'
                      ]
        random_comp_player = player.RandomComputerPlayer('X')
        res = random_comp_player.get_move(game)
        self.assertTrue(10 > res > 4)

    def test_check_random_computer_player_get_move_returns_value_in_possible_range_happy_path(self):
        game = app.TicTacToe()
        game.board = ['#',
                      '1', 'X', '3',
                      'O', '5', '6',
                      'O', '8', '9'
                      ]

        random_comp_player = player.RandomComputerPlayer('X')
        res = random_comp_player.get_move(game)
        self.assertTrue(res in [1, 3, 5, 6, 8, 9])

    def test_check_random_computer_player_get_move_returns_the_only_possible_value_happy_path(self):
        game = app.TicTacToe()
        game.board = ['#',
                      'O', 'X', 'O',
                      'O', 'X', 'O',
                      'O', '8', 'X'
                      ]
        random_comp_player = player.RandomComputerPlayer('X')
        res = random_comp_player.get_move(game)
        self.assertEqual(8, res)

    def test_check_random_computer_player_raise_LogicError_exception_when_the_game_is_still_on_and_no_empty_squares_sad_path(
            self):
        game = app.TicTacToe()
        game.board = ['#',
                      'X', 'X', 'O',
                      'O', 'X', 'X',
                      'O', 'X', 'O'
                      ]
        random_comp_player = player.RandomComputerPlayer('X')
        with self.assertRaises(LogicError):
            random_comp_player.get_move(game)


if __name__ == '__main__':
    unittest.main()
