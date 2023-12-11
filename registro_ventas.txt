import pandas as pd

def ej_1_leer_archivo(direccion_archivo: str) -> list[str]:
# Abrir el archivo y leer las líneas sin aplicar strip
    with open("registro_ventas.txt", "r", encoding= "utf-8") as file:
        lineas = file.readlines()
        return lineas


def ej_2_lista_diccionarios(lineas: list[str]) -> list[dict[str, str]]:
    registros = []
# Definir un diccionario temporal para almacenar los datos de cada registro
    registro = {}
# Procesar las líneas y producir una lista de diccionarios
    for linea in lineas:
        if ':' in linea:  # Verificar si la línea no está en blanco
            clave, Valor = linea.split(":",1)
            clave = clave.strip()
            Valor = Valor.strip()
            if not Valor:
                Valor = None
            registro[clave] = Valor
        elif registro:
            registros.append(registro)
            registro = {}
    # Agregar el último registro
    if registro:
            registros.append(registro)
            return registros



def ej_3_convertir_a_dataframe(datos: list[dict[str, str]]) -> pd.DataFrame:
        df = pd.DataFrame(datos)
        return df


def ej_4_limpieza(df: pd.DataFrame) -> None:
        # Convertir Cantidad y Precio a números utilizando 'astype'
    df["Cantidad"] = pd.to_numeric(df["Cantidad"], errors="coerce")
    df["Precio"] = pd.to_numeric(df["Precio"], errors="coerce")

    # Reemplazar los valores faltantes en Cantidad y Precio por la media de la columna
    df["Cantidad"].fillna(df["Cantidad"].mean(), inplace=True)
    df["Precio"].fillna(df["Precio"].mean(), inplace=True)

    # Eliminar outliers en Cantidad y Precio usando el rango intercuartil
    Q1 = df["Cantidad"].quantile(0.25)
    Q3 = df["Cantidad"].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound= Q1 - 1.5 * IQR
    higher_bound = Q3 + 1.5 * IQR

    Q1 = df["Precio"].quantile(0.25)
    Q3 = df["Precio"].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound= Q1 - 1.5 * IQR
    higher_bound = Q3 + 1.5 * IQR

    df_cleaned = df[(df['Cantidad']>= lower_bound) & (df['Cantidad']<=higher_bound)]
    df_cleaned = df[(df['Precio']>= lower_bound) & (df['Precio']<=higher_bound)]
    # Guardar el DataFrame limpio en un nuevo archivo "registros_ventas_limpios.csv"

    return df_cleaned

lineas = ej_1_leer_archivo("registro_ventas.txt")
datos = ej_2_lista_diccionarios(lineas)
df = ej_3_convertir_a_dataframe(datos)

    #aplicar las tecnicas de limpieza
df =   ej_4_limpieza(df)

# Guardar el DataFrame limpio en un nuevo archivo "registros_ventas_limpios.csv"
df.to_csv("registros_ventas_limpios.csv", index=False)