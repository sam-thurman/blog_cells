import yfinance as yf
import pandas as pd

def get_master_stock_data(stocks=None):
    if stocks:
        cos = stocks
    else:
        cos = ['GOOG', 'AAPL', 'AMZN', 'FB', 'NFLX', 'MSFT', 'SPOT', 'TSLA']

    closes = []

    for co in cos:
        series = yf.Ticker(co).history(period='1y').rename({'Close':co}, axis=1)[co]
        closes.append(series)

    master = pd.concat(closes, axis=1)
    return master

def get_stock_data(tickerSymbol='MSFT', period='1d'):
    '''
    Returns up-to-date trend data for the provided stock 
    over the past provided time period.

    Valid time periods: 1d, 5d, 1mo, 3mo, 6mo, ytd, 1y, 2y, 5y, 10y, max
    '''
    if period in ['1d','5d']:
        interval = '1m'
    elif period=='1mo':
        interval = '5m'
    elif period in ['3mo','6mo','1y','2y']:
        interval = '1h'
    elif period in ['5y','10y','max']:
        interval = '1d'
    else:
        interval = '1d'

    tickerData = yf.Ticker(tickerSymbol)

    tickerDf = tickerData.history(period=period, interval=interval)

    return tickerDf

def get_stock_data_for_period(tickerSymbol='MSFT', start_date='2010-1-1', end_date='2020-1-25'):
    '''
    Returns trend data for the provided stock 
    over the provided period of time.

    start and end dates are in format 4_DIGIT_YR-MONTH-DAY
    ex: 2020-1-1, 2020-1-25
    '''
    # use yfinance to get data on this ticker
    tickerData = yf.Ticker(tickerSymbol)

    # get the historical prices for this ticker
    tickerDf = tickerData.history(start=start_date, end=end_date, interval='1m')

    # return data
    return tickerDf
