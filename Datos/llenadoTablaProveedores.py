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

    # Datos simulados de proveedores
    datos_proveedores = [
        (1, 'Celulares Tico S.A.', 'contacto@celesticocr.com'),
        (2, 'Distribuidora GlobalTech', '+506 8888-1234'),
        (3, 'ElectroMóvil CR', 'ventas@electromovil.cr'),
        (4, 'Importadora La Esquina', '+506 7012-4567'),
        (5, 'Smart Solutions Ltda.', 'info@smartsolutions.com'),
        (6, 'Juan Pérez', 'juan.perez@proveedores.com'),
        (7, 'TecnoMundo', '+506 6000-9988'),
        (8, 'Grupo Innovacel', 'soporte@innovacel.com'),
        (9, 'María Rodríguez', '+506 7200-3344'),
        (10, 'ElectroTico', 'electrotico@correo.cr')
    ]

    # Inserción de datos
    for id_prov, nombre, contacto in datos_proveedores:
        cursor.execute("""
                       INSERT INTO Proveedores (id_Proveedor, NombreProveedor, Contacto)
                       VALUES (?, ?, ?)
                       """, id_prov, nombre, contacto)


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