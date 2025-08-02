import pyodbc
import urllib
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, text


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

    # Datos simulados
    datos_garantias = [
        (1, 12, 'Fabricante'),
        (2, 24, 'Extendida'),
        (3, 6, 'Reacondicionado'),
        (4, 18, 'Premium'),
        (5, 12, 'Tienda'),
        (6, 36, 'Corporativa'),
        (7, 3, 'Promocional'),
        (8, 24, 'Fabricante'),
        (9, 12, 'Reemplazo'),
        (10, 6, 'Básica')
    ]

    # Inserción de datos
    for id_garantia, duracion, tipo in datos_garantias:
        cursor.execute("""
                       INSERT INTO Garantias (id_Garantia, DuracionMeses, Tipo)
                       VALUES (?, ?, ?)
                       """, id_garantia, duracion, tipo)


    conn.commit()
    print("✅ Certificaciones insertadas correctamente.")

except pyodbc.Error as e:
    print(f"❌ Error de SQL Server: {str(e)}")
except Exception as e:
    print(f"❌ Error general: {str(e)}")

finally:
    if 'conn' in locals():
        conn.close()