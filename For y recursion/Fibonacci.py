"""Genera una serie de Fibonacci con un ciclo y con recursión."""

# Importamos la librería time para medir el tiempo
import time

# Indicamos cuántos números tendrá la serie.
cantidad = 10


# ---------------- FIBONACCI USANDO FOR ----------------

# Guardamos el tiempo antes de comenzar.
inicio = time.perf_counter()

# En esta lista guardaremos los números de Fibonacci.
serie_for = []

# Los primeros números de Fibonacci son 0 y 1.
a = 0
b = 1

# El ciclo se repite según la cantidad indicada.
for i in range(cantidad):

    # Agregamos el valor actual a la lista.
    serie_for.append(a)

    # El siguiente número se obtiene sumando los dos anteriores.
    siguiente = a + b

    # Actualizamos los valores para la siguiente repetición.
    a = b
    b = siguiente

# Guardamos el tiempo cuando termina el ciclo.
fin = time.perf_counter()

# Calculamos el tiempo total del método con for.
tiempo_for = fin - inicio


# ---------------- FIBONACCI USANDO RECURSIÓN ----------------

# Esta función calcula el número de Fibonacci
# que se encuentra en la posición n.
def fibonacci_recursivo(n):
    """Devuelve el número de Fibonacci ubicado en la posición ``n``."""

    # Primer caso base: la posición 0 tiene el valor 0.
    if n == 0:
        return 0

    # Segundo caso base: la posición 1 tiene el valor 1.
    if n == 1:
        return 1

    # La función se llama a sí misma para obtener
    # los dos números anteriores y después sumarlos.
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)


# Guardamos el tiempo antes de usar la recursión.
inicio = time.perf_counter()

# En esta lista guardaremos la serie calculada recursivamente.
serie_recursion = []

# Recorremos las posiciones desde 0 hasta la cantidad indicada.
for i in range(cantidad):

    # Calculamos cada posición con la función recursiva
    # y agregamos el resultado a la lista.
    serie_recursion.append(fibonacci_recursivo(i))

# Guardamos el tiempo cuando termina el cálculo.
fin = time.perf_counter()

# Calculamos el tiempo total del método recursivo.
tiempo_recursion = fin - inicio


# ---------------- MOSTRAR RESULTADOS ----------------

# Mostramos la cantidad de números solicitados.
print("Cantidad de números:", cantidad)

# Mostramos la serie y el tiempo obtenido con el ciclo for.
print("Serie con for:", serie_for)
print("Tiempo con for:", tiempo_for)

# Mostramos la serie y el tiempo obtenido con recursión.
print("Serie con recursión:", serie_recursion)
print("Tiempo con recursión:", tiempo_recursion)