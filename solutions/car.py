class Car:
    def __init__(self, capacity: int, gas_per_km: int, gas=0):
        self.__capacity = capacity
        self.__gas_per_km = gas_per_km
        self.__gas = gas
        self.milage = 0

    def fill(self, liters: int) -> None:

        if liters > self.__capacity - self.__gas:
            extra_liters = liters - (self.__capacity - self.__gas)
            self.__gas = self.__capacity
            print(f'Tank is full. You have {extra_liters} extra liters')

        self.__gas += liters

    def ride(self, milage: int) -> None:
        max_distance = int(self.__gas / self.__gas_per_km)
        if milage > max_distance:
            self.__gas = 0
            self.milage += max_distance

        self.__gas -= self.__gas_per_km * milage
        self.milage += milage
