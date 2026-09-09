"""Compara dos formas de calcular el máximo común divisor (MCD)."""

# Importamos time para medir el tiempo de ejecución.
import time

# Números para calcular su máximo común divisor.
numero1 = 48
numero2 = 18


# ---------------- ALGORITMO DE EUCLIDES CON FOR ----------------

inicio = time.perf_counter()

a = numero1
b = numero2

# Repetimos las divisiones hasta que el residuo sea cero.
for i in range(min(numero1, numero2) + 1):

    # Cuando b es cero, el valor de a es el máximo común divisor.
    if b == 0:
        break

    # Guardamos b y el residuo de dividir a entre b.
    a, b = b, a % b

mcd_for = a

fin = time.perf_counter()
tiempo_for = fin - inicio


# ---------------- ALGORITMO DE EUCLIDES CON RECURSIÓN ----------------

def euclides_recursivo(a, b):
    """Devuelve el MCD de dos números mediante el algoritmo de Euclides."""

    # Caso base: cuando b es cero, encontramos el MCD.
    if b == 0:
        return a

    # Llamamos nuevamente a la función usando el residuo.
    return euclides_recursivo(b, a % b)


inicio = time.perf_counter()

# Calculamos el máximo común divisor usando recursión.
mcd_recursion = euclides_recursivo(numero1, numero2)

fin = time.perf_counter()
tiempo_recursion = fin - inicio


# ---------------- MOSTRAR RESULTADOS ----------------

print("Primer número:", numero1)
print("Segundo número:", numero2)

print("MCD con for:", mcd_for)
print("Tiempo con for:", tiempo_for)

print("MCD con recursión:", mcd_recursion)
print("Tiempo con recursión:", tiempo_recursion)