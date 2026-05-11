import datetime  # Esta pieza sirve para saber la hora

# 1. Configuración de Identidad
nombre_usuario = "Omar" 
ubicacion = "León, Guanajuato"

# 2. Sensor de Tiempo (Buenos días, tardes o noches)
hora = datetime.datetime.now().hour
if hora < 12:
    saludo = "Buenos días"
elif 12 <= hora < 19:
    saludo = "Buenas tardes"
else:
    saludo = "Buenas noches"

# 3. Frase de Activación
print(f"{saludo}, Jefe {nombre_usuario}.")
print("Viernes lista para trabajar con usted, ¿qué haremos hoy?")

# 4. Conciencia de Datos (Fecha y Ubicación)
print(f"Sistemas activos en: {ubicacion}")
print(f"Fecha estelar: {datetime.date.today()}")
