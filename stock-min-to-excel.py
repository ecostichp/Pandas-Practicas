import pandas as pd

almacenes = [1, 2]


def df_limpio():
    df = pd.read_excel("data.xlsx", 'data')
    df["Clave de artículo "] = df["Clave de artículo "].astype(object)
    df["Fecha "] = pd.to_datetime(df["Fecha "], dayfirst=True)
    df["Cantidad "] = pd.to_numeric(df["Cantidad "].str.replace(',', ''))
    return df


def stock_min_to_excel(almacenes):

    df = df_limpio()

    writer = pd.ExcelWriter("stock-mínimo.xlsx", engine="openpyxl")

    for almacen in almacenes:

        dfA = df[df["Almacén "] == almacen][["Fecha ", "Cantidad "]]

        dfprov = dfA.groupby("Fecha ").sum()
        dfprov["Cantidad "] = dfprov[dfprov["Cantidad "] < 0] * -1
        dfprov["Dias "] = 1
        dfprov["Probabilidad "] = 1 / dfprov["Cantidad "].count()

        tabla = dfprov.groupby("Cantidad ").agg(
            {"Dias ": 'count', "Probabilidad ": 'sum'})
        tabla["Si-dias "] = tabla["Dias "].cumsum()
        tabla["No-dias "] = tabla["Dias "].sum() - tabla["Si-dias "]
        tabla["Si-% "] = tabla["Si-dias "] / tabla["Dias "].sum()
        tabla["No-% "] = tabla["No-dias "] / tabla["Dias "].sum()

        tabla.to_excel(writer, sheet_name=f"A{almacen}")

    writer.close()
    writer.handles = None


if __name__ == "__main__":
    stock_min_to_excel(almacenes)
