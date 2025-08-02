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

    # ==========================================================

    # Datos simulados de sucursales
    datos_sucursales = [
        (1, 'Sucursal Central', 'San José', 'Valle Central'),
        (2, 'Sucursal Cartago', 'Cartago', 'Valle Central'),
        (3, 'Sucursal Liberia', 'Liberia', 'Guanacaste'),
        (4, 'Sucursal Alajuela', 'Alajuela', 'Valle Central'),
        (5, 'Sucursal Limón', 'Limón', 'Caribe'),
        (6, 'Sucursal Pérez', 'San Isidro', 'Zona Sur'),
        (7, 'Sucursal Heredia', 'Heredia', 'Valle Central'),
        (8, 'Sucursal Puntarenas', 'Puntarenas', 'Pacífico'),
        (9, 'Sucursal Nicoya', 'Nicoya', 'Guanacaste'),
        (10, 'Sucursal Escazú', 'Escazú', 'Valle Central')
    ]

    # Inserción de datos
    for id_suc, nombre, ciudad, region in datos_sucursales:
        cursor.execute("""
                       INSERT INTO Sucursales (id_Sucursal, NombreSucursal, Ciudad, Region)
                       VALUES (?, ?, ?, ?)
                       """, id_suc, nombre, ciudad, region)


    # ================================================


    conn.commit()
    print("✅ Certificaciones insertadas correctamente.")

except pyodbc.Error as e:
    print(f"❌ Error de SQL Server: {str(e)}")
except Exception as e:
    print(f"❌ Error general: {str(e)}")

finally:
    if 'conn' in locals():
        conn.close()