class TicTacToe:

    def __init__(self):
        self.board = self.initiate_board()
        self.current_winner = None

    def initiate_board(self) -> list[10]:
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

    def make_a_move(self, square, letter):
        if self.board[square] == '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9':
            self.board[square] = letter
            # chcek for win
            if self.check_for_a_win():
                self.current_winner = letter

            return True
        return False

    def check_for_a_win(self):
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

    def check_if_there_are_any_empty_squares(self):
        return ('1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9') in self.board

    def calculate_the_number_of_empty_squares_on_the_board(self):
        counter = 0
        for i in self.board:
            if i in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                counter += 1
        return counter

    def return_the_available_moves_on_the_current_board_as_a_list_of_integers(self):
        available_moves_list = [int(i) for i in self.board if i in ['1', '2', '3', '4', '5', '6', '7', '8', '9']]
        return available_moves_list


if __name__ == '__main__':
    game = TicTacToe()

    game.print_the_board()
