import random

from board import Board
from move import Move


class Player:
    # Easier to maintain in case we want to extend our code
    PLAYER_MARKER = "X"
    COMPUTER_MARKER = "O"
    VALID_MOVES = list(range(1, 10))

    def __init__(self, is_human=True):
        self._is_human = is_human

        if is_human:
            self._marker = Player.PLAYER_MARKER
        else:
            self._marker = Player.COMPUTER_MARKER

    @property
    def is_human(self):
        return self._is_human

    @property
    def marker(self):
        return self._marker

    def get_move(self):
        if self._is_human:
            return self.get_human_move()
        else:
            return self.get_computer_move()

    def get_human_move(self):
        try:
            while True:
                user_input = int(input("Please enter your move (1-9): "))
                if user_input in Player.VALID_MOVES:
                    Player.VALID_MOVES.remove(user_input)
                    move = Move(user_input)
                    break
                else:
                    board = Board()
                    print()
                    board.print_board_with_positions()
                    print(f"Positions on the board that are available: {', '.join(map(str, Player.VALID_MOVES))}\n")
            return move
        except KeyboardInterrupt as e:
            print(e)

    def get_computer_move(self):
        # Check if there are no valid moves left
        if not Player.VALID_MOVES:
            return None

        # Choose a random move from the list of valid moves
        random_choice = random.choice(Player.VALID_MOVES)
        Player.VALID_MOVES.remove(random_choice)

        move = Move(random_choice)
        print("Computer move (1-9): ", move.value)
        return move

    def reset_valid_moves(self):
        Player.VALID_MOVES = list(range(1, 10))

# computer = Player(False)

# movee = computer.get_move() # get_move returns a move object

# print(movee)
