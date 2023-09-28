import pytest
from solutions.luna_algo import luna_algo


@pytest.mark.parametrize("card_number", [8888888888888888,
                                         6233720003430773,
                                         5105105105105100,
                                         4012888888881881
                                         ])
def test_luna_algo_valid(card_number):
    assert luna_algo(card_number)


@pytest.mark.parametrize("card_number", [7223000048400011,
                                         5000000000000001,
                                         4652060573334991,
                                         ])
def test_luna_algo_invalid(card_number):
    assert not luna_algo(card_number)