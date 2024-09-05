from datetime import datetime

class Stock:
    def __init__(self, symbol, prices):
        """
        Initialize Stock with a symbol and a dictionary of prices by date.
        :param symbol: The stock's symbol (e.g., 'AAPL')
        :param prices: A dictionary with dates as keys and prices as values.
        """
        self.symbol = symbol
        self.prices = prices  # prices should be a dictionary with date keys
    
    def Price(self, date):
        """
        Return the stock price on the given date.
        :param date: A datetime object.
        :return: Stock price on the given date.
        """
        return self.prices.get(date, 0)

class Portfolio:
    def __init__(self):
        """
        Initialize a Portfolio with an empty list of stocks.
        """
        self.stocks = []
    
    def add_stock(self, stock):
        """
        Add a Stock to the portfolio.
        :param stock: A Stock object.
        """
        self.stocks.append(stock)
    
    def Profit(self, start_date, end_date):
        """
        Calculate the portfolio's total profit between two dates.
        :param start_date: A datetime object representing the start date.
        :param end_date: A datetime object representing the end date.
        :return: Total profit (sum of individual stock profits).
        """
        total_profit = 0
        for stock in self.stocks:
            start_price = stock.Price(start_date)
            end_price = stock.Price(end_date)
            total_profit += (end_price - start_price)
        return total_profit

    def AnnualizedReturn(self, start_date, end_date):
        """
        Calculate the annualized return of the portfolio between two dates.
        :param start_date: A datetime object representing the start date.
        :param end_date: A datetime object representing the end date.
        :return: Annualized return of the portfolio.
        """
        total_profit = self.Profit(start_date, end_date)
        
        # Calculate the number of years between the two dates
        days_difference = (end_date - start_date).days
        years_difference = days_difference / 365.25
        
        # Assuming the portfolio's initial value is based on stock prices at start_date
        initial_value = sum(stock.Price(start_date) for stock in self.stocks)
        
        if initial_value == 0 or years_difference == 0:
            return 0  # Avoid division by zero

        # Calculate annualized return
        return ((initial_value + total_profit) / initial_value) ** (1 / years_difference) - 1

# Example usage:
prices_aapl = {
    datetime(2023, 1, 1): 150,
    datetime(2024, 1, 1): 170
}
prices_msft = {
    datetime(2023, 1, 1): 250,
    datetime(2024, 1, 1): 280
}

aapl = Stock('AAPL', prices_aapl)
msft = Stock('MSFT', prices_msft)

portfolio = Portfolio()
portfolio.add_stock(aapl)
portfolio.add_stock(msft)

start_date = datetime(2023, 1, 1)
end_date = datetime(2024, 1, 1)

# Profit between two dates
print("Total Profit:", portfolio.Profit(start_date, end_date))

# Annualized return
print("Annualized Return:", portfolio.AnnualizedReturn(start_date, end_date))
