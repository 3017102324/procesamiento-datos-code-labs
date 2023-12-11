import pandas as pd
from solucion import (
    ej_1_cargar_iso_codes,
    ej_2_cargar_tipos_de_cambio,
    ej_3_convertir,
)


def test_sol_1():
    expected = [
        "AUD",
        "COP",
        "COU",
        "KMF",
        "CDF",
        "XAF",
        "NZD",
        "CRC",
        "XOF",
        "HRK",
    ]
    actual = ej_1_cargar_iso_codes()[50:60]
    
    assert actual == expected
    
    
def test_sol_2():
    monedas = ej_1_cargar_iso_codes()[50:60]
    ej_2_cargar_tipos_de_cambio(monedas)
    
    expected = pd.DataFrame.from_dict({
        'iso_code': {0: "AUD", 1: "NZD"},
        'tipo_de_cambio': {0: 1.466875, 1: 1.580415}
    })
    actual = pd.read_csv("monedas.csv")
    
    assert (expected.columns == actual.columns).all()
    assert (expected["iso_code"] == actual["iso_code"]).all()
    

def test_sol_3():
    new_amount = ej_3_convertir("AUD", 150, "NZD")
    
    assert isinstance(new_amount, float)
