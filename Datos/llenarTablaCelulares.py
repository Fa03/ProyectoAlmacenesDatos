import pyodbc
import urllib
import pandas as pd
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, text

# Leer el archivo Excel
df = pd.read_excel('C:/Users/Lenovo/OneDrive/CUC/AlmacenesDeDatos/Proyecto/Celulares.xlsx')

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

    # Insertar fila por fila
    for _, row in df.iterrows():
        cursor.execute("""
                       INSERT INTO Celulares (id_Celular, id_Modelo, id_Especificaciones, id_Color,
                                                     id_Categoria, id_Proveedor, id_Certificacion, id_Garantia)
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                       """, int(row['id_Celular']), int(row['id_Modelo']), int(row['id_Especificaciones']), int(row['id_Color']),
                       int(row['id_Categoria']), int(row['id_Proveedor']), int(row['id_Certificacion']), int(row['id_Garantia']))


    # ================================================


    conn.commit()
    print("✅ Datos Celular insertadas correctamente.")

except pyodbc.Error as e:
    print(f"❌ Error de SQL Server: {str(e)}")
except Exception as e:
    print(f"❌ Error general: {str(e)}")

finally:
    if 'conn' in locals():
        conn.close()