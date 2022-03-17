import unittest
from unittest.mock import MagicMock, patch

import app


class TestHumanVsHuman(unittest.TestCase):

    @patch('builtins.input')
    def test_check_human_vs_human_ends_with_tie_happy_path(self, input_mock: MagicMock):
        input_mock.side_effect = [2, 1, 5, 9, 2, 8, 7, 3, 6, 4]
        res = app.play()
        self.assertEqual('Tie', res)

    @patch('builtins.input')
    def test_check_human_vs_human_X_wins(self, input_mock: MagicMock):
        input_mock.side_effect = [2, 1, 5, 9, 3, 7, 4, 8]
        res = app.play()
        self.assertEqual('X', res)

    @patch('builtins.input')
    def test_check_human_vs_human_O_wins(self, input_mock: MagicMock):
        input_mock.side_effect = [2, 1, 4, 2, 5, 7, 6]
        res = app.play()
        self.assertEqual('O', res)


if __name__ == '__main__':
    unittest.main()
