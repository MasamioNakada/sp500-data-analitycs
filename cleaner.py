import pandas as pd

path = 'data/labels.csv'


def get_sp500(sp500):
    sp500 = sp500[0]
    return sp500['Symbol']


# def clean_export(sp500):
    sp500.replace('.', '-')
    return sp500.to_csv(path)


def clean():
    sp500 = pd.read_html(
        'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')

    sp500 = get_sp500(sp500)
    # clean_export(sp500)
    return pd.read_csv(path)['MMM']
# def sp500_csv(sp500):
#    return sp500.to_csv('./data/S&P500-Symbols.csv')
