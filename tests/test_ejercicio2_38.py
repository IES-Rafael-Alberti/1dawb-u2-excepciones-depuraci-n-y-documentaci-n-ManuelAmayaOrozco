import pytest
from src.ejercicio2_38 import cuentAtras

@pytest.mark.parametrize(
    "input_n1, expected",
    [
      (3, "3, 2, 1, 0"),
      (9, "9, 8, 7, 6, 5, 4, 3, 2, 1, 0"),
      (8, "8, 7, 6, 5, 4, 3, 2, 1, 0")
    ] 
)
def test_cuentAtras_params(input_n1, expected):
    assert cuentAtras(input_n1) == expected
    

def test_cuentAtras_ValueError():
    with pytest.raises(ValueError):
        cuentAtras(-3)
        cuentAtras(9.9)