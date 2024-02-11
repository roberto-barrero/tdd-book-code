from money import Money


class Bank:
    def __init__(self):
        self.exchangeRates = {}

    def addExchangeRate(self, fromCurrency, toCurrency, rate):
        key = fromCurrency + '->' + toCurrency
        self.exchangeRates[key] = rate

    def convert(self, money, toCurrency):

        if money.currency == toCurrency:
            return Money(money.amount, toCurrency)

        key = money.currency + '->' + toCurrency
        if key in self.exchangeRates:
            return Money(money.amount * self.exchangeRates[key], toCurrency)
        raise Exception(key)
