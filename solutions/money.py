import math


class Money:
    def __init__(self, rub: int, cents: int):
        self.__cents = cents + rub * 100

    @staticmethod
    def __cents_and_rubs(cents) -> tuple[int, int]:
        rub_in_cents = cents // 100
        actual_cents = cents % 100

        return rub_in_cents, actual_cents

    def __str__(self):
        rubs_from_cents, cents_left = self.__cents_and_rubs(self.__cents)
        return f'{rubs_from_cents}руб {cents_left}коп'

    def __add__(self, other):
        summ = self.__cents + other.__cents
        rub, cent = self.__cents_and_rubs(summ)
        return Money(rub, cent)

    def __sub__(self, other):
        substraction = self.__cents - other.__cents
        rub, cent = self.__cents_and_rubs(substraction)
        return Money(rub, cent)

    def __mul__(self, num):
        money_multiply = self.__cents * num
        rub, cent = self.__cents_and_rubs(money_multiply)
        return Money(rub, cent)

    def __gt__(self, other):
        return self.__cents > other.__cents

    def __lt__(self, other):
        return self.__cents < other.__cents

    def __eq__(self, other):
        return self.__cents == other.__cents

    def __ne__(self, other):
        return self.__cents != other.__cents

money1 = Money(10, 45)
money2 = Money(10, 55)
print(money1)