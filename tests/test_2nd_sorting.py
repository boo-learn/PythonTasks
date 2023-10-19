import pytest

from solutions.second_sorting import paycheck_best_sum


@pytest.mark.parametrize(
    'prices,result',
    [
        ([1, 25, 6, 50], 75),
        ([4, 80, 5], 85),
        ([5, 80, 4], 85),
        ([6], 6),
        ([2, 1, 10, 50, 10], 70),
        ([2, 1, 10, 50, 10, 10], 70),
        ([2, 1, 10, 50, 10, 12], 72)
    ]
)
def test_price_sort(prices, result):
    assert paycheck_best_sum(prices) == result
