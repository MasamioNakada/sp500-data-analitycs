import pandas as pd
import yfinance as yf
from cleaning import cleaning


def sp500_dict(labels):
    data_dict = {}
    for label in labels[:10]:
        data_dict[label] = yf.download(
            f'{label}', period="max", start='2000-01-01', rounding=2)

    return data_dict


def sp500_all():
    sp500 = yf.Ticker("^GSPC")
    hist = sp500.history(period="max", start='2000-01-01', rounding=2)
    return hist


#labels = sp500_symbols()
#data_dict = s500_dict(labels)
