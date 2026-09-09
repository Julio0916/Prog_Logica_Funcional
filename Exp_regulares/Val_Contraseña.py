"""Valida que una contraseña cumpla requisitos básicos de seguridad."""

import re

def validar_contrasena(contrasena):
    """Devuelve True si la contraseña cumple todos los requisitos.

    La contraseña debe tener al menos ocho caracteres, no contener espacios,
    e incluir una minúscula, una mayúscula, un número y un carácter especial.
    """
    patron = (
        r"^(?=.*[a-z])"       # Usar al menos una letra minúscula
        r"(?=.*[A-Z])"        # Usar al menos una letra mayúscula
        r"(?=.*\d)"           # Usar al menos un número
        r"(?=.*[!@#$%^&*._-])"  # Usar al menos un carácter especial
        r"\S{8,}$"            # Mínimo 8 caracteres y ningún espacio
    )

    return re.fullmatch(patron, contrasena) is not None

# No se usa strip() para que los espacios introducidos también sean rechazados.
contrasena = input("Ingresa una contraseña: ")

if validar_contrasena(contrasena):
    print("La contraseña es segura.")
else:
    print("La contraseña no es segura.")
    print("Debe tener al menos 8 caracteres, una mayúscula,")
    print("una minúscula, un número y un carácter especial.")