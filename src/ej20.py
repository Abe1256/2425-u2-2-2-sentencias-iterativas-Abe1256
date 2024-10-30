frase = input("Ingrese una frase: ")
letra_buscada = input("Ingrese una letra: ")

for i in range(len(frase)):
    if frase[i] == letra_buscada:
        print(f"Coincidencia encontrada en la posición: {i}")
        break
    else:
        print(f"No hay coincidencia en la posición: {i}")
