from tic_tac_toe import TicTacToe


def test_who_winner():
    game = TicTacToe()
    assert_true = True
    assert_false = False

    assert game.who_winner((0, 1, 2)) == assert_true
    assert game.who_winner((3, 4, 5)) == assert_true
    assert game.who_winner((6, 7, 8)) == assert_true
    assert game.who_winner((0, 3, 6)) == assert_true
    assert game.who_winner((1, 4, 7)) == assert_true
    assert game.who_winner((2, 5, 8)) == assert_true
    assert game.who_winner((0, 4, 8)) == assert_true
    assert game.who_winner((2, 4, 6)) == assert_true

    assert game.who_winner([0, 1, 2]) == assert_false
    assert game.who_winner(set([0, 1, 2])) == assert_false
    assert game.who_winner((2, 1, 0)) == assert_false
    assert game.who_winner("string") == assert_false
    assert game.who_winner(1) == assert_false
    assert game.who_winner(0.1234) == assert_false


def test_next_turn():
    game = TicTacToe()

    assert game.next_turn(1) == 0
    assert game.next_turn(0) == 1

    try:
        game.next_turn(2)
    except KeyError:
        pass

    try:
        game.next_turn(-1)
    except KeyError:
        pass

    try:
        game.next_turn("string")
    except KeyError:
        pass

    try:
        game.next_turn([1, 1, 1])
    except KeyError:
        pass

