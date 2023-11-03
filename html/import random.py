import random

numero_secreto = random.randint(1, 100)
intentos = 0

while True:
    intento = int(input("Adivina el número (entre 1 y 100): "))
    intentos += 1
    if intento < numero_secreto:
        print("El número es mayor. Intenta de nuevo.")
    elif intento > numero_secreto:
        print("El número es menor. Intenta de nuevo.")
    else:
        print(f"¡Adivinaste el número en {intentos} intentos!")
        break