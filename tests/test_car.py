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


@pytest.mark.parametrize(
    'car,gas_to_fill,result',
    [
        (Car(400, 25), 0, 0),
        (Car(600, 25, gas_to_fill=10), 10, 20),
        (Car(500, 25, gas_to_fill=600), 500, 500),
        (Car(200, 20, gas_to_fill=100), 150, 200)
    ]
)
def test_car_fill(car, gas_to_fill, result):
    car.fill(gas_to_fill)
    assert car.gas == result


@pytest.mark.parametrize(
    'car,distance,result_milage,result_gas',
    [
        (Car(400, 25), 0, 0, 0),
        (Car(600, 25, gas_to_fill=600), 10, 10, 350),
        (Car(500, 1, gas_to_fill=600), 500, 500, 0),
        (Car(200, 20, gas_to_fill=100), 10, 5, 0)
    ]
)
def test_car_ride(car, distance, result_milage, result_gas):
    car.ride(distance)
    assert car.milage == result_milage
    assert car.gas == result_gas
