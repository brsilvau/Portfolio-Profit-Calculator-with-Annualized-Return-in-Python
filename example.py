from datetime import datetime
from portfolio import Stock, Portfolio

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

print("Total Profit:", portfolio.Profit(start_date, end_date))
print("Annualized Return:", portfolio.AnnualizedReturn(start_date, end_date))
