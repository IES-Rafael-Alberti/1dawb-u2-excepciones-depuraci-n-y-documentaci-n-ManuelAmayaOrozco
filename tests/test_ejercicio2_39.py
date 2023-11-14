import pytest
from src.ejercicio2_39 import enterNum

def test_enterNum_ValueError():
    with pytest.raises(ValueError):
        enterNum(8.8)