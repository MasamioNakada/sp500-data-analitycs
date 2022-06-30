import pandas as pd
import numpy as np
from funciones import get_retorno_medio_year

from utils import now_date, writter, Say

say = Say()


def sorter(data, bool):
    sort = {}
    sort_keys = sorted(data, key=data.get, reverse=bool)

    for w in sort_keys:
        sort[w] = data[w]
    return sort


def iter_get_return_mean(data):
    for key in data.keys():
        data[key] = get_retorno_medio_year(data[key])

    sorted_return = pd.Series(sorter(data, True))
    sorted_return[:40].to_csv(f'out/best_companies-{now_date()}.csv')
    return sorted_return[:40]


def iterator(series):
    list = ''
    for i in range(series.size):
        list += f'{i+1}. ' + \
            str(series.index[i]) + ': ' + str(round(series[i], 3)) + '\n'
    return list


def md_report_best_companies(data):
    path = f'out/best_companies-{now_date()}.md'

    return_series = iter_get_return_mean(data)

    list_return = iterator(return_series)

    md = f"""![HenryLogo](https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png)
# Reporte de Mejores Compañias del SP-500 ({now_date()})
# 50 mejores empresas respecto al retorno medio anual:
Se Muestra a continuación el posible retorno que daría dichas empresas
{list_return}
"""

    return writter(md, path)
