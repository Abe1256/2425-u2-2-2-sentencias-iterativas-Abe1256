n = int(input("Ingrese un número entero: "))

for i in range(1, n + 1):
    num_impar = 2 * i - 1
    impares = [str(num_impar - 2 * j) for j in range(i)]
    print(" ".join(impares))