"""
Streamlit con visualizaciones en Seaborn
Dentro de tu app principal, hacemos consulta a Redis, convertimos a DataFrame y visualizamos con Seaborn:

"""
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import redis.asyncio as redis
import asyncio

r = redis.Redis()

async def get_prices():
    regiones = ['San José', 'Alajuela', 'Limón']
    tipos = ['corporativo', 'personal', 'premium']
    celulares = [101, 102, 103]

    data = []
    for region in regiones:
        for tipo in tipos:
            for cid in celulares:
                key = f"precio:{region}:{tipo}:{cid}"
                precio = await r.get(key)
                if precio:
                    data.append({
                        "Región": region,
                        "Tipo Cliente": tipo,
                        "ID Celular": cid,
                        "Precio": float(precio)
                    })
    return pd.DataFrame(data)

st.title("🧠 Precios Simulados por Región y Cliente")

df = asyncio.run(get_prices())
st.dataframe(df)

# Visualización Seaborn
st.subheader("📈 Distribución de precios simulados")

fig, ax = plt.subplots(figsize=(8,5))
sns.boxplot(x="Región", y="Precio", hue="Tipo Cliente", data=df, ax=ax)
st.pyplot(fig)
