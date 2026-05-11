nombre = input("¿Quién intenta acceder al sistema? ")
print("Bienvenido, " + nombre)

mision = input("¿Quieres ir a ENTRENAR o DESCANSAR? ")

if mision == "ENTRENAR":
    print("Preparando la armadura... ¡A darle con todo!")
else:
    print("Modo de ahorro de energía activado. Disfrute su descanso, señor.")

humor = input("¿Cómo se siente hoy, señor? ")

if humor == "ABURRIDO":
    print("¿Sabe qué hace un robot al salir de vacaciones?")
    print("¡Se va a la playa a cargar las baterías! Jajaja.")
else:
    print("Me alegra que se sienta " + humor + ". ¡Vamos por un gran día!")
