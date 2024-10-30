def encontrar_mayor_numero():
    mayor = 0
    while True:
        numero = int(input("Ingrese un número entero positivo (0 para terminar): "))
        if numero == 0:
            break
        elif numero < 0:
            print("Por favor, ingrese solo números enteros positivos.")
            continue
        if numero > mayor:
            mayor = numero
    print(f"El mayor número ingresado fue: {mayor}")

encontrar_mayor_numero()