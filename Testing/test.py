#pip install -U pytest
import pytest
def func(x):
    return x + 1

def test_answer():
    # assert func(5) == 4
    assert func(3) == 4

# pytest test.py