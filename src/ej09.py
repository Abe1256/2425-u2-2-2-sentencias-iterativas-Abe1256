contraseña_correcta = "contraseña"

entrada_usuario = ""

while entrada_usuario != contraseña_correcta:
    entrada_usuario = input("Por favor, introduce la contraseña: ")
    if entrada_usuario == contraseña_correcta:
        print("Contraseña correcta. Acceso concedido.")
    else:
        print("Contraseña incorrecta. Inténtalo de nuevo.")