"""Valida y descompone una matrícula escolar."""

import re


def validar_matricula(matricula):
    """Valida una matrícula y muestra sus partes si es correcta.

    El formato esperado es: dos dígitos del año, la clave ``115`` y cuatro
    dígitos que identifican al alumno.
    """
    # Grupo 1: dos dígitos del año
    # Grupo 2: clave del plantel (115)
    # Grupo 3: identificador de cuatro dígitos
    patron = r"^(\d{2})(115)(\d{4})$"

    coincidencia = re.fullmatch(patron, matricula)

    if coincidencia:
        año = "20" + coincidencia.group(1)
        carrera = coincidencia.group(2)
        identificador = coincidencia.group(3)

        print("La matrícula es válida.")
        print("Año de ingreso:", año)
        print("Clave del plantel:", carrera)
        print("Identificador del alumno:", identificador)
    else:
        print("La matrícula no es válida.")
        print("Formato requerido: dos dígitos del año, 115 y cuatro dígitos.")


# Se eliminan espacios accidentales antes de aplicar el patrón.
matricula = input("Ingresa la matrícula escolar: ").strip()
validar_matricula(matricula)