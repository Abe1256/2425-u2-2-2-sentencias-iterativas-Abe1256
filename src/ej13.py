def eco_programa():
    while True:
        entrada = input("Introduce algo (escribe 'salir' para terminar): ")
        if entrada.lower() == "salir":
            print("Programa terminado.")
            break
        print(f"Eco: {entrada}")

eco_programa()