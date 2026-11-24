import pytest
from a3 import *

def test_is_prime():
    assert is_prime(1) == False
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(7) == True
    assert is_prime(10) == False
    assert is_prime(17) == True
    assert is_prime(25) == False
pytest.main()