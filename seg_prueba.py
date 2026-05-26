# Mes 1 - Día 2: Variables y tipos de datos
# Proyecto: AIO Sensors

# Datos de un sensor industrial
nombre = "Sensor de presión"
ubicacion = "Planta Minera Norte"
valor_actual = 1013.25
valor_actual_1=valor_actual*2/8
unidad = "hPa"
activo = True
alertas_hoy = 5

# Mostramos la información
print("=== REPORTE DE SENSOR ===")
print("Nombre:", nombre)
print("Ubicación:", ubicacion)
print("Valor actual:", valor_actual_1, unidad)
print("¿Activo?:", activo)
print("Alertas hoy:", alertas_hoy)