"""Valida si una entrada representa un número entero o decimal."""

import re


def validar_numero(dato):
    """Devuelve True si ``dato`` tiene formato numérico válido.

    Se permiten signos positivo o negativo y una parte decimal opcional.
    """
    patron = r"^[+-]?\d+(?:\.\d+)?$"

    return re.fullmatch(patron, dato) is not None


# Se eliminan espacios al inicio y al final antes de validar la entrada.
dato = input("Ingresa un dato numérico: ").strip()

if validar_numero(dato):
    print("El dato numérico es válido.")
else:
    print("El dato numérico no es válido.")