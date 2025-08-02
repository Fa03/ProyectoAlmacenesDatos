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

    # Datos simulados
    datos_especificaciones = [
        (1, 180, 4, 64, 8, 12, 'Snapdragon 680', 5000, 6.5),
        (2, 195, 6, 128, 16, 48, 'MediaTek Helio G95', 6000, 6.7),
        (3, 165, 8, 256, 32, 64, 'Snapdragon 888', 4500, 6.1),
        (4, 210, 12, 512, 40, 108, 'Exynos 2200', 5000, 6.8),
        (5, 175, 3, 32, 5, 8, 'Unisoc SC9863A', 4000, 6.0),
        (6, 185, 6, 128, 12, 50, 'Snapdragon 695', 4700, 6.6),
        (7, 190, 8, 128, 20, 64, 'Dimensity 920', 5000, 6.4),
        (8, 200, 4, 64, 13, 16, 'Snapdragon 662', 6000, 6.5),
        (9, 170, 6, 256, 24, 48, 'Snapdragon 7 Gen 1', 4800, 6.3),
        (10, 160, 2, 16, 2, 5, 'MediaTek MT6739', 3000, 5.5),
        (11, 185, 8, 128, 32, 64, 'Snapdragon 870', 4500, 6.7),
        (12, 195, 12, 256, 40, 108, 'Dimensity 1200', 5000, 6.9),
        (13, 175, 6, 64, 8, 13, 'Kirin 710F', 4000, 6.2),
        (14, 205, 4, 128, 10, 25, 'Snapdragon 480', 5000, 6.5),
        (15, 180, 3, 32, 5, 8, 'MediaTek A22', 3500, 5.8),
        (16, 190, 6, 128, 16, 48, 'Exynos 850', 6000, 6.6),
        (17, 165, 8, 256, 32, 64, 'Snapdragon 778G', 4700, 6.4),
        (18, 210, 12, 512, 50, 200, 'Snapdragon 8 Gen 2', 5000, 6.8),
        (19, 170, 4, 64, 8, 12, 'MediaTek G37', 5000, 6.3),
        (20, 160, 2, 32, 5, 8, 'Unisoc T610', 4000, 6.0)
    ]

    # Inserción de datos
    for espec in datos_especificaciones:
        cursor.execute("""
                       INSERT INTO Especificaciones (id_Especificaciones, Peso, RAM, Almacenamiento,
                                                     Camara_Front, Camara_Tras, Procesador, Bateria, Pantalla_Tamaño)
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                       """, espec)


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