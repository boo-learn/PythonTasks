import math


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

    def __add__(self, other):
        rub = self.__rub + other.__rub
        cents = self.__cents + other.__cents
        return Money(rub, cents)

    def __sub__(self, other):
        all_money = (self.__rub + (self.__cents / 100)) - (other.__rub + (other.__cents / 100))
        if all_money < 0:
            return Money(0, 0)
        cent, rub = math.modf(all_money)
        rub = int(rub)
        cent = int(round(cent, 2) * 100)
        return Money(rub, cent)

    def __mul__(self, num):
        self_all_money = self.__rub + (self.__cents / 100)
        money_multiply = self_all_money * num
        cent, rub = math.modf(money_multiply)
        rub = int(rub)
        cent = int(round(cent, 2) * 100)
        return Money(rub, cent)

    def __gt__(self, other):
        self_money = self.__rub + (self.__cents / 100)
        other_money = other.__rub + (other.__cents / 100)
        return self_money > other_money

    def __lt__(self, other):
        self_money = self.__rub + (self.__cents / 100)
        other_money = other.__rub + (other.__cents / 100)
        return self_money < other_money

    def __eq__(self, other):
        self_money = self.__rub + (self.__cents / 100)
        other_money = other.__rub + (other.__cents / 100)
        return self_money == other_money

    def __ne__(self, other):
        self_money = self.__rub + (self.__cents / 100)
        other_money = other.__rub + (other.__cents / 100)
        return self_money != other_money

