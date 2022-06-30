import pandas as pd
from time import sleep

from sp500_variables import sp500_all, sp500_dict
from report_sp500 import md_report_best_day, visual_report
from cleaner import clean
from volatilidad import plot_peaks, md_report_volatilidad
from report_best_enterprise import md_report_best_companies

# instaciamos las etiquetas
labels = clean()
# intaciamos el diccionario
sp500_dict = sp500_dict(labels)
# intaciamos sp500 dataframe
sp500 = sp500_all()

if __name__ == '__main__':
    tittle = '''      ___________________           ._______________   _______   
     /   _____/\______   \          |   ____/\   _  \  \   _  \  
     \_____  \  |     ___/  ______  |____  \ /  /_\  \ /  /_\  \ 
     /        \ |    |     /_____/  /       \\  \_/   \\  \_/   \
    /_______  / |____|             /______  / \_____  / \_____  /
            \/                            \/        \/        \/ 
        _____                   .__                  .__         
       /  _  \    ____  _____   |  |  ___.__.  ______|__|  ______
      /  /_\  \  /    \ \__  \  |  | <   |  | /  ___/|  | /  ___/
     /    |    \|   |  \ / __ \_|  |__\___  | \___ \ |  | \___ \ 
     \____|__  /|___|  /(____  /|____// ____|/____  >|__|/____  >
             \/      \/      \/       \/          \/          \/ '''
    print(tittle)

    # reporte del mejor dia para invertir :
    visual_report(sp500)  # --> gráfica

    md_report_best_day(sp500)  # --> reporte generado en markdown

    # reporte de momentos de volatilidad sp500
    plot_peaks(sp500)  # --> gráfica de volatilidad

    md_report_volatilidad(sp500)  # --> reporte generado en markdown

    # reporte de las mejores industrias para invertir sp500

    md_report_best_companies(sp500_dict)

    # reporte de momentos de volatilidad sp500

    # reporte de las 9 mejores industrias
