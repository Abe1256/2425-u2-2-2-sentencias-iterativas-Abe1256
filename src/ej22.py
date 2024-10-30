def contar_digitos(numero):
    pares = 0
    impares = 0
    for digito in str(numero):
        if int(digito) % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares

def main():
    total_pares = 0
    total_impares = 0
    while True:
        numero = int(input("Ingrese un número entero positivo (0 para terminar): "))
        if numero == 0:
            break
        pares, impares = contar_digitos(numero)
        total_pares += pares
        total_impares += impares
        print(f"Número: {numero} - Dígitos pares: {pares}, Dígitos impares: {impares}")

    print(f"Total de dígitos pares: {total_pares}, Total de dígitos impares: {total_impares}")

if __name__ == "__main__":
    main()
