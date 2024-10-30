suma_total = 0

while True:
    numero = int(input("Ingrese un número entero (0 para terminar): "))
    if numero == 0:
        break
    suma_total += numero

print("La sumatoria de todos los números ingresados es:", suma_total)
