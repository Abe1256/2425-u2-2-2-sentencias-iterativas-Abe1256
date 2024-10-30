numero = int(input("Ingrese un número entero positivo: "))

if numero > 0:
    
impares = [str(i) for i in range(1, numero + 1) if i % 2 != 0]
    print("Números impares desde 1 hasta", numero, ":", ", ".join(impares))
else:
    print("Por favor, ingrese un número entero positivo.")