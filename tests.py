import unittest
from datetime import datetime
from portfolio import Stock, Portfolio

class TestStockPortfolio(unittest.TestCase):
    def setUp(self):
        prices_aapl = {
            datetime(2023, 1, 1): 150,
            datetime(2024, 1, 1): 170
        }
        prices_msft = {
            datetime(2023, 1, 1): 250,
            datetime(2024, 1, 1): 280
        }

        self.aapl = Stock('AAPL', prices_aapl)
        self.msft = Stock('MSFT', prices_msft)
        
        self.portfolio = Portfolio()
        self.portfolio.add_stock(self.aapl)
        self.portfolio.add_stock(self.msft)

    def test_stock_price(self):
        self.assertEqual(self.aapl.Price(datetime(2023, 1, 1)), 150)
        self.assertEqual(self.msft.Price(datetime(2023, 1, 1)), 250)
    
    def test_portfolio_profit(self):
        start_date = datetime(2023, 1, 1)
        end_date = datetime(2024, 1, 1)
        expected_profit = (170 - 150) + (280 - 250)
        self.assertEqual(self.portfolio.Profit(start_date, end_date), expected_profit)

    def test_annualized_return(self):
        start_date = datetime(2023, 1, 1)
        end_date = datetime(2024, 1, 1)
        expected_annualized_return = 0.12509076113705664
        self.assertAlmostEqual(self.portfolio.AnnualizedReturn(start_date, end_date), expected_annualized_return, places=6)

if __name__ == '__main__':
    unittest.main()
