"""Compara el cálculo iterativo y recursivo del factorial de un número."""

# Importamos la librería time para medir el tiempo de ejecución.
import time

# Número que utilizaremos para calcular su factorial.
numero = 5

# Guardamos el tiempo justo antes de comenzar el cálculo.
inicio = time.perf_counter()

# El factorial comienza en 1 porque multiplicar por 1 no cambia el resultado.
factorial_for = 1
for i in range(1, numero + 1):
    factorial_for *= i

fin = time.perf_counter()
tiempo_for = fin - inicio


# Esta función se llama a sí misma para calcular el factorial.
def factorial_recursivo(n):
    """Devuelve el factorial de ``n`` mediante llamadas recursivas."""

    # Caso base: el factorial de 0 y de 1 es igual a 1.
    # También evita que la función continúe llamándose indefinidamente.
    if n <= 1:
        return 1
    return n * factorial_recursivo(n - 1)


# Guardamos el tiempo antes de llamar a la función recursiva.
inicio = time.perf_counter()
# Calculamos el factorial utilizando recursión.
factorial_recursion = factorial_recursivo(numero)
# Guardamos el tiempo cuando termina el cálculo.
fin = time.perf_counter()
# Calculamos cuánto tiempo tardó la recursión.
tiempo_recursion = fin - inicio


# Mostrar resultados
print("Número:", numero)
print("Factorial con for:", factorial_for)
print("Tiempo con for:", tiempo_for)

print("Factorial con recursión:", factorial_recursion)
print("Tiempo con recursión:", tiempo_recursion)