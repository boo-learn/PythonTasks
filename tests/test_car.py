import pytest

from solutions.car import Car


@pytest.mark.parametrize(
    'car,gas_in_tank',
    [
        (Car(400, 25), 0),
        (Car(600, 25, gas_to_fill=10), 10),
        (Car(500, 25, gas_to_fill=600), 500)
    ]
)
def test_car_creation(car, gas_in_tank):
    assert car.gas == gas_in_tank


def test_car_fill(create_car):
    car = create_car
    assert car.fill(500) == 'Tank is full. You have 5 extra liters'


def test_car_ride(create_car):
    car = create_car
    car.fill(500)
    assert car.ride(10)
    assert car.milage == 10
    assert str(car.ride(100)) == 'Out of gas. 90km left to go.'
    assert car.milage == 20
