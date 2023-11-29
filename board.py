import sys

SUCCESS = 0
ERROR_GENERIC = 1
ERROR_CUSTOM = 2

"""
sys.exit(0): Indicates a successful and normal exit.
sys.exit(1): Typically indicates a generic error.
sys.exit(2): Could be used to represent a different kind of error.
"""


class Board:
    EMPTY_CELL = 0

    def __init__(self):
        self.game_board = [[0, 0, 0],
                           [0, 0, 0],
                           [0, 0, 0]]

    def print_board(self):
        """
        The "end" parameter's default argument is "\n" meaning that is printing a new line each time we call
        the function print.

        In order to output our board correctly we must assign to our "end" parameter an empty string "".
        """
        print("\nPositions:")
        self.print_board_with_positions()

        print("Board: ")

        for row in self.game_board:
            print("|", end="")
            for column in row:
                if column == Board.EMPTY_CELL:
                    print("   |", end="")
                else:
                    print(f" {column} |", end="")
            print()
        print()

    def print_board_with_positions(self):
        print("| 1 | 2 | 3 |\n| 4 | 5 | 6 |\n| 7 | 8 | 9 |")

    def submit_move(self, player, move):
        if move is None:
            print("See you next time!")
            sys.exit(ERROR_CUSTOM)

        row = move.get_row()
        col = move.get_column()

        value = self.game_board[row][col]

        if value == Board.EMPTY_CELL:
            self.game_board[row][col] = player.marker
            return True
        else:
            raise ValueError("This position is already taken. Please enter another one.")

    def check_is_game_over(self, player, last_move):
        return ((self.check_row(player, last_move))
                or (self.check_column(player, last_move))
                or (self.check_diagonal(player))
                or self.check_antidiagonal(player))

    def check_row(self, player, last_move):
        row_index = last_move.get_row()
        board_row = self.game_board[row_index]

        # Checking each cell of the row board
        for cell in board_row:
            if cell != player.marker:
                return False  # If any cell in the row does not have the same marker as the player, return False.
        return True  # If all cells in the row have the same marker as the player, return True.

    def check_column(self, player, last_move):
        markers_count = 0
        column_index = last_move.get_column()

        for i in range(3):
            if self.game_board[i][column_index] == player.marker:
                markers_count += 1

        return markers_count == 3

    def check_diagonal(self, player):
        markers_count = 0

        for i in range(3):
            if self.game_board[i][i] == player.marker:
                markers_count += 1

        return markers_count == 3

    def check_antidiagonal(self, player):
        markers_count = 0

        for i in range(3):
            if self.game_board[i][2-i] == player.marker:
                markers_count += 1

        return markers_count == 3

    def check_is_tie(self):
        for row in self.game_board:
            if Board.EMPTY_CELL in row:
                return False
        return True

    def reset_board(self):
        self.game_board = [[0, 0, 0],
                           [0, 0, 0],
                           [0, 0, 0]]
