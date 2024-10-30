numero = int(input("Introduce un número entero positivo: "))

if numero > 0:
    cuenta_atras = ', '.join(str(i) for i in range(numero, -1, -1))
    print("Cuenta atrás:", cuenta_atras)
else:
    print("Por favor, introduce un número entero positivo.")