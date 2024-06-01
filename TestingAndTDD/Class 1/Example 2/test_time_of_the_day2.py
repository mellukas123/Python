import time_of_the_day
import pytest

@pytest.mark.parametrize("time, label", [(6, 'Morning'), (11, 'Day'), (19, 'Evening'), (23, 'Night'), (4, "Night")])
def test_what_time(time, label):
    """ Evaluating that time of the day converts to day time correctly """
    # (7, morning), (10, day), (20, evening), (24, night)
    assert time_of_the_day.what_time(time) == label