# Mes 1 - Día 2: Loops
# Proyecto: AIO Sensors

# Lista de sensores con sus valores
sensores = [
    {"nombre": "Sensor 1", "presion": 1013.25},
    {"nombre": "Sensor 2", "presion": 1055.0},
    {"nombre": "Sensor 3", "presion": 980.0},
    {"nombre": "Sensor 4", "presion": 1025.0},
    {"nombre": "Sensor 5", "presion": 1060.0},
]

print("=== REVISIÓN DE SENSORES ===")

# Recorremos cada sensor
for sensor in sensores:
    nombre = sensor["nombre"]
    presion = sensor["presion"]

    if presion > 1050:
        estado = "🚨 CRÍTICO"
    elif presion > 1020:
        estado = "⚠️ ELEVADO"
    else:
        estado = "✅ NORMAL"

    print(f"{nombre} - {presion} hPa - {estado}")