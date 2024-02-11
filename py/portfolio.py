import functools
import operator
from money import Money


class Portfolio:
    def __init__(self):
        self.moneys = []
        self._eur_to_usd = 1.2

    def add(self, *moneys):
        self.moneys.extend(moneys)

    def evaluate(self, currency):
        total = functools.reduce(
            operator.add, map(lambda money: self.__convert(money, currency), self.moneys), 0)
        return Money(total, currency)

    def __convert(self, money, currency):
        if money.currency == currency:
            return money.amount
        else:
            return money.amount * self._eur_to_usd
