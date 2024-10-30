frase = input("Por favor, ingresa una frase: ")
letra = input("Ingresa la letra que deseas contar: ")

if len(letra) != 1:
    print("Por favor, ingresa solo una letra.")
else:
    frecuencia = frase.count(letra)
    print(f"La letra '{letra}' aparece {frecuencia} veces en la frase.")

