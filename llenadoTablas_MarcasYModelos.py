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

    # 📱 Marcas de celulares
    marcas = [
        "Apple", "Samsung", "Xiaomi", "Motorola", "Huawei",
        "Oppo", "Vivo", "Realme", "Sony", "Google", "OnePlus", "Nokia"
    ]

    # 🧩 Modelos por marca
    modelos_por_marca = {
        "Apple": ["iPhone 14", "iPhone 13 Pro", "iPhone SE"],
        "Samsung": ["Galaxy S23", "Galaxy A54", "Galaxy Z Fold"],
        "Xiaomi": ["Redmi Note 12", "Poco X5", "Mi 11"],
        "Motorola": ["Moto G73", "Edge 40", "Moto E13"],
        "Huawei": ["P50 Pro", "Nova 11", "Mate Xs"],
        "Oppo": ["Reno10", "Find X5", "A78"],
        "Vivo": ["V27", "Y36", "X90 Pro"],
        "Realme": ["Realme 11 Pro", "Narzo 60", "C55"],
        "Sony": ["Xperia 1 V", "Xperia 10 IV"],
        "Google": ["Pixel 8", "Pixel 7a"],
        "OnePlus": ["OnePlus 11", "Nord CE 3"],
        "Nokia": ["G22", "X30", "C32"]
    }

    # 🚀 Insertar marcas y modelos
    marca_ids = {}

    for marca in marcas:
        cursor.execute("INSERT INTO Marcas (Nombre) VALUES (?)", marca)
        cursor.execute("SELECT id_Marca FROM Marcas WHERE Nombre = ?", marca)
        id_marca = cursor.fetchone()[0]
        marca_ids[marca] = id_marca

        for modelo in modelos_por_marca.get(marca, []):
            cursor.execute(
                "INSERT INTO Modelos (Modelo, id_Marca) VALUES (?, ?)",
                modelo, id_marca
            )

    conn.commit()
    print("✅ Certificaciones insertadas correctamente.")

except pyodbc.Error as e:
    print(f"❌ Error de SQL Server: {str(e)}")
except Exception as e:
    print(f"❌ Error general: {str(e)}")

finally:
    if 'conn' in locals():
        conn.close()