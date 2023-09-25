from solutions.luna_algo import luna_algo


def test_luna_algo_valid():
    assert luna_algo(8888888888888888) == 'Да'

def test_luna_algo_invalid():
    assert luna_algo(2723000048400011) == 'Нет'
