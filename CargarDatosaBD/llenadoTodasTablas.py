from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from config import params
import random
from datetime import datetime
import time
import pandas as pd


engine = create_engine(f'mssql+pyodbc:///?odbc_connect={params}')
Session = sessionmaker(bind=engine)

# Insertar códigos ya existentes en la base de datos FK
df_clientes = pd.read_sql("SELECT Codigo_Cliente FROM CLIENTE", engine)

# Función seleciona aleatoriamente el código
def obtener_codigo_cliente():
    return df_clientes.sample(1).iloc[0]['Codigo_Cliente']

# Función para insertar un evento en la base de datos con datos simulados
def insertar_dato():
    session = Session()
    try:
        evento = {
            "Codigo_Envio": random.randint(100000, 999999),
            "Codigo_Cliente": obtener_codigo_cliente(),
            "Codigo_Producto": random.randint(1, 49782),
            "Codigo_Pago": random.randint(1, 3),
            "Codigo_Proveedor": random.randint(1, 4),
            "Codigo_Canal": random.randint(1, 2),
            "Codigo_Ubicacion": random.randint(1, 6),
            "Codigo_Destino": random.randint(1, 12),
            "Cantidad": random.randint(1, 50),
            "Costo_Envio": round(random.uniform(5.0, 50.0), 2),
            "Descuento": round(random.uniform(0.00, 0.99), 2),
            "Fecha_Envio": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "Prioridad": random.choice(['High', 'Medium', 'Low'])
        }

        query = text("""
                     INSERT INTO ENVIO (Codigo_Envio, Codigo_Cliente, Codigo_Producto, Codigo_Pago,
                                        Codigo_Proveedor, Codigo_Canal, Codigo_Ubicacion, Codigo_Destino,
                                        Cantidad, Costo_Envio, Descuento, Fecha_Envio, Prioridad)
                     VALUES (:Codigo_Envio, :Codigo_Cliente, :Codigo_Producto, :Codigo_Pago,
                             :Codigo_Proveedor, :Codigo_Canal, :Codigo_Ubicacion, :Codigo_Destino,
                             :Cantidad, :Costo_Envio, :Descuento, :Fecha_Envio, :Prioridad)
                     """)
        #Conexión a la base de datos
        session.execute(query, evento)
        session.execute(text("EXEC sp_refreshview 'vw_Canal_Metodo'"))
        session.commit()
        print("Evento insertado con cliente aleatorio:", evento["Codigo_Cliente"])

    #Para manejo de errores al conectar a la BD
    except Exception as e:
        session.rollback()
        print("Error al insertar evento:", e)

    finally:
        session.close()

#Ciclo para insertar 10 eventos en la base de datos con datos simulados, cada 2 segundos.
for i in range(1, 11):
    insertar_dato()
    time.sleep(2)


