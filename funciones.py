import yfinance as yf

import numpy as np

from scipy.signal import find_peaks


from scipy.stats import skew
from scipy.stats import kurtosis


def get_data(name, start='2021-01-01'):
    return yf.download(name, period="max", start=start, rounding=2)


def get_variaciones(df):
    variaciones = df.Close.pct_change()

    return variaciones


def get_volatilidad(df):
    var = get_variaciones(df)
    volatilidad = var.rolling(250).std()*100*(250)**0.5

    return volatilidad


def find_peak(df):
    vol = get_volatilidad(df)
    peaks, _ = find_peaks(vol, prominence=3)
    return peaks, vol


def retornos_gap(df):
    return np.log(df.Open/df.Close.shift(1)).fillna(0)


def retornos_intra(df):
    return np.log(df['Close']/df.Open).fillna(0)


def get_return(df):
    return df['Adj Close'].pct_change()


def get_retorno_medio_daily(df):
    daily = np.mean(get_return(df))
    return daily


def get_retorno_medio_year(df):
    daily = np.mean(get_return(df))
    year = ((1 + daily)**252)-1
    return year


def get_skewness(df):
    skenew = skew(get_return(df).dropna())
    return skenew


def get_curtosis(df):
    excess = kurtosis(get_return(df))
    real = excess + 3
    return excess, real


def year_volatilidad(df):
    daily_std = np.std(df['Adj Close'].pct_change().dropna())
    annual_std = daily_std*np.sqrt(252)
    return annual_std
