import pytest


class Player:
    count = 0

    def __init__(self, name):
        self.name = name
        self.count += 1


def test_player_init():
    p = Player("Bob")
    assert p.count == 1
    assert Player.count == 0


def test_unicode():
    assert len("Krakoẃ") == 6  # with digraph from vim
    assert len("Kraków") == 7
    assert len("Kraków") == 6


def test_almost_equal():
    x = 1.1
    # assert x * x == 1.21
    assert pytest.approx(x * x) == 1.21
