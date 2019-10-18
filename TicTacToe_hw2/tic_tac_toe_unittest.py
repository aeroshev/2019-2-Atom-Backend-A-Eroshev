import unittest
from tic_tac_toe import TicTacToe


class UnitTestTicTacToe(unittest.TestCase):
    def test_who_winner(self):
        game = TicTacToe()

        self.assertTrue(game.who_winner((0, 1, 2)))
        self.assertTrue(game.who_winner((3, 4, 5)))
        self.assertTrue(game.who_winner((6, 7, 8)))
        self.assertTrue(game.who_winner((0, 3, 6)))
        self.assertTrue(game.who_winner((1, 4, 7)))
        self.assertTrue(game.who_winner((2, 5, 8)))
        self.assertTrue(game.who_winner((0, 4, 8)))
        self.assertTrue(game.who_winner((2, 4, 6)))

        self.assertFalse(game.who_winner([0, 1, 2]))
        self.assertFalse(game.who_winner(set([0, 1, 2])))
        self.assertFalse(game.who_winner((2, 1, 0)))
        self.assertFalse(game.who_winner("string"))
        self.assertFalse(game.who_winner(1))
        self.assertFalse(game.who_winner(0.1234))

    def test_next_turn(self):
        game = TicTacToe()

        self.assertEqual(game.next_turn(1), 0)
        self.assertEqual(game.next_turn(0), 1)

        self.assertRaises(KeyError, game.next_turn(2))
        self.assertRaises(KeyError, game.next_turn(-1))
        self.assertRaises(KeyError, game.next_turn("string"))
        self.assertRaises(KeyError, game.next_turn([1, 1, 1]))


if __name__ == '__main__':
    unittest.main()
