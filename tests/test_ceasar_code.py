import pytest
from solutions.ceasar_code import ceasar_encode


@pytest.mark.parametrize("base, encoded", [
    ('gyjxz', 'jbmac'),
    ('gYjXZ', 'jBmAC')
])
def test_ceasar_encode_end_letters(base, encoded):
    assert ceasar_encode(base) == encoded


def test_ceasar_encode_symbols_and_digits_remain():
    assert ceasar_encode('a $+= ]1') == 'd $+= ]1'


def test_ceasar_encode_upper_and_lower():
    assert ceasar_encode('Aa bD') == 'Dd eG'


def test_ceasar_encode_empty_string():
    assert ceasar_encode('') == ''
