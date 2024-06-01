import function2

def test_factorial():
    """ Testing the factorial"""
    assert function2.factorial(0) == 1
    assert function2.factorial(1) == 1
    assert function2.factorial(5) == 120


