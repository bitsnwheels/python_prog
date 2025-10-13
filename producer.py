import pytest
from fib import fib

def test_fib_base_cases():
    assert fib(0) == 0
    assert fib(1) == 1


def test_fib_small_numbers():
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3
    assert fib(5) == 5

def test_fib_larger_numbers():
    assert fib(9) == 34
    assert fib(10) == 55

def test_fib_negative_numbers():
    with pytest.raises(ValueError):
        fib(-1)
    with pytest.raises(ValueError):
        fib(-10)
