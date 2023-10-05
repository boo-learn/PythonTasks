class Money:
    def __init__(self, rub: int, cents: int):
        self.__rub = rub
        self.__cents = cents

    def __min_cents(self) -> tuple:
        rub_in_cents = self.__cents // 100
        actual_cents = self.__cents % 100

        return rub_in_cents, actual_cents

    def __str__(self):
        rubs_from_cents, cents_left = self.__min_cents()
        return f'{rubs_from_cents + self.__rub}руб {cents_left}коп'
