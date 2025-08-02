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

    # # 🏗️ Crear tabla si no existe
    # cursor.execute("""
    #     IF NOT EXISTS (
    #         SELECT * FROM INFORMATION_SCHEMA.TABLES
    #         WHERE TABLE_NAME = 'Certificaciones'
    #     )
    #     CREATE TABLE CertificacionesCelulares (
    #         id_Certificacion INT PRIMARY KEY,
    #         TipoCertificacion VARCHAR(10)
    #     )
    # """)
    # conn.commit()

    # # 📋 Lista de certificaciones de celulares
    # certificaciones = [
    #     "FCC", "CE", "PTCRB", "CCC", "IC",
    #     "NOM", "SUTEL", "JATE", "BIS", "ANATEL"
    # ]

    # 🚀 Insertar datos
    # for idx, tipo in enumerate(certificaciones, start=1):
    #     cursor.execute("""
    #         IF NOT EXISTS (
    #             SELECT 1 FROM Certificaciones WHERE id_Certificacion = ?
    #         )
    #         INSERT INTO Certificaciones (id_Certificacion, TipoCertificacion)
    #         VALUES (?, ?)
    #     """, idx, idx, tipo)

    conn.commit()
    print("✅ Certificaciones insertadas correctamente.")

except pyodbc.Error as e:
    print(f"❌ Error de SQL Server: {str(e)}")
except Exception as e:
    print(f"❌ Error general: {str(e)}")

finally:
    if 'conn' in locals():
        conn.close()

# =====================================  SEGUNDA TABLA A POBLAR Categorias =====================================
# '''
# DIRECTAMENTE EN SQL

# insert into Categorias(id_Categoria,NombreCategoria)
# values(1,'Gama Baja'),
# 	  (2,'Gama Media'),
#       (3,'Gama Alta'),
# 	  (4,'Gama premium/flagshi')
# '''

