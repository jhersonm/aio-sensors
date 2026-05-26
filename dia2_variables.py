# Mes 1 - Día 2: Variables y tipos de datos
# Proyecto: AIO Sensors

# Datos de un sensor industrial
nombre = "Sensor de presión"
ubicacion = "Planta Minera Norte"
valor_actual = 1013.25
unidad = "hPa"
activo = True
alertas_hoy = 3

# Mostramos la información
print("=== REPORTE DE SENSOR ===")
print("Nombre:", nombre)
print("Ubicación:", ubicacion)
print("Valor actual:", valor_actual, unidad)
print("¿Activo?:", activo)
print("Alertas hoy:", alertas_hoy)
# Verificar tipos
print("\n=== TIPOS DE DATOS ===")
print(type(nombre))
print(type(valor_actual))
print(type(alertas_hoy))
print(type(activo))