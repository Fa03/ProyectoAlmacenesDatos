"""
¡Dale, Fabián! Aquí vamos con una propuesta modular que conecta Streamlit, simulación 
de precios con redis.asyncio, y vistas SQL para análisis por marca y cliente. Así no solo ves qué ha 
pasado, sino también qué podría pasar 📈

Módulo Streamlit: Ventas por sucursal y precios simulados
Primero, configuramos la app base que toma datos de ventas y muestra una simulación de precios futura:


"""


import streamlit as st
import pandas as pd
import redis.asyncio as redis
import asyncio
from datetime import datetime, timedelta
import random

# Redis connection
r = redis.Redis()

async def simulate_future_price(id_celular: int, precio_actual: float):
    fluct = round(precio_actual * (1 + random.uniform(-0.05, 0.08)), 2)
    key = f"precio_simulado:{id_celular}"
    await r.set(key, fluct)
    return fluct

# UI
st.title("Ventas por Sucursal y Simulación de Precios 📊")

# Ejemplo de carga de ventas
df_ventas = pd.read_csv("ventas.csv")  # adaptá esto a tu fuente real

# Filtro por sucursal
sucursal = st.selectbox("Seleccioná sucursal", df_ventas['sucursal'].unique())
ventas_sucursal = df_ventas[df_ventas['sucursal'] == sucursal]
st.write("Resumen de ventas:", ventas_sucursal)

# Simulación de precios
celulares = ventas_sucursal['id_celular'].unique()
precios_actuales = dict(zip(celulares, [300.00, 420.00, 210.00]))  # ejemplo

simulados = {}
for cid in celulares:
    simulados[cid] = asyncio.run(simulate_future_price(cid, precios_actuales[cid]))

st.subheader("📈 Precios simulados (futuros)")
for cid, precio in simulados.items():
    st.write(f"Celular {cid}: ₡{precio}")