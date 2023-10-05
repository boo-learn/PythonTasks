import pytest
import sys

from io import StringIO

from solutions.money import Money


@pytest.mark.parametrize(
    'money_given,expected',
    [
        (Money(10, 45), '10руб 45коп'),
        (Money(10, 101), '11руб 1коп'),
        (Money(10, 205), '12руб 5коп'),
        (Money(10, 0), '10руб 0коп')
    ]
)
def test_str_money(money_given, expected):
    out = StringIO()
    sys.stdout = out
    print(money_given)
    assert out.getvalue().strip() == expected
