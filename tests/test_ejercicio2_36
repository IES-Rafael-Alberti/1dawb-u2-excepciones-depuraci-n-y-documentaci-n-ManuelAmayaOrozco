import pytest
from src.ejercicio2_36 import cuentEdad

@pytest.mark.parametrize(
    "input_n1, expected",
    [
      (19, 19),
      (10, 10),
      (24, 24)
    ] 
)
def test_cuentEdad_params(input_n1, expected):
    assert cuentEdad(input_n1) == expected