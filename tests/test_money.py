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
        (Money(10, 0), '10руб 0коп'),
        (Money(10, 99), '10руб 99коп')
    ]
)
def test_str_money(money_given, expected):
    assert str(money_given) == expected


@pytest.mark.parametrize(
    'first_money,second_money,expected',
    [
        (Money(10, 45), Money(10, 55), '21руб 0коп'),
        (Money(10, 101), Money(1, 200), '14руб 1коп'),
        (Money(0, 205), Money(0, 0), '2руб 5коп'),
        (Money(0, 0), Money(0, 205), '2руб 5коп'),
        (Money(10, 99), Money(10, 99), '21руб 98коп')
    ]
)
def test_add_money(first_money, second_money, expected):
    summ = first_money + second_money
    assert isinstance(summ, Money)
    out = StringIO()
    sys.stdout = out
    print(summ)
    assert out.getvalue().strip() == expected

@pytest.mark.parametrize(
    'first_money,second_money,expected',
    [
        (Money(10, 45), Money(10, 55), '0руб -10коп'),
        (Money(10, 101), Money(1, 200), '8руб 1коп'),
        (Money(0, 205), Money(0, 0), '2руб 5коп'),
        (Money(0, 0), Money(0, 205), '-2руб -5коп'),
    ]
)
def test_substract_money(first_money, second_money, expected):
    substraction_res = first_money - second_money
    assert isinstance(substraction_res, Money)
    out = StringIO()
    sys.stdout = out
    print(substraction_res)
    assert out.getvalue().strip() == expected

@pytest.mark.parametrize(
    'first_money,num,expected',
    [
        (Money(10, 45), 3, '31руб 35коп'),
        (Money(10, 101), 5, '55руб 5коп'),
        (Money(0, 205), 0, '0руб 0коп'),
        (Money(0, 0), 2, '0руб 0коп')
    ]
)
def test_mul_money(first_money, num, expected):
    mul = first_money * num
    assert isinstance(mul, Money)
    out = StringIO()
    sys.stdout = out
    print(mul)
    assert out.getvalue().strip() == expected

@pytest.mark.parametrize(
    'first_money,second_money,expected',
    [
        (Money(10, 45), Money(10, 55), False),
        (Money(10, 101), Money(1, 200), True),
        (Money(0, 205), Money(0, 0), True),
        (Money(0, 0), Money(0, 205), False),
    ]
)
def test_gt_money(first_money, second_money, expected):
    result = first_money > second_money
    assert result == expected

@pytest.mark.parametrize(
    'first_money,second_money,expected',
    [
        (Money(10, 45), Money(10, 55), True),
        (Money(10, 101), Money(1, 200), False),
        (Money(0, 205), Money(0, 0), False),
        (Money(0, 0), Money(0, 205), True),
    ]
)
def test_lt_money(first_money, second_money, expected):
    result = first_money < second_money
    assert result == expected

@pytest.mark.parametrize(
    'first_money,second_money,expected',
    [
        (Money(10, 45), Money(10, 55), False),
        (Money(10, 101), Money(0, 1101), True),
        (Money(0, 205), Money(2, 5), True),
        (Money(0, 0), Money(0, 205), False),
    ]
)
def test_eq_money(first_money, second_money, expected):
    result = first_money == second_money
    assert result == expected

@pytest.mark.parametrize(
    'first_money,second_money,expected',
    [
        (Money(10, 45), Money(10, 55), True),
        (Money(10, 101), Money(0, 1101), False),
        (Money(0, 205), Money(2, 5), False),
        (Money(0, 0), Money(0, 205), True),
    ]
)
def test_ne_money(first_money, second_money, expected):
    result = first_money != second_money
    assert result == expected