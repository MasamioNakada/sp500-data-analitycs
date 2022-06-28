import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from utils import Say, now_date, writter

say = Say()

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

def plot_peaks(df):

    vol = get_volatilidad(df)
    vol = vol.dropna()
    vol.dropna()
    peaks, _ = find_peaks(vol, prominence=3)
    plt.plot(vol)
    plt.plot(vol[peaks], 'o')
    path = f"./out/report_peaks-{now_date()}.png"
    plt.savefig(path)

    return say.cow_says_good(f'Graficos Generados en {path}')

def md_report_volatilidad(df):
    vol = get_volatilidad(df)
    vol = vol.dropna()
    vol.dropna()
    peaks, _ = find_peaks(vol, prominence=3)
    path = f"./out/report_peaks-{now_date()}.md"

    list = ''

    for i in range(vol[peaks].index.strftime('%m-%Y').shape[0]):
        list += '- ' + str(vol[peaks].index[i].strftime('%m-%Y')) + '\n'

    md = f"""![HenryLogo](https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png)
# Reporte de Volatilidad SP-500
## Gráfico:
![Report](report_peaks-{now_date()}.png)
Donde los dias:
{list} """

    return writter(md, path)
