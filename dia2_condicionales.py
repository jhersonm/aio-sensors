# Mes 1 - Día 2: Condicionales
# Proyecto: AIO Sensors

presion = 1055.0
temperatura = 25.0
sensor_activo = False

# Verificar presión
if presion > 1050:
    print("🚨 ALERTA: Presión crítica -", presion, "hPa")
elif presion > 1020:
    print("⚠️ ADVERTENCIA: Presión elevada -", presion, "hPa")
else:
    print("✅ Presión normal -", presion, "hPa")

# Verificar temperatura
if temperatura >= 80:
    print("🚨 ALERTA: Temperatura alta -", temperatura, "°C")
else:
    print("✅ Temperatura normal -", temperatura, "°C")

# Verificar estado del sensor
if sensor_activo:
    print("✅ Sensor operativo")
else:
    print("❌ Sensor fuera de línea")