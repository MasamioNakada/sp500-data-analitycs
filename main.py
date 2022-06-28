from distutils.command.clean import clean
import pandas as pd


from sp500_variables import sp500_all, sp500_dict
from report_sp500 import visual_report, md_report
from cleaning import cleaning

# instaciamos las etiquetas
labels = cleaning()
# intaciamos el diccionario
sp500_dict = sp500_dict(labels)
# intaciamos sp500 dataframe
sp500_all = sp500_all()

if __name__ == '__main__':

    # reporte del mejor dia para invertir :
    # visual_report(sp500_all)  # --> gráfica
    # md_report(sp500_all)  # --> archivo generado en markdown

    # reporte de las mejores industrias para invertir sp500
    print(sp500_dict['MMM'])
    # reporte de momentos de volatilidad sp500

    # reporte de las 9 mejores industrias
    pass
