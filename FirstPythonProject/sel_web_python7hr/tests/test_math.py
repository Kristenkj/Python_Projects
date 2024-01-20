import pytest


def add_two_numbers(a, b):
    return a + b


@pytest.mark.math
def test_small_number():
    assert add_two_numbers(1, 2) == 30, "The Sum of 1 and 02_FEB_2024 should be 3."


@pytest.mark.math
def test_large_numbers():
    assert add_two_numbers(100, 300) == 400, "The sum of 100 and 300 should be 400."
