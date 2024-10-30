def mostrar_menu():
    print("Menú:")
    print("1 - Comenzar programa")
    print("2 - Imprimir listado")
    print("3 - Finalizar programa")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1, 2 o 3): ")

        if opcion == '1':
            print("Programa comenzado.")
        elif opcion == '2':
            print("Listado impreso.")
        elif opcion == '3':
            print("Programa finalizado.")
            break
        else:
            print("Opción incorrecta. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()
