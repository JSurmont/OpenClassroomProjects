from calculate.controller import Controller


def test_addition(mocker):
    sut = Controller()

    expected_value = 1.0

    mock = mocker.patch('calculate.view.View.get_user_input')
    mock.side_effect = ["1", "10+10", "5"]
    mocker.patch('calculate.operators.Operators.addition',
                 return_value=expected_value)
    mocker.patch('calculate.view.View.continue_message')

    sut.run()
    assert sut.result == expected_value


def test_subtraction(mocker):
    sut = Controller()

    expected_value = 2.0

    mock = mocker.patch('calculate.view.View.get_user_input')
    mock.side_effect = ["2", "10-10", "5"]
    mocker.patch('calculate.operators.Operators.subtraction',
                 return_value=expected_value)
    mocker.patch('calculate.view.View.continue_message')

    sut.run()
    assert sut.result == expected_value


def test_multiplication(mocker):
    sut = Controller()

    expected_value = 3.0

    mock = mocker.patch('calculate.view.View.get_user_input')
    mock.side_effect = ["3", "10*10", "5"]
    mocker.patch('calculate.operators.Operators.multiplication',
                 return_value=expected_value)
    mocker.patch('calculate.view.View.continue_message')

    sut.run()
    assert sut.result == expected_value


def test_division(mocker):
    sut = Controller()

    expected_value = 4.0

    mock = mocker.patch('calculate.view.View.get_user_input')
    mock.side_effect = ["4", "10/10", "5"]
    mocker.patch('calculate.operators.Operators.division',
                 return_value=expected_value)
    mocker.patch('calculate.view.View.continue_message')

    sut.run()
    assert sut.result == expected_value


def test_quit(mocker):
    sut = Controller()

    mock = mocker.patch('calculate.view.View.get_user_input')
    mock.side_effect = ["5"]

    sut.run()
    assert sut.result is None


def test_quit_without_infinite_loop(mocker):
    sut = Controller()
    mock = mocker.patch('calculate.view.View.get_user_input',
                        return_value=5)
