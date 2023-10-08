class Car:

    def __init__(self, capacity: int, gas_per_km: int, gas_to_fill=0):
        self.capacity = capacity
        self.gas_per_km = gas_per_km
        self.gas = 0
        self.fill(gas_to_fill)
        self.milage = 0

    def fill(self, liters: int) -> None:

        if liters > self.capacity - self.gas:
            extra_liters = liters - (self.capacity - self.gas)
            self.gas = self.capacity
            print(f'Tank is full. You have {extra_liters} extra liters')
        else:
            self.gas += liters

    def ride(self, distance: int) -> None:
        max_distance = int(self.gas / self.gas_per_km)
        if distance > max_distance:
            self.gas = 0
            self.milage += max_distance
            print(f'Out of gas. {distance - max_distance}km left to go.')

        self.gas -= self.gas_per_km * distance
        self.milage += distance
