from mocks import source


def test_should_return_perimeter(mocker):
    mocker.patch.object(source, 'PI', 3.14)
    expected_value = 12.56
    assert source.perimeter(2) == expected_value


def test_main_function(mocker):
    mocker.patch('mocks.source.request', return_value=100)

    expected_value = 100
    assert source.main_function() == expected_value


class MockResponse:
    @staticmethod
    def get_info():
        return {"name": "test", "level": 200}


def test_create_player(mocker):
    mocker.patch('mocks.source.Player', return_value=MockResponse())

    expected_value = {"name": "test", "level": 200}
    assert source.create_player() == expected_value


def test_fighter_attack(mocker):
    weapon1 = source.Weapon(10)
    weapon2 = source.Weapon(5)

    fighter1 = source.Fighter("San-Goku", weapon1)
    fighter2 = source.Fighter("Freezer", weapon2)

    mocker.patch("mocks.source.Weapon.damage", return_value=20)

    fighter1.attack(fighter2)

    expected_value = 80

    assert fighter2.get_life_point() == expected_value
