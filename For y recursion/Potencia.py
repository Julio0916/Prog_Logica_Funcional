"""Compara el cálculo iterativo y recursivo de una potencia."""

# Importamos time para medir el tiempo de ejecución.
import time

# Número base y potencia que vamos a calcular.
numero = 2
potencia = 5


# ---------------- POTENCIA USANDO FOR ----------------

inicio = time.perf_counter()

resultado_for = 1

# Multiplicamos el número por sí mismo según la potencia.
for i in range(potencia):
    resultado_for = resultado_for * numero

fin = time.perf_counter()
tiempo_for = fin - inicio


# ---------------- POTENCIA USANDO RECURSIÓN ----------------

def potencia_recursiva(base, exponente):
    """Devuelve ``base`` elevado a ``exponente`` mediante recursión."""

    # Caso base: cualquier número elevado a cero es 1.
    if exponente == 0:
        return 1

    # Multiplicamos la base y reducimos el exponente.
    return base * potencia_recursiva(base, exponente - 1)


inicio = time.perf_counter()

resultado_recursion = potencia_recursiva(numero, potencia)

fin = time.perf_counter()
tiempo_recursion = fin - inicio


# ---------------- MOSTRAR RESULTADOS ----------------

print("Número:", numero)
print("Potencia:", potencia)

print("Resultado con for:", resultado_for)
print("Tiempo con for:", tiempo_for)

print("Resultado con recursión:", resultado_recursion)
print("Tiempo con recursión:", tiempo_recursion)