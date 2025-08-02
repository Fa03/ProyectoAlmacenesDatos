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

    # Generar combinaciones y precios

    for id_celular in range(1, 34):  # 1 a 33
        precio = round(random.uniform(120000, 650000), 2)  # precios en colones
        cursor.execute("""
                       INSERT INTO PreciosxRegion (id_Region, id_Celular, PrecioRegional)
                       VALUES (?, ?, ?)
                       """, id_celular, id_celular, precio)


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