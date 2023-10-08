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
        rub, cent = summ.__min_cents()
        return Money(rub, cent)

    def __sub__(self, other):
        substraction = self.__cents - other.__cents
        rub, cent = substraction.__min_cents()
        return Money(rub, cent)

    def __mul__(self, num):
        money_multiply = self.__cents * num
        rub, cent = money_multiply.__min_cents
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

money1 = Money(10, 45)
money2 = Money(10, 55)
print(money1)