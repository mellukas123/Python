import what_century
import pytest

@pytest.mark.parametrize("year, century", [(1290, 13), (1734, 18), (1967, 20), (2024, 21)])

def what_century(year):
    pass

def test_century_is(year, century):
    assert what_century.what_century(year) == century