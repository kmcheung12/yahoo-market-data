from urllib.parse import urlencode
from . import util

QUOTE_URL_FMT = "http://download.finance.yahoo.com/d/quotes.csv?%s"
HISTORICAL_URL_FMT = "http://chart.finance.yahoo.com/table.csv?%s"

class Quote:
    # http://wern-ancheta.com/blog/2015/04/05/getting-started-with-the-yahoo-finance-api/
    COLUMNS = {
        "ask": "a",
        "average_daily_volume": "a2",
        "ask_size": "a5",
        "bid": "b",
        "ask_realtime": "b2",
        "bid_realtime": "b3",
        "book_value": "b4",
        "bid_size": "b6",
        "change_and_percentage_change": "c",
        "change": "c1",
        "commission": "c3",
        "change_realtime": "c6",
        "after_hours_change": "c8",
        "dividend_per_share": "d",
        "last_trade_date": "d1",
        "trade_date": "d2",
        "earnings_per_share": "e",
        "eps_estimate_current_year": "e7",
        "eps_estimate_next_year": "e8",
        "eps_estimate_next_quarter": "e9",
        "float_shares": "f6",
        "day_low": "g",
        "holding_gain_percent": "g1",
        "annualized_gain": "g3",
        "holdings_gain": "g4",
        "holdings_gain_percent_realtime": "g5",
        "holdings_gain_realtime": "g6",
        "day_high": "h",
        "more_info": "i",
        "order_book_realtime": "i5",
        "fifty_two_week low": "j",
        "market_capitalization": "j1",
        "shares_outstanding": "j2",
        "market_cap_realtime": "j3",
        "EBITDA": "j4",
        "change_from_fifty_two_week_low": "j5",
        "percent_change_from_fifty_two_week_low": "j6",
        "fifty_two_week_high": "k",
        "last_trade_realtime_with_time": "k1",
        "change_percent": "k2",
        "last_trade_size": "k3",
        "change_from_fifty_two_week_high": "k4",
        "percent_change_from_fifty_two_week_high": "k5",
        "last_trade_with_time": "l",
        "last_trade_price_only": "l1",
        "high_limit": "l2",
        "low_limit": "l3",
        "day_range": "m",
        "day_range_realtime": "m2",
        "fifty_day_moving_average": "m3",
        "two_hundred_day_moving_average": "m4",
        "change_from_200_day_moving_average": "m5",
        "percent_change_from_200_day_moving_average": "m6",
        "change_from_50_day_moving_average": "m7",
        "percent_change_from_50_day_moving_average": "m8",
        "name": "n",
        "notes": "n4",
        "open": "o",
        "previous_close": "p",
        "price_paid": "p1",
        "change_in_percent": "p2",
        "price_per_sales": "p5",
        "price_per_book": "p6",
        "ex-dividend_date": "q",
        "pe_ratio": "r",
        "dividend_pay_date": "r1",
        "pe_ratio_realtime": "r2",
        "peg_ratio": "r5",
        "price_per_eps_estimate_current_year": "r6",
        "price_pereps_estimate_next_year": "r7",
        "symbol": "s",
        "shares_owned": "s1",
        "revenue": "s6",
        "short_ratio": "s7",
        "last_trade_time": "t1",
        "trade_links": "t6",
        "ticker_trend": "t7",
        "one_yr_target_price": "t8",
        "volume": "v",
        "holdings_value": "v1",
        "holdings_value_realtime": "v7",
        "fifty_two_week_range": "w",
        "day_value_change": "w1",
        "day_value_change_realtime": "w4",
        "stock_exchange": "x",
        "dividend_yield": "y"
    }
    def __getattr__(self, name):
        if name in Quote.COLUMNS:
            if name not in self.columns:
                self.columns.append(name)
                self.fmt += Quote.COLUMNS[name]
            return self
        else:
            raise AttributeError(name)
            
    def __init__(self):
        self.symbols = []
        self.columns = []
        self.fmt = ''

    def get_header(self):
        return self.columns

    def get_format(self):
        return self.fmt

    def set_all_format(self):
        for key in Quote.COLUMNS:
            self.__getattr__(key)
        return self

    def reset(self):
        self.symbols = []
        self.columns = []
        self.fmt = ''
        return self

    def set_symbols(self, *symbols):
        if len(symbols) + len(self.symbols) < 1:
            raise ValueError("No symbol specified")
        elif len(symbols) == 1:
            if isinstance(symbols[0], list):
                symbols = symbols[0]
            elif isinstance(symbols[0], str):
                symbols = symbols[0].split(",")
            else:
                raise ValueError("Unknown type", symbols)

        self.symbols.extend(symbols)
        return self

    def quote(self):
        s = ','.join(self.symbols)
        params = urlencode({
            "s": s,
            "f": self.fmt
        })
        url = QUOTE_URL_FMT % (params)
        if len(url) > 8000:
            raise ValueError("Url of length > 8000", len(url))
        content = util.curl(url)
        rows = content.split('\n')
        return rows

    @staticmethod
    def historical_quote(symbol, start, end): #'YYYY-MM-DD'
        params = urlencode({
            's': symbol,
            'a': int(start.split('-')[1]) - 1,
            'b': int(start.split('-')[2]),
            'c': int(start.split('-')[0]),
            'd': int(end.split('-')[1]) - 1,
            'e': int(end.split('-')[2]),
            'f': int(end.split('-')[0]),
            'g': 'd',
            'ignore': '.csv',
            })
        url = HISTORICAL_URL_FMT % params
        content = util.curl(url)
        return content.split('\n')
