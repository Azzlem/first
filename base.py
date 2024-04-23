import pandas as pd


def read_csv_my1():
    gl = pd.read_csv('USD_RUB .csv')
    gl.head()
    df_new = gl.iloc[:, [0, 1]]
    df_new = [float(i[1].replace(",", ".")) for i in df_new.values]

    return df_new


def read_csv_my2():
    gl = pd.read_csv('USD_RUB .csv')
    gl.head()
    df_new = gl.iloc[:, [0, 1]]
    df_new = [float(i[1].replace(",", ".")) for i in df_new.values]
    return df_new


def read_csv_my3():
    gl = pd.read_csv('USD_RUB .csv')
    gl.head()
    df_new = gl.iloc[:, [0, 1]]
    df_new = [float(i[1].replace(",", ".")) for i in df_new.values]
    return df_new


def read_csv_my4():
    gl = pd.read_csv('USD_RUB .csv')
    gl.head()
    df_new = gl.iloc[:, [0, 1]]
    df_new = [float(i[1].replace(",", ".")) for i in df_new.values]
    return df_new
