class Car():
    def __init__(self, capacity: int, gas_per_km: int, gas=0):
        self.__capacity = capacity
        self.__gas_per_km = gas_per_km
        self.__gas = gas

    def fill(self, liters: int) -> str:

        if liters > self.__capacity - self.__gas:
            extra_liters = liters - (self.__capacity - self.__gas)
            self.__gas = self.__capacity
            return f'Tank is full. You have {extra_liters} extra liters'

        self.__gas += liters
        return f'Has {self.__gas} liters out of {self.__capacity}'
