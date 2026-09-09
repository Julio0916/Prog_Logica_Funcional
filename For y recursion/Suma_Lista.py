"""Compara la suma iterativa y recursiva de una lista de números."""

# Importamos time para medir el tiempo de ejecución.
import time

# Lista de números que vamos a sumar.
numeros = [5, 10, 15, 20, 25]


# ---------------- SUMA USANDO FOR ----------------

inicio = time.perf_counter()

suma_for = 0

# Recorremos la lista y acumulamos cada número.
for numero in numeros:
    suma_for = suma_for + numero

fin = time.perf_counter()
tiempo_for = fin - inicio


# ---------------- SUMA USANDO RECURSIÓN ----------------

def suma_recursiva(lista, posicion=0):
    """Suma recursivamente los elementos de ``lista`` desde ``posicion``."""

    # Caso base: termina al llegar al final de la lista.
    if posicion == len(lista):
        return 0

    # Sumamos el elemento actual y avanzamos a la siguiente posición.
    return lista[posicion] + suma_recursiva(lista, posicion + 1)


inicio = time.perf_counter()

suma_recursion = suma_recursiva(numeros)

fin = time.perf_counter()
tiempo_recursion = fin - inicio


# ---------------- MOSTRAR RESULTADOS ----------------

print("Lista:", numeros)

print("Suma con for:", suma_for)
print("Tiempo con for:", tiempo_for)

print("Suma con recursión:", suma_recursion)
print("Tiempo con recursión:", tiempo_recursion)