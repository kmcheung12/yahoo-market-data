# yahoo-market-data
A python library to retrieve quotes from yahoo finance.

## Installation (Python 3.x only)
pip: `pip install yahoo-market-data`

Source: `git clone git@github.com:kmcheung12/yahoo-market-data.git`

## Usage
### Get stocks symbols by market:
```python
>>> from yahoo_market_data import Symbols
>>> Symbols.nyse()
['DDD',
 'MMM',
 'WBAI',
 ...]
 >>> Symbols.hkex()
 ['0001.HK',
 '0002.HK',
 '0003.HK',
 ...]
```
Currently support markets are `nyse`, `nasdaq`, `amex`, `hkex` and `hkgem`

### Get realtime stocks data from Yahoo finance
```python
>>> from yahoo_market_data import Quote
>>>
>>> # support multiple symbols at one go
>>> # see below for all available fields
>>> q = Quote()\
        .set_symbols("DDD", "MMM")\
        .change\
        .last_trade_price_only\
        .name
>>> q.quote()
['-0.20,16.63,"3D Systems Corporation Common S"',
'+1.15,187.19,"3M Company Common Stock"']
```
### Get historical stocks data from Yahoo finance

```python
>>> Quote.historical_quote('AAPL', '2016-01-01', '2016-01-07')
['Date,Open,High,Low,Close,Volume,Adj Close',
 '2016-01-07,98.68,100.129997,96.43,96.449997,81094400,93.943473',
 '2016-01-06,100.559998,102.370003,99.870003,100.699997,68457400,98.083025',
 '2016-01-05,105.75,105.849998,102.410004,102.709999,55791000,100.040792',
 '2016-01-04,102.610001,105.370003,102.00,105.349998,67649400,102.612183']
```

### Available attributes for real time quotes
```
.ask
.average_daily_volume
.ask_size
.bid
.ask_realtime
.bid_realtime
.book_value
.bid_size
.change_and_percentage_change
.change
.commission
.change_realtime
.after_hours_change
.dividend_per_share
.last_trade_date
.trade_date
.earnings_per_share
.eps_estimate_current_year
.eps_estimate_next_year
.eps_estimate_next_quarter
.float_shares
.day_low
.holding_gain_percent
.annualized_gain
.holdings_gain
.holdings_gain_percent_realtime
.holdings_gain_realtime
.day_high
.more_info
.order_book_realtime
.fifty_two_week low
.market_capitalization
.shares_outstanding
.market_cap_realtime
.EBITDA
.change_from_fifty_two_week_low
.percent_change_from_fifty_two_week_low
.fifty_two_week_high
.last_trade_realtime_with_time
.change_percent
.last_trade_size
.change_from_fifty_two_week_high
.percent_change_from_fifty_two_week_high
.last_trade_with_time
.last_trade_price_only
.high_limit
.low_limit
.day_range
.day_range_realtime
.fifty_day_moving_average
.two_hundred_day_moving_average
.change_from_200_day_moving_average
.percent_change_from_200_day_moving_average
.change_from_50_day_moving_average
.percent_change_from_50_day_moving_average
.name
.notes
.open
.previous_close
.price_paid
.change_in_percent
.price_per_sales
.price_per_book
.ex-dividend_date
.pe_ratio
.dividend_pay_date
.pe_ratio_realtime
.peg_ratio
.price_per_eps_estimate_current_year
.price_pereps_estimate_next_year
.symbol
.shares_owned
.revenue
.short_ratio
.last_trade_time
.trade_links
.ticker_trend
.one_yr_target_price
.volume
.holdings_value
.holdings_value_realtime
.fifty_two_week_range
.day_value_change
.day_value_change_realtime
.stock_exchange
.dividend_yield

```
