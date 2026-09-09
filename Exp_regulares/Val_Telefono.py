"""Valida números telefónicos mexicanos con prefijo internacional +52."""

import re


def validar_telefono(telefono):
    """Devuelve True si ``telefono`` tiene un formato mexicano válido.

    Se permiten espacios, guiones y paréntesis como separadores, pero después
    de eliminarlos debe quedar ``+52`` seguido de exactamente diez dígitos.
    """
    # Eliminamos espacios, guiones y paréntesis.
    telefono_limpio = re.sub(r"[\s()-]", "", telefono)

    # Debe comenzar con +52 y continuar con exactamente 10 dígitos.
    patron = r"^\+52\d{10}$"

    return re.fullmatch(patron, telefono_limpio) is not None


# Se conserva la entrada original para permitir separadores legibles.
telefono = input("Ingresa un número telefónico de México: ")

if validar_telefono(telefono):
    print("El número telefónico es válido.")
else:
    print("El número telefónico no es válido.")
    print("Debe comenzar con +52 y contener 10 dígitos.")