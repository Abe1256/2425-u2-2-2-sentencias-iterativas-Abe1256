cantidad_invertir = float(input("Ingrese la cantidad a invertir: "))
interes_anual = float(input("Ingrese el interés anual (en %): "))
numero_años = int(input("Ingrese el número de años: "))

for año in range(1, numero_años + 1):
    cantidad_invertir *= 1 + interes_anual / 100
    print(f"Año {año}: Capital acumulado = {cantidad_invertir:.2f}")