from datetime import datetime

class Stock:
    def __init__(self, symbol, prices):
        self.symbol = symbol
        self.prices = prices

    def Price(self, date):
        return self.prices.get(date, 0)

class Portfolio:
    def __init__(self):
        self.stocks = []

    def add_stock(self, stock):
        self.stocks.append(stock)

    def Profit(self, start_date, end_date):
        total_profit = 0
        for stock in self.stocks:
            start_price = stock.Price(start_date)
            end_price = stock.Price(end_date)
            total_profit += (end_price - start_price)
        return total_profit

    def AnnualizedReturn(self, start_date, end_date):
        total_profit = self.Profit(start_date, end_date)
        days_difference = (end_date - start_date).days
        years_difference = days_difference / 365.25
        initial_value = sum(stock.Price(start_date) for stock in self.stocks)

        if initial_value == 0 or years_difference == 0:
            return 0

        return ((initial_value + total_profit) / initial_value) ** (1 / years_difference) - 1
