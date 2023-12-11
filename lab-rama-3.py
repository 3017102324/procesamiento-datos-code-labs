import pandas as pd
import requests


def ej_1_cargar_iso_codes() -> list[str]:
    df = pd.read_csv('currency_codes.csv')

# Extraer los códigos ISO como una lista
    iso_code = df['AlphabeticCode'].tolist()
    return iso_code


def ej_2_cargar_tipos_de_cambio(monedas: list[str]) -> None:
    lista_datos = []

    for moneda in range(len(monedas)):
        par= f'USD_{monedas[moneda]}'
        base_url= f'https://api.api-ninjas.com/v1/exchangerate?pair={par}'
        response =requests.get(base_url, headers={'X-Api-Key':'WXEkTv0bbJxgzKzNi3XG6g==vugbby2U0GWUHi5L'})
        if response.status_code ==requests.codes.ok:
            lista_datos.append([monedas[moneda],response.json()["exchange_rate"]])

        df_divisas = pd.DataFrame(lista_datos, columns=['iso_code','tipo_de_cambio'])
        df_divisas.to_csv("./monedas.csv", index=False)

def ej_3_convertir(moneda_origen: str, monto: float, moneda_destino: str) -> float:
        cambio = pd.read_csv('./monedas.csv')

        df_tasa_origen = cambio[cambio["iso_code"] == moneda_origen]
        df_tasa_origen = df_tasa_origen.reset_index(drop=True)
        tasa_value_origen = df_tasa_origen.at[0, 'tipo_de_cambio']
        origen_a_USD = monto/tasa_value_origen

        df_tasa_destino = cambio[cambio["iso_code"] == moneda_destino]
        df_tasa_destino = df_tasa_destino.reset_index(drop=True)
        tasa_value_destino = df_tasa_destino.at[0, 'tipo_de_cambio']
        USD_a_destino = origen_a_USD * tasa_value_destino

        return USD_a_destino