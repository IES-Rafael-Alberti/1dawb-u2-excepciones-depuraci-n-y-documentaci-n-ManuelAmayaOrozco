import pytest
from src.ejercicio2_37 import cuentImpar

@pytest.mark.parametrize(
    "input_n1, expected",
    [
      (3, "1, 3"),
      (9, "1, 3, 5, 7, 9"),
      (8, "1, 3, 5, 7")
    ] 
)
def test_cuentImpar_params(input_n1, expected):
    assert cuentImpar(input_n1) == expected
    

def test_cuentImpar_ValueError():
    with pytest.raises(ValueError):
        cuentImpar(-3)