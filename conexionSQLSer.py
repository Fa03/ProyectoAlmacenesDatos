import pyodbc
import pandas as pd

# Datos de conexión
server = 'AZUSFA\SQLEXPRESS'  # Puede ser 'localhost' o el nombre del servidor
database = 'Telefonos'
username = "AZUSFA\fab_t"  # Si es autenticación de SQL Server
password = 'TU_CONTRASEÑA'  # No requerido si usas autenticación integrada

# String de conexión usando autenticación de SQL Server
conn = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}')

# Alternativamente, si usas autenticación integrada de Windows:
# conn = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes')

# Ejecutar una consulta
query = "SELECT * FROM TU_TABLA"
df = pd.read_sql(query, conn)

# Cerrar la conexión
conn.close()

# Mostrar los datos
print(df.head())