import pyodbc
import urllib
import pandas as pd
import numpy as np
import random
import pyodbc
from datetime import datetime, timedelta


# # Leer el archivo Excel
# df = pd.read_excel('C:/Users/Lenovo/OneDrive/CUC/AlmacenesDeDatos/Proyecto/Celulares.xlsx')

# Configuración de conexión
driver = 'ODBC Driver 17 for SQL Server'
server = 'FA-NEW'
database = 'BD_Celulares'
username = 'TEST4'
password = 'ContrasenaSegura123!'

params = urllib.parse.quote_plus(
    f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'
)

try:
    # Single connection attempt with proper error handling
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        f'SERVER={server};'
        f'DATABASE={database};'
        'Trusted_Connection=yes;'
    )
    cursor = conn.cursor()

    # ==========================================================
    # 📌 Parámetros
    NUM_ROWS = 500000
    YEARS = 5
    FECHAS_POR_AÑO = NUM_ROWS // YEARS
    ID_CELULARES = list(range(1, 34))
    ID_SUCURSALES = list(range(1, 11))
    CANTIDADES = list(range(1, 6))


    # 🧮 Generar fechas aleatorias por año
    def generar_fechas_aleatorias():
        fechas = []
        for year in range(datetime.now().year - YEARS, datetime.now().year):
            start_date = datetime(year, 1, 1)
            for _ in range(FECHAS_POR_AÑO):
                delta = timedelta(days=random.randint(0, 364))
                fechas.append(start_date + delta)
        random.shuffle(fechas)
        return fechas


    # 🏷️ Obtener precios por id_Celular
    def obtener_precios_unitarios():
        cursor.execute("SELECT id_Celular, PrecioRegional FROM PreciosxRegion")
        precios = {row.id_Celular: row.PrecioRegional for row in cursor.fetchall()}
        return precios


    precios_dict = obtener_precios_unitarios()


    # 🧱 Generar DataFrame
    def generar_dataframe():
        df = pd.DataFrame({
            'id_Venta': range(1, NUM_ROWS + 1),
            'id_Celular': np.random.choice(ID_CELULARES, NUM_ROWS),
            'id_Sucursal': np.random.choice(ID_SUCURSALES, NUM_ROWS),
            'FechaVenta': generar_fechas_aleatorias(),
            'Cantidad': np.random.choice(CANTIDADES, NUM_ROWS)
        })
        df['PrecioRegional'] = df['id_Celular'].map(precios_dict)
        return df


    df_ventas = generar_dataframe()


    # 🚚 Insertar por lotes
    def insertar_por_lotes(df, batch_size=10000):
        insert_query = """
                       INSERT INTO Ventas (id_Venta, id_Celular, id_Sucursal, FechaVenta, Cantidad, PrecioVentaUnitario)
                       VALUES (?, ?, ?, ?, ?, ?) \
                       """
        for start in range(0, len(df), batch_size):
            batch = df.iloc[start:start + batch_size]
            data = [
                (
                    int(row.id_Venta),
                    int(row.id_Celular),
                    int(row.id_Sucursal),
                    row.FechaVenta,
                    int(row.Cantidad),
                    float(row.PrecioRegional)
                )
                for row in batch.itertuples(index=False)
            ]
            cursor.executemany(insert_query, data)
            conn.commit()
            print(f"✅ Insertadas {start + len(batch)} filas...")


    insertar_por_lotes(df_ventas)

    # ================================================


    conn.commit()
    print("✅ Datos PreciosxRegion insertadas correctamente.")

except pyodbc.Error as e:
    print(f"❌ Error de SQL Server: {str(e)}")
except Exception as e:
    print(f"❌ Error general: {str(e)}")

finally:
    if 'conn' in locals():
        conn.close()