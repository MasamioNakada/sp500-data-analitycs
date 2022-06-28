def variaciones(df):
    variaciones = df.Close.pct_change()

    return variaciones

def volatilidad(df):
    variaciones = variaciones(df)
    volatilidad = variaciones.rolling(250).std()*100(250)**0.5
    return volatilidad