import pandas as pd
import yfinance as yf
from datetime import datetime
import os


def now_date():
    now = datetime.now()
    current_time = now.strftime("%d_%m_%Y")
    return current_time


def writter(text):
    path = f"out/reporte-{now_date()}.md"
    open(path, mode='a').close()
    fd = os.open(path, os.O_RDWR)
    line = str.encode(text)
    os.write(fd, line)
    os.close(fd)
    return Say().cow_says_good("reporte escrito exitosamente en ./out")


def enterprise_info(name):
    """Funcion que permite averiguar la informacion de la empresa"""

# -----------------------------------------------


class Say:

    # -----------------------------------------------
    def cow_says_good(self, str):
        """
        Aquí va un string , y la vaquita lo dirá :v
        """
        lenght = len(str)
        print(" _" + lenght * "_" + "_ ")
        print("< " + str + " > ")
        print(" -" + lenght * "-" + "- ")
        print("        \   ^__^ ")
        print("         \  (oo)\_______ ")
        print("            (__)\  good )\/\ ")
        print("                ||----w | ")
        print("                ||     || ")

    def cow_says_error(self, str):
        lenght = len(str)
        print(" _" + lenght * "_" + "_ ")
        print("< " + str + " > ")
        print(" -" + lenght * "-" + "- ")
        print("        \   ^__^ ")
        print("         \  (oo)\_______ ")
        print("            (__)\  error )\/\ ")
        print("                ||----w | ")
        print("                ||     || ")
