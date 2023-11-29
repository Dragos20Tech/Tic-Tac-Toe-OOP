from board import Board
from player import Player


class TicTacToeGame:

    def start(self):
        print("**************************")
        print("  Welcome to Tic-Tac-Toe  ")
        print("**************************")

        board = Board()
        player = Player()
        computer = Player(False)

        board.print_board()

        while True:

            while True:

                player_move = player.get_move()
                board.submit_move(player, player_move)
                board.print_board()

                if board.check_is_game_over(player, player_move):
                    print("Awesome. You won the game! 🎉")
                    break
                elif board.check_is_tie():
                    print("It's a tie! 👍 Try again.")
                    break
                else:
                    computer_move = computer.get_move()
                    board.submit_move(computer, computer_move)
                    board.print_board()

                    if board.check_is_game_over(computer, computer_move):
                        print("Oops... 😱 The Computer Won. Try again.")
                        break
            try:
                play_again = input("Would you like to play again? (Y/N): ").upper().strip()

                if play_again == "N":
                    print("Bye! Come back soon 👋")
                    break
                elif play_again == "Y":
                    self.start_new_round(board, player)
                else:
                    print("Your input was not valid but I will assume that you want to play again. 💡")
                    self.start_new_round(board, player)
            except KeyboardInterrupt as e:
                print(e)

    def start_new_round(self, board, player):
        print("\n*************")
        print("  New Round  ")
        print("*************")
        board.reset_board()
        board.print_board()
        player.reset_valid_moves()


game = TicTacToeGame()
game.start()
