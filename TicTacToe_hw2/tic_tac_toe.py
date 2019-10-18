"""This module contain only class of game tic tac toe.
It's study module for course FullStack Backend of Technoatom.
Start program in this file.
test_tic_tac_toe.py contain test for this class.
"""


class TicTacToe:
    """This class realize game tic tac toe on board 3x3
    :param player1 = choose your side
    :param player2 = choose your side
    run() - start the game
    """

    __slots__ = ["player1", "player2", "cells", "ways_to_win"]

    def __init__(self, player1="+", player2="o"):
        self.player1 = player1
        self.player2 = player2

        self.cells = list(' ' for _ in range(9))

        self.ways_to_win = ((0, 1, 2),
                            (3, 4, 5),
                            (6, 7, 8),
                            (0, 3, 6),
                            (1, 4, 7),
                            (2, 5, 8),
                            (0, 4, 8),
                            (2, 4, 6))

    def display_game(self):
        """This function print to display current status of game"""
        print("\n\t{} | {} | {}".format(self.cells[0], self.cells[1], self.cells[2]))
        print("\t" + "-" * (len(str(self.cells[0]) + str(self.cells[1]) + str(self.cells[2])) + 6))
        print("\t{} | {} | {}".format(self.cells[3], self.cells[4], self.cells[5]))
        print("\t" + "-" * (len(str(self.cells[3]) + str(self.cells[4]) + str(self.cells[5])) + 6))
        print("\t{} | {} | {}".format(self.cells[6], self.cells[7], self.cells[8]) + '\n')

    @staticmethod
    def show_rule():
        """This function show on display rule of game"""
        print("Game tic tac toe")
        print("\t{} | {} | {}".format(0, 1, 2))
        print("\t" + "-" * 9)
        print("\t{} | {} | {}".format(3, 4, 5))
        print("\t" + "-" * 9)
        print("\t{} | {} | {}".format(6, 7, 8) + '\n')

    @staticmethod
    def next_turn(turn):
        """Transfer of the right to thr next player"""
        if turn == 1:
            return 0

        if turn == 0:
            return 1

        raise KeyError

    def who_winner(self, combination):
        """This function checking who is win compare with prepared set"""
        if combination in self.ways_to_win:
            return True

        return False

    def run(self):
        """Start game"""
        self.show_rule()

        winner = False
        turn = 0
        space = ' '

        player_set = [[], []]

        while not winner:
            self.display_game()

            response = self.make_choice(0, 9)
            if self.cells[response] is space:
                if turn:
                    self.cells[response] = self.player2
                    player_set[turn].append(response)
                else:
                    self.cells[response] = self.player1
                    player_set[turn].append(response)

                if space not in self.cells:
                    print("All cells has already filled")
                    break

                player_set[turn].sort()
                if self.who_winner(tuple(player_set[turn])):
                    print(f"{self.player2 if turn else self.player1} win!")
                    self.display_game()
                    break

                turn = self.next_turn(turn)
            else:
                print("This cell has already filled")
                continue

    @staticmethod
    def make_choice(low, high):
        """Take choice of player and take out this choice game"""
        response = None
        while response not in range(low, high):
            response = int(input("Enter a choice -> "))
        return response


if __name__ == "__main__":
    GAME = TicTacToe()
    GAME.run()
