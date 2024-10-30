def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def contar_primos():
    contador_primos = 0
    while True:
        numero = int(input("Ingrese un número mayor que 1 (0 para terminar): "))
        if numero == 0:
            break
        if numero > 1 and es_primo(numero):
            contador_primos += 1
    print(f"Cantidad de números primos ingresados: {contador_primos}")

contar_primos()
