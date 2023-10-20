from calculate.view import View


def test_should_print_menu(capsys):
    View.print_menu()
    out, err = capsys.readouterr()
    expected_out = ("\n=========== MENU ==========="
                    "\n1 - Addition"
                    "\n2 - Soustraction"
                    "\n3 - Multiplication"
                    "\n4 - Division"
                    "\n5 - Quitter"
                    "\n============================\n\n")
    assert out == expected_out


def test_should_print_end_message(capsys):
    View.end_message()
    out, err = capsys.readouterr()
    expected_out = "=========== GOOD-BYE ===========\n"
    assert out == expected_out


def test_should_print_result_with_no_error(capsys):
    operation = "1 + 1"
    result = 2
    View.print_result(operation, result)
    out, err = capsys.readouterr()
    expected_out = f"RESULTAT : {operation} = {result}\n"
    assert out == expected_out


def test_should_print_result_with_error(capsys):
    operation = "1 + 1"
    result = None
    View.print_result(operation, result)
    out, err = capsys.readouterr()
    expected_out = f"Votre operation est incorrect ! : {operation}\n"
    assert out == expected_out
