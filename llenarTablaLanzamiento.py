import pyodbc
import urllib
import random

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


    # Lista de celulares con precios en colones
    celulares = [
        ("Apple", "iPhone 14", "2022-09-01", 431460),
        ("Apple", "iPhone 13 Pro", "2021-09-01", 485460),
        ("Apple", "iPhone SE (2022)", "2022-03-01", 231660),
        ("Samsung", "Galaxy S23", "2023-02-01", 539460),
        ("Samsung", "Galaxy A54", "2023-03-01", 242460),
        ("Samsung", "Galaxy Z Fold5", "2023-08-01", 971460),
        ("Xiaomi", "Redmi Note 12", "2023-01-01", 134460),
        ("Xiaomi", "Poco X5", "2023-02-01", 161460),
        ("Xiaomi", "Mi 11", "2021-01-01", 269460),
        ("Motorola", "Moto G73", "2023-01-01", 150660),
        ("Motorola", "Edge 40", "2023-05-01", 296460),
        ("Motorola", "Moto E13", "2023-02-01", 69660),
        ("Huawei", "P50 Pro", "2021-07-01", 431460),
        ("Huawei", "Nova 11", "2023-04-01", 242460),
        ("Huawei", "Mate Xs", "2020-03-01", 1349460),
        ("Oppo", "Reno10", "2023-07-01", 242460),
        ("Oppo", "Find X5", "2022-03-01", 485460),
        ("Oppo", "A78", "2023-01-01", 123660),
        ("Vivo", "V27", "2023-03-01", 242460),
        ("Vivo", "Y36", "2023-05-01", 123660),
        ("Vivo", "X90 Pro", "2022-11-01", 539460),
        ("Realme", "Realme 11 Pro", "2023-05-01", 188460),
        ("Realme", "Narzo 60", "2023-07-01", 97200),
        ("Realme", "C55", "2023-03-01", 96660),
        ("Sony", "Xperia 1 V", "2023-07-01", 755460),
        ("Sony", "Xperia 10 IV", "2022-06-01", 269460),
        ("Google", "Pixel 8", "2023-10-01", 377460),
        ("Google", "Pixel 7a", "2023-05-01", 269460),
        ("OnePlus", "OnePlus 11", "2023-02-01", 431460),
        ("OnePlus", "Nord CE 3", "2023-08-01", 110700),
        ("Nokia", "G22", "2023-02-01", 100440),
        ("Nokia", "X30", "2022-09-01", 215460),
        ("Nokia", "C32", "2023-02-01", 58860),
    ]

    # Insertar en la tabla
    contador = 1
    for marca, modelo, fecha, precio_crc in celulares:
        cursor.execute("""
                       INSERT INTO Lanzamiento (id_Preciolanzamiento, Precio, Fecha_Lanzamiento, id_Celular)
                       VALUES (?, ?, ?, ?)
                       """, contador, precio_crc, fecha, contador)
        contador += 1



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