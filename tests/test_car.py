import pytest

from solutions.car import Car


@pytest.fixture
def create_car():
    return Car(500, 25)


def test_car_creation(create_car):
    car = create_car
    assert isinstance(car, Car)


def test_car_fill(create_car):
    car = create_car
    assert car.fill(5) == 'Has 5 liters out of 500'
    assert car.fill(500) == 'Tank is full. You have 5 extra liters'


def test_car_ride(create_car):
    car = create_car
    car.fill(500)
    assert car.ride(10) == 'Trip finished'
    assert car.milage == 10
    assert car.ride(100) == 'Out of gas. 90km left to go.'
    assert car.milage == 20
