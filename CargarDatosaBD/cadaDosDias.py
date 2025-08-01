
"""
 Backend con aioschedule: precios simulados cada 2 días
Creamos un servicio que actualiza Redis cada 48 horas, diferenciando por región y tipo de cliente:

"""

import redis.asyncio as redis
import aioschedule
import asyncio
import random

# Redis connection
r = redis.Redis()

# Simulación según región y tipo de cliente
async def simulate_prices():
    regiones = ['San José', 'Alajuela', 'Limón']
    tipos = ['corporativo', 'personal', 'premium']
    celulares = [101, 102, 103]  # ejemplo de IDs

    for region in regiones:
        for tipo in tipos:
            for cid in celulares:
                base = 250 + (hash(region + tipo) % 150)
                precio_sim = round(base * (1 + random.uniform(-0.03, 0.07)), 2)
                key = f"precio:{region}:{tipo}:{cid}"
                await r.set(key, precio_sim)
                print(f"🌀 {key} → ₡{precio_sim}")

# Tarea periódica
async def job_runner():
    aioschedule.every(2).days.do(simulate_prices)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(10)

# Iniciá el runner si estás en modo backend
if __name__ == "__main__":
    asyncio.run(job_runner())