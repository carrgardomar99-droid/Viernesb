
import datetime

# --- CONFIGURACIÓN DE IDENTIDAD ---
jefe = "Omar"
ciudad = "León, Guanajuato"
frase_activacion = "Viernes lista para trabajar con usted, ¿qué haremos hoy?"

def obtener_saludo():
    hora = datetime.datetime.now().hour
    if hora < 12:
        return "Buenos días"
    elif 12 <= hora < 19:
        return "Buenas tardes"
    else:
        return "Buenas noches"

# --- EJECUCIÓN DEL SISTEMA ---
print(f"--- SISTEMAS VIERNES ACTIVOS ---")
print(f"{obtener_saludo()}, Jefe {jefe}.")
print(frase_activacion)
print(f"Localización: {ciudad}")
print(f"Fecha estelar: {datetime.date.today()}")
print("--------------------------------")

orden = input("Esperando órdenes, Jefe: ")
print(f"Procesando: {orden}...")
