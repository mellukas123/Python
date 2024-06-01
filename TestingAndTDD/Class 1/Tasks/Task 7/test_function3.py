import function3


def test_calculator():
    assert function3.calculator('+', 1, 1) == 2
    assert function3.calculator('-', 2, 1) == 1
    assert function3.calculator('*', 2, 2) == 4
    assert function3.calculator('/', 4, 2) == 2
    try:
        function3.calculator('/', 3, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero."
    else:
        assert False, "Expected ValueError"