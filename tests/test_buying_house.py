import pytest

from solutions.byuing_house import Human, House


@pytest.fixture
def human_example():
    return Human('Vasilij', start_money=1000)


@pytest.fixture
def house_example():
    return House(1, 5000.15)


def test_house_final_price(house_example):
    house = house_example
    assert house.final_price == 5000.15


def test_human_earn_money(human_example):
    person = human_example
    assert person.money == 1000
    person.earn_money(50)
    assert person.money == 1050
    person.earn_money(56.5)
    assert person.money == 1106.5


def test_human_spend_money(human_example):
    person = human_example
    assert person.money == 1000
    person.spend_money(50)
    assert person.money == 950


def test_person_buy_house(human_example, house_example):
    person = human_example
    house = house_example
    assert not person.have_house
    assert not person.buy_house(house)
    person.earn_money(5000)
    assert person.buy_house(house)


def test_human_have_house(human_example, house_example):
    person = human_example
    house = house_example
    assert not person.have_house
    person.earn_money(5000)
    person.buy_house(house)
    assert person.have_house



