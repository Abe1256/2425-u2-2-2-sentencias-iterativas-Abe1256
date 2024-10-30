def sumar_numeros_positivos():
    suma = 0
    while True:
        numero = int(input("Ingrese un número entero (0 para terminar): "))
        if numero == 0:
            break
        elif numero > 0:
            suma += numero
    print(f"La sumatoria de los números positivos ingresados es: {suma}")

sumar_numeros_positivos()