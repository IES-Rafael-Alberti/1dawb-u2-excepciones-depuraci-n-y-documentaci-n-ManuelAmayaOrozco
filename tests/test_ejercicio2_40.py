import pytest
from src.ejercicio2_40 import tPassword

def test_tPassword_ValueError():
    with pytest.raises(ValueError):
        tPassword("nada")