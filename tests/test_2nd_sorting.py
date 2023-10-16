import pytest

from solutions.second_sorting import price_sort


@pytest.mark.parametrize(
    'prices,result',
    [
        ([1, 25, 6, 50], [25, 1, 50, 6]),
        ([4, 80, 5], [80, 4, 5]),
        ([5, 80, 4], [80, 4, 5]),
        ([6], [6]),
        ([2, 1, 10, 50, 10], [10, 2, 50, 1, 10])
    ]
)
def test_price_sort(prices, result):
    assert price_sort(prices) == result
