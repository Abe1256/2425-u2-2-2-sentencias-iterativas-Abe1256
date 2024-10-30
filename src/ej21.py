def calcular_total_compras():
    total = 0
    while True:
        monto = float(input("Ingrese el monto de la compra (0 para finalizar): "))
        if monto == 0:
            break
        elif monto < 0:
            print("Monto negativo, por favor ingrese un monto válido.")
            continue
        total += monto

    if total > 1000:
        total *= 0.9  # Aplicar un 10% de descuento

    print(f"El total a pagar es: ${total:.2f}")

calcular_total_compras()
