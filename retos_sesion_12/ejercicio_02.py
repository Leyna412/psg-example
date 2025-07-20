# Definición de usuarios y contraseñas usando un diccionario
usuarios = {
    "admin": "admin123",
    "user1": "user123",
    "user2": "user123",
    "user3": "user123"
}

# Solicitar credenciales al usuario
print("=== Inicio de Sesión ===")
usuario = input("Ingrese su nombre de usuario: ")
contraseña = input("Ingrese su contraseña: ")

# Verificar credenciales usando estructura condicional
if usuario in usuarios and usuarios[usuario] == contraseña:
    print("Acceso Aprobado")
    print(f"Bienvenido, {usuario}. Ahora puedes gestionar tus tareas.")
else:
    print("Acceso Denegado")
    print("Error: Usuario o contraseña incorrectos.")