class Player:
    count = 0
    def __init__(self, name):
        self.name = name
        self.count += 1


def test_player_init():
    p = Player("Bob")
    assert p.count == 1
    assert Player.count == 0
