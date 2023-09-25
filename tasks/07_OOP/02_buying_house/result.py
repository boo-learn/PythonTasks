class House:
    def __init__(self, area: int, price_per_sm: float):
        self.__area = area
        self.__price = price_per_sm  # цена за кв.метр

    @property
    def area(self):
        return self.__area

    def final_price(self) -> float:
        """
        Возвращает полную цену дома
        """
        ...


class Human:
    def __init__(self, name, start_money=0):
        self.name = name
        self.__money = start_money
        self.__house = None  # Изначально у человека нет дома

    @property
    def money(self):
        return self.__money

    def have_house(self) -> bool:
        """
        :return: True - если есть дом, False - если нет
        """
        return ...

    def info(self) -> str:
        """
        возвращает строку формата: "<имя> | на счету: <сумма> | дом: <есть/нет>"
        """
        ...

    def earn_money(self, income: int) -> None:
        """
        Увеличивает текущее кол-во денег на income
        """
        ...

    def buy_house(self, house: House) -> bool:
        """
        Покупка дома
        Если денег для покупки достаточно:
            в self.__house сохраняем объект покупаемого дома
            тратим деньги на покупку
            возвращаем True
        Если денег недостаточно:
            возвращаем False
        Примечание: Что происходит со старым домом при покупке нового? Он просто исчезает(магия).
        """
        ...
