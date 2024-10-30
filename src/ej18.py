def suma_digitos(n):
    return sum(int(d) for d in str(n))

contador_pares = 0

while True:
    numero = int(input("Ingrese un número entero positivo (-1 para terminar): "))
    if numero == -1:
        break
    if numero >= 0:
        suma = suma_digitos(numero)
        print(f"La suma de los dígitos de {numero} es: {suma}")
        if numero % 2 == 0:
            contador_pares += 1
    else:
        print("Por favor, ingrese un número entero positivo.")

print(f"Se ingresaron {contador_pares} números pares.")
