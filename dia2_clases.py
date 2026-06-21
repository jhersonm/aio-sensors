# Mes 1 - Día 2: Clases
# Proyecto: AIO Sensors

# Definimos la clase Sensor - es el molde para crear sensores
# Todo sensor tendrá: nombre, ubicacion, presion y temperatura
class Sensor:

    # __init__ es el constructor - se ejecuta al crear un sensor
    # self representa al objeto que se está creando
    def __init__(self, nombre, ubicacion, presion, temperatura):
        self.nombre = nombre          # guardamos el nombre en el objeto
        self.ubicacion = ubicacion    # guardamos la ubicación
        self.presion = presion        # guardamos la presión
        self.temperatura = temperatura # guardamos la temperatura

    # Método que verifica y muestra el estado del sensor
    # Un método es una función que pertenece a la clase
    def verificar_estado(self):
        print(f"\n--- {self.nombre} ({self.ubicacion}) ---")

        # Verificamos presión
        if self.presion > 1050:
            print(f"  Presión: 🚨 CRÍTICO ({self.presion} hPa)")
        elif self.presion > 1020:
            print(f"  Presión: ⚠️ ELEVADO ({self.presion} hPa)")
        else:
            print(f"  Presión: ✅ NORMAL ({self.presion} hPa)")

        # Verificamos temperatura
        if self.temperatura >= 80:
            print(f"  Temperatura: 🚨 ALERTA ({self.temperatura} °C)")
        else:
            print(f"  Temperatura: ✅ NORMAL ({self.temperatura} °C)")

    # Método que actualiza el valor de presión del sensor
    def actualizar_presion(self, nueva_presion):
        print(f"\n  Actualizando presión de {self.nombre}...")
        self.presion = nueva_presion  # reemplazamos el valor anterior
        print(f"  Nueva presión: {self.presion} hPa")


# Creamos 3 sensores usando la clase como molde
sensor1 = Sensor("Sensor Norte", "Planta Norte", 1013.25, 25.0)
sensor2 = Sensor("Sensor Sur",   "Planta Sur",   1055.0,  85.0)
sensor3 = Sensor("Sensor Almacén", "Almacén",    1025.0,  60.0)

# Verificamos el estado de cada sensor
print("=== REPORTE AIO SENSORS ===")
sensor1.verificar_estado()
sensor2.verificar_estado()
sensor3.verificar_estado()

# Actualizamos la presión del sensor1 y verificamos de nuevo
sensor1.actualizar_presion(1058.0)
sensor1.verificar_estado()