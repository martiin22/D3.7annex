   temperatura = float(input("Ingrese la temperatura: "))
   escala = input("Ingrese la escala (Celsius o Fahrenheit): ")
if escala.lower() == 'celsius':
    fahrenheit = (temperatura *9/5) + 32
    print(f"{temperatura}°C es igual a {fahrenheit}°F")
elif escala.lower() == 'fahrenheit':
    celsius = (temperatura - 32)* 5/9
    print(f"{temperatura}°F es igual a {celsius}°C")
else:
    print("Escala no válida.")