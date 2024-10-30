def contar_digitos(titulos):
    return sum(c.isdigit() for c in titulos)

def main():
    lineas_completas = 0
    titulos_linea = ""
    
    while True:
        entrada = input("Ingrese un título de libro (o '*' para finalizar): ")
        
        if entrada == "*":
            break
        
        if entrada == "/":
            if titulos_linea:
                digitos = contar_digitos(titulos_linea)
                print(f"Número de dígitos en la línea: {digitos}")
                lineas_completas += 1
                titulos_linea = ""
        else:
            titulos_linea += entrada + " "
    
    print(f"Número total de líneas completas ingresadas: {lineas_completas}")

if __name__ == "__main__":
    main()
