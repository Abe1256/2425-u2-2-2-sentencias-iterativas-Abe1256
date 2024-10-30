def analizar_frase():
    frase = input("Ingrese una frase: ")
    palabras = frase.split()  
    if not palabras:  
        print("No se ingresaron palabras.")
        return
    
    palabra_mas_larga = max(palabras, key=len)  
    cantidad_palabras = len(palabras)  

    print(f"La palabra más larga es: '{palabra_mas_larga}'")
    print(f"Cantidad de palabras: {cantidad_palabras}")

analizar_frase()
