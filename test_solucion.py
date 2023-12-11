import pandas as pd
from solucion import (
    ej_1_leer_archivo,
    ej_2_lista_diccionarios,
    ej_3_convertir_a_dataframe,
    ej_4_limpieza,
)


def test_sol_1():
    lineas = ej_1_leer_archivo("registro_ventas.txt")
    
    assert lineas[:12] == [
        "Fecha: 01/05/2023\n",
        "Hora: 09:15\n",
        "Producto: Camiseta\n",
        "Cantidad: 2\n",
        "Precio: 25.0\n",
        "\n",
        "Fecha: 02/05/2023\n",
        "Hora: 10:30\n",
        "Producto: Pantalón\n",
        "Cantidad: 5\n",
        "Precio: 35.0\n",
        "\n",
    ]


def test_sol_2():
    lineas = ej_1_leer_archivo("registro_ventas.txt")
    actual = ej_2_lista_diccionarios(lineas)

    expected = [
        {'Fecha': '01/05/2023', 'Hora': '09:15', 'Producto': 'Camiseta', 'Cantidad': '2', 'Precio': '25.0'},
        {'Fecha': '02/05/2023', 'Hora': '10:30', 'Producto': 'Pantalón', 'Cantidad': '5', 'Precio': '35.0'},
        {'Fecha': '03/05/2023', 'Hora': '12:45', 'Producto': 'Zapatos', 'Cantidad': None, 'Precio': '50.0'},
        {'Fecha': '04/05/2023', 'Hora': '14:00', 'Producto': 'Gorra', 'Cantidad': '3', 'Precio': '1800.0'},
        {'Fecha': '05/05/2023', 'Hora': '16:30', 'Producto': 'Calcetines', 'Cantidad': '4', 'Precio': '10.0'},
    ]
    
    assert actual == expected
    
    
def test_sol_3():
    lineas = ej_1_leer_archivo("registro_ventas.txt")
    datos = ej_2_lista_diccionarios(lineas)
    actual = ej_3_convertir_a_dataframe(datos)

    expected = pd.DataFrame.from_dict({
        'Fecha': {0: '01/05/2023', 1: '02/05/2023', 2: '03/05/2023', 3: '04/05/2023', 4: '05/05/2023'},
        'Hora': {0: '09:15', 1: '10:30', 2: '12:45', 3: '14:00', 4: '16:30'},
        'Producto': {0: 'Camiseta', 1: 'Pantalón', 2: 'Zapatos', 3: 'Gorra', 4: 'Calcetines'},
        'Cantidad': {0: '2', 1: '5', 2: None, 3: '3', 4: '4'},
        'Precio': {0: '25.0', 1: '35.0', 2: '50.0', 3: '1800.0', 4: '10.0'}
    })
    
    assert (actual.values == expected.values).all()


def test_sol_4():
    lineas = ej_1_leer_archivo("registro_ventas.txt")
    datos = ej_2_lista_diccionarios(lineas)
    df = ej_3_convertir_a_dataframe(datos)
    
    ej_4_limpieza(df)
    
    actual = pd.read_csv("registros_ventas_limpios.csv").values
    
    expected = pd.DataFrame.from_dict({
        'Fecha': {0: '01/05/2023', 1: '02/05/2023', 2: '03/05/2023', 3: '05/05/2023'},
        'Hora': {0: '09:15', 1: '10:30', 2: '12:45', 3: '16:30'},
        'Producto': {0: 'Camiseta', 1: 'Pantalón', 2: 'Zapatos', 3: 'Calcetines'},
        'Cantidad': {0: 2.0, 1: 5.0, 2: 3.5, 3: 4.0},
        'Precio': {0: 25.0, 1: 35.0, 2: 50.0, 3: 10.0},
    }).values
    
    assert (actual == expected).all()
