import mathlib


def test_addition():
    """ Testing the addition """
    assert mathlib.addition(1, 2) == 3
    assert mathlib.addition(1, -5) == -4
    assert type(mathlib.addition(1, 2)) == type(9)


def test_multiply():
    """" Testing the multiply functionality """
    assert mathlib.multiply(2, 2) == 4
    assert mathlib.multiply(2, -2) == -4
    assert type(mathlib.multiply(1, 2)) == type(9)


def test_text():
    """ Testing the addition """
    assert 'a' in 'asdasdasd'