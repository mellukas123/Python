import function1


def test_fibonacci():
    """ Testing the fibonacci """
    assert function1.fibonacci(1) == 1
    assert function1.fibonacci(0) == 0
    assert function1.fibonacci(2) == 1
    assert function1.fibonacci(10) == 55
