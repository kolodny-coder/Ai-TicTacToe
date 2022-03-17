import unittest
import os

from unittest.mock import MagicMock, patch
from io import StringIO

import app
# from test_tic_tac_toe import fixtures
import test_tic_tac_toe.fixtures as fixtures
import player


class TestApp(unittest.TestCase):

    def test_print_the_board_init_state(self):
        c

    def test_check_init_board_will_return_list_with_10_items_happy_path(self):
        game = app.TicTacToe()
        res = game.initiate_board()
        self.assertEqual(len(res), 10)

    def test_print_the_board_when_spot_no_one_mark_with_x(self):
        with patch('sys.stdout', new=StringIO()) as output:
            game = app.TicTacToe()
            game.board = ['#', 'X', '2', '3', '4', '5', '6', '7', '8', '9']
            game.print_the_board()
            self.assertEqual(fixtures.expected_initial_board_with_x_on_the_first_spot, output.getvalue())

    def test_check_for_a_win_diagonal_happy_path1(self):
        game = app.TicTacToe()
        game.board = ['#', 'X', '2', '3', '4', 'X', '6', '7', '8', 'X']
        res = game.check_for_a_win()
        self.assertTrue(res)

    def test_check_for_a_win_diagonal_happy_path2(self):
        game = app.TicTacToe()
        game.board = ['#', '1', '2', 'X', '4', 'X', '6', 'X', '8', '9']
        res = game.check_for_a_win()
        self.assertTrue(res)

    def test_won_in_horizontal_row1_happy_path(self):
        game = app.TicTacToe()
        game.board = ['#', 'X', 'X', 'X', '4', '5', '6', '7', '8', '9']
        res = game.check_for_a_win()
        self.assertTrue(res)

    def test_won_in_horizontal_row2_happy_path(self):
        game = app.TicTacToe()
        game.board = ['#', '1', '2', '3', 'X', 'X', 'X', '7', '8', '9']
        res = game.check_for_a_win()
        self.assertTrue(res)

    def test_won_in_horizontal_row3_happy_path(self):
        game = app.TicTacToe()
        game.board = ['#', '1', '2', '3', '4', '5', '6', 'X', 'X', 'X']
        res = game.check_for_a_win()
        self.assertTrue(res)

    def test_won_in_vertical_column1_happy_path(self):
        game = app.TicTacToe()
        game.board = ['#', 'X', '2', '3', 'X', '5', '6', 'X', '8', '9']
        res = game.check_for_a_win()
        self.assertTrue(res)

    def test_won_in_vertical_column2_happy_path(self):
        game = app.TicTacToe()
        game.board = ['#', '1', 'X', '3', '4', 'X', '6', '7', 'X', '9']
        res = game.check_for_a_win()
        self.assertTrue(res)

    def test_won_in_vertical_column3_happy_path(self):
        game = app.TicTacToe()
        game.board = ['#', '1', '2', 'X', '4', '5', 'X', '7', '8', 'X']
        res = game.check_for_a_win()
        self.assertTrue(res)

    def test_won_in_vertical_column1_sad_path(self):
        game = app.TicTacToe()
        game.board = ['#', '1', '2', 'X', '4', '5', 'O', '7', '8', 'X']
        res = game.check_for_a_win()
        self.assertFalse(res)

    def test_won_in_vertical_column2_sad_path(self):
        game = app.TicTacToe()
        game.board = ['#', '1', '2', 'O', '4', '5', 'X', '7', '8', 'X']
        res = game.check_for_a_win()
        self.assertFalse(res)

    def test_won_in_vertical_column3_sad_path(self):
        game = app.TicTacToe()
        game.board = ['#', '1', '2', '3', '4', '5', 'X', '7', '8', 'X']
        res = game.check_for_a_win()
        self.assertFalse(res)

    def test_won_sad_path_random1(self):
        game = app.TicTacToe()
        game.board = ['#', '1', 'X', 'X', 'X', '5', 'X', 'X', '8', 'X']
        res = game.check_for_a_win()
        self.assertTrue(res)

    def test_are_there_any_empty_spaces_available_happy_path(self):
        game = app.TicTacToe()
        game.board = ['#', '1', 'X', 'X', 'X', '5', 'X', 'X', '8', 'X']
        res = game.check_if_there_are_any_empty_squares()
        self.assertTrue(res)

    def test_are_there_any_empty_spaces_available_inital_board_happy_path(self):
        game = app.TicTacToe()
        game.board = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        res = game.check_if_there_are_any_empty_squares()
        self.assertTrue(res)

    def test_are_there_any_empty_spaces_available_sad_path(self):
        game = app.TicTacToe()
        game.board = ['#', 'O', 'X', 'X', 'X', 'O', 'X', 'X', 'O', 'X']
        res = game.check_if_there_are_any_empty_squares()
        self.assertFalse(res)

    def test_are_there_any_empty_spaces_one_spot_available_sad_path(self):
        game = app.TicTacToe()
        game.board = ['#', 'O', '2', 'X', 'X', 'O', 'X', 'X', 'O', 'X']
        res = game.check_if_there_are_any_empty_squares()
        self.assertTrue(res)

    def test_calculate_the_number_of_empty_squares_on_the_board_happy_path_1_empty(self):
        game = app.TicTacToe()
        game.board = ['#', 'O', '2', 'X', 'X', 'O', 'X', 'X', 'O', 'X']
        res = game.calculate_the_number_of_empty_squares_on_the_board()
        self.assertEqual(1, res)

    def test_calculate_the_number_of_empty_squares_on_the_board_2_empty_happy_path_(self):
        game = app.TicTacToe()
        game.board = ['#', 'O', '2', '3', 'X', 'O', 'X', 'X', 'O', 'X']
        res = game.calculate_the_number_of_empty_squares_on_the_board()
        self.assertEqual(2, res)

    def test_calculate_the_number_of_empty_squares_on_the_board_3_empty_happy_path_(self):
        game = app.TicTacToe()
        game.board = ['#', '1', '2', '3', 'X', 'O', 'X', 'X', 'O', 'X']
        res = game.calculate_the_number_of_empty_squares_on_the_board()
        self.assertEqual(3, res)

    def test_calculate_the_number_of_empty_squares_on_the_board_4_empty_happy_path_(self):
        game = app.TicTacToe()
        game.board = ['#', '1', '2', '3', '4', 'O', 'X', 'X', 'O', 'X']
        res = game.calculate_the_number_of_empty_squares_on_the_board()
        self.assertEqual(4, res)

    def test_calculate_the_number_of_empty_squares_on_the_board_5_empty_happy_path_(self):
        game = app.TicTacToe()
        game.board = ['#', '1', '2', '3', '4', '5', 'X', 'X', 'O', 'X']
        res = game.calculate_the_number_of_empty_squares_on_the_board()
        self.assertEqual(5, res)

    def test_calculate_the_number_of_empty_squares_on_the_board_6_empty_happy_path_(self):
        game = app.TicTacToe()
        game.board = ['#', '1', '2', '3', '4', '5', '6', 'X', 'O', 'X']
        res = game.calculate_the_number_of_empty_squares_on_the_board()
        self.assertEqual(6, res)

    def test_calculate_the_number_of_empty_squares_on_the_board_7_empty_happy_path_(self):
        game = app.TicTacToe()
        game.board = ['#', '1', '2', '3', '4', '5', '6', '7', 'O', 'X']
        res = game.calculate_the_number_of_empty_squares_on_the_board()
        self.assertEqual(7, res)

    def test_calculate_the_number_of_empty_squares_on_the_board_8_empty_happy_path_(self):
        game = app.TicTacToe()
        game.board = ['#', '1', '2', '3', '4', '5', '6', '7', '8', 'X']
        res = game.calculate_the_number_of_empty_squares_on_the_board()
        self.assertEqual(8, res)

    def test_calculate_the_number_of_empty_squares_on_the_board_9_empty_happy_path_(self):
        game = app.TicTacToe()
        game.board = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        res = game.calculate_the_number_of_empty_squares_on_the_board()
        self.assertEqual(9, res)

    def test_calculate_the_number_of_empty_squares_on_the_board_0_empty_happy_path_(self):
        game = app.TicTacToe()
        game.board = ['#', 'X', 'O', 'O', 'X', 'O', 'X', 'O', 'X', 'X']
        res = game.calculate_the_number_of_empty_squares_on_the_board()
        self.assertEqual(0, res)

    def test_return_the_available_moves_on_the_current_board_9_moves_happy_path(self):
        game = app.TicTacToe()
        game.board = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        res = game.return_the_available_moves_on_the_current_board_as_a_list_of_integers()
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], res)

    def test_return_the_available_moves_on_the_current_board_9_moves_sad_path(self):
        game = app.TicTacToe()
        game.board = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        res = game.return_the_available_moves_on_the_current_board_as_a_list_of_integers()
        self.assertNotEqual([1, 3, 4, 5, 6, 7, 8, 9], res)

    def test_return_the_available_moves_on_the_current_board_7_moves_happy_path(self):
        game = app.TicTacToe()
        game.board = ['#', '1', 'X', '3', 'O', '5', '6', '7', '8', '9']
        res = game.return_the_available_moves_on_the_current_board_as_a_list_of_integers()
        self.assertEqual([1, 3, 5, 6, 7, 8, 9], res)

    def test_return_the_available_moves_on_the_current_board_7_moves_sad_path(self):
        game = app.TicTacToe()
        game.board = ['#', '1', 'X', '3', 'O', '5', '6', '7', '8', '9']
        res = game.return_the_available_moves_on_the_current_board_as_a_list_of_integers()
        self.assertNotEqual([1, 3, 4, 5, 6, 7, 8, 9], res)

    def test_return_the_available_moves_on_the_current_board_0_moves_happy_path(self):
        game = app.TicTacToe()
        game.board = ['#', 'O', 'X', 'X', 'O', 'O', 'X', 'X', 'O', 'X']
        res = game.return_the_available_moves_on_the_current_board_as_a_list_of_integers()
        self.assertEqual([], res)

    def test_return_the_available_moves_on_the_current_board_0_moves_sad_path(self):
        game = app.TicTacToe()
        game.board = ['#', '1', 'X', 'X', 'O', 'O', 'X', 'X', 'O', 'X']
        res = game.return_the_available_moves_on_the_current_board_as_a_list_of_integers()
        self.assertNotEqual([], res)

    @patch('builtins.input')
    def test_minmax_check_if_X_wins_1_happy_path(self, input_mock: MagicMock):
        input_mock.side_effect = [4]
        board = ['#', 'X', '2', 'O', '4', 'X', '6', '7', 'O', '9']
        res = app.play(board=board)
        self.assertEqual('X', res)

    @patch('builtins.input')
    def test_check_that_smart_bot_vs_smart_bot_ends_with_tie(self, input_mock: MagicMock):
        input_mock.side_effect = [5]
        res = app.play()
        self.assertEqual('Tie', res)

    # check check_if_there_are_any_empty_squares Function

    def test_check_if_there_are_any_empty_squares_happy_path_1_empty_square(self):
        game = app.TicTacToe()
        game.board = ['#', '1', 'X', 'X', 'O', 'O', 'X', 'X', 'O', 'X']
        res = game.check_if_there_are_any_empty_squares()
        self.assertTrue(res)

    def test_check_if_there_are_any_empty_squares_happy_path_2_empty_square(self):
        game = app.TicTacToe()
        game.board = ['#', '1', 'X', '3', 'O', 'O', 'X', 'X', 'O', 'X']
        res = game.check_if_there_are_any_empty_squares()
        self.assertTrue(res)

    def test_check_if_there_are_any_empty_squares_happy_path_3_empty_square(self):
        game = app.TicTacToe()
        game.board = ['#', '1', '2', '3', 'O', 'O', 'X', 'X', 'O', 'X']
        res = game.check_if_there_are_any_empty_squares()
        self.assertTrue(res)

    def test_check_if_there_are_any_empty_squares_happy_path_4_empty_square(self):
        game = app.TicTacToe()
        game.board = ['#', '1', '2', '3', '4', 'O', 'X', 'X', 'O', 'X']
        res = game.check_if_there_are_any_empty_squares()
        self.assertTrue(res)

    def test_check_if_there_are_any_empty_squares_happy_path_5_empty_square(self):
        game = app.TicTacToe()
        game.board = ['#', '1', '2', '3', '4', '5', 'X', 'X', 'O', 'X']
        res = game.check_if_there_are_any_empty_squares()
        self.assertTrue(res)

    def test_check_if_there_are_any_empty_squares_happy_path_6_empty_square(self):
        game = app.TicTacToe()
        game.board = ['#', '1', '2', '3', '4', '5', '6', 'X', 'O', 'X']
        res = game.check_if_there_are_any_empty_squares()
        self.assertTrue(res)

    def test_check_if_there_are_any_empty_squares_happy_path_7_empty_square(self):
        game = app.TicTacToe()
        game.board = ['#', '1', '2', '3', '4', '5', '6', '7', 'O', 'X']
        res = game.check_if_there_are_any_empty_squares()
        self.assertTrue(res)

    def test_check_if_there_are_any_empty_squares_happy_path_8_empty_square(self):
        game = app.TicTacToe()
        game.board = ['#', '1', '2', '3', '4', '5', '6', '7', '8', 'X']
        res = game.check_if_there_are_any_empty_squares()
        self.assertTrue(res)

    def test_check_if_there_are_any_empty_squares_happy_path_9_empty_square(self):
        game = app.TicTacToe()
        game.board = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        res = game.check_if_there_are_any_empty_squares()
        self.assertTrue(res)

    def test_check_if_there_are_any_empty_squares_happy_path_0_empty_square(self):
        game = app.TicTacToe()
        game.board = ['#', 'X', 'O', 'O', 'O', 'X', 'O', 'X', 'O', 'X']
        res = game.check_if_there_are_any_empty_squares()
        self.assertFalse(res)


if __name__ == '__main__':
    unittest.main()
