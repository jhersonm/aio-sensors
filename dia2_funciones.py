# Mes 1 - Día 2: Funciones
# Proyecto: AIO Sensors

# Una función es un bloque de código reutilizable
# Se define con "def" seguido del nombre y parámetros
# Los parámetros son los datos que necesita la función para trabajar
def verificar_sensor(nombre, presion, temperatura):
    # Imprimimos el nombre del sensor como encabezado
    # \n agrega una línea vacía antes para mejor legibilidad
    print(f"\n--- {nombre} ---")
    
    # Verificamos la presión con condicionales
    # Si supera 1050 es crítico, entre 1020-1050 es elevado, sino normal
    if presion > 1050:
        print(f"  Presión: 🚨 CRÍTICO ({presion} hPa)")
    elif presion > 1020:
        print(f"  Presión: ⚠️ ELEVADO ({presion} hPa)")
    else:
        print(f"  Presión: ✅ NORMAL ({presion} hPa)")

    # Verificamos la temperatura
    # 80°C o más se considera peligroso en ambiente industrial
    if temperatura >= 80:
        print(f"  Temperatura: 🚨 ALERTA ({temperatura} °C)")
    else:
        print(f"  Temperatura: ✅ NORMAL ({temperatura} °C)")

# Aquí comienza el programa principal
# Llamamos la función 3 veces con datos de sensores diferentes
# Cada llamada ejecuta todo el código de la función con esos valores
print("=== REPORTE AIO SENSORS ===")

# Parámetros: nombre del sensor, presión en hPa, temperatura en °C
verificar_sensor("Sensor Planta Norte", 1013.25, 25.0)
verificar_sensor("Sensor Planta Sur",   1055.0,  85.0)
verificar_sensor("Sensor Almacén",      1025.0,  60.0)