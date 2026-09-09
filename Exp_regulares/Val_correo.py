"""Valida direcciones de correo electrónico mediante una expresión regular."""

import re


def validar_correo(correo):
    """Devuelve True si ``correo`` tiene un formato de correo válido.

    Exige texto antes de ``@``, un dominio y una extensión de al menos
    dos letras.
    """
    patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*\.[a-zA-Z]{2,}$"

    return re.fullmatch(patron, correo) is not None


# Se ignoran espacios accidentales al principio y al final de la entrada.
correo = input("Ingresa un correo electrónico: ").strip()

if validar_correo(correo):
    print("El correo electrónico es válido.")
else:
    print("El correo electrónico no es válido.")