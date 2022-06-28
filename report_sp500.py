import numpy
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf


from utils import Say, now_date, writter

say = Say()


def retornos_gap(df):
    """Retorna una Serie del el retorno de los movimiento gap agrupados por día de la semana """
    serie = np.log(df.Open/df.Close.shift(1)).fillna(0)

    return serie.groupby(serie.index.day_name()).mean()


def retornos_intra(df):
    """Retorna una Serie del el movimientos intradiarios  agrupados por dia de la semana"""
    serie = np.log(df.Open/df.Close).fillna(0)

    return serie.groupby(serie.index.day_name()).mean()


def best_value(df):
    sr1 = retornos_gap(df)
    sr2 = retornos_intra(df)

    max1 = sr1.max()
    max2 = sr2.max()

    return (sr1[sr1 == max1].index.values, sr2[sr2 == max2].index.values)


def visual_report(df):
    """Retorno de Graficos"""
    fig, axes = plt.subplots(2, 1)
    axes[0].plot(retornos_gap(df))
    axes[0].set_title('Movimiento Gap Agrupados por día de la semana')
    axes[1].plot(retornos_intra(df))
    axes[1].set_title(
        'Movimientos intradiarios Agrupados por día de la semana')
    path = f"./out/report-{now_date()}.png"
    plt.tight_layout()
    plt.savefig(path)
    plt.close(fig)
    return say.cow_says_good('Graficos Generados en ./out')


def md_report(df):

    md = f"""![HenryLogo](https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png)
# Reporte Mejor día par invertir:
## Resumen
![Report](report-{now_date()}.png)

Donde *{best_value(df)[0].item()}* el mejor día para invertir teniendo en cuenta el retorno de los movimiento gap

Y *{best_value(df)[1].item()}* el mejor día para invertir teniendo en cuenta el retorno de los movimientos intradiarios"""

    return writter(md)
