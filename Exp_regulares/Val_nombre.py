"""Valida nombres formados por letras y separadores comunes."""

import re


def validar_nombre(nombre):
    """Devuelve True si ``nombre`` solo contiene caracteres permitidos.

    Se aceptan letras del español, espacios, guiones y apóstrofes entre
    palabras. No se permiten números ni separadores consecutivos.
    """
    # Solo permite letras, incluyendo acentos, diéresis y ñ.
    letras = r"A-Za-zÁÉÍÓÚÜÑáéíóúüñ"

    # Permite palabras separadas por espacio, guion o apóstrofo.
    patron = rf"^[{letras}]+(?:[ '-][{letras}]+)*$"

    return re.fullmatch(patron, nombre) is not None


# Se eliminan espacios exteriores, pero se conservan los separadores internos.
nombre = input("Ingresa un nombre completo: ").strip()

if validar_nombre(nombre):
    print("El nombre es válido.")
else:
    print("El nombre no es válido.")
    print("Debe contener solamente letras y no contener números.")