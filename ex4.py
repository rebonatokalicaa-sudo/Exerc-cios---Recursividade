import time

def fibonacci_recursivo(n):
    if n <= 1:
        return n
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

def fibonacci_iterativo(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

n = 30
inicio = time.time()
print("Recursivo:", fibonacci_recursivo(n))
print("Tempo recursivo:", round(time.time() - inicio, 4), "s")

inicio = time.time()
print("Iterativo:", fibonacci_iterativo(n))
print("Tempo iterativo:", round(time.time() - inicio, 4), "s")
