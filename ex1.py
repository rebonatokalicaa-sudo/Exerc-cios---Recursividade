total_elementos = 0

def analisar_numeros(lista):
    global total_elementos
    positivos = 0
    negativos = 0
    zeros = 0
    total_elementos = len(lista)

    for n in lista:
        if n > 0:
            positivos += 1
        elif n < 0:
            negativos += 1
        else:
            zeros += 1

    return positivos, negativos, zeros

numeros = [1, -2, 0, 4, -5, 0]
p, n, z = analisar_numeros(numeros)
print(f"Positivos: {p}, Negativos: {n}, Zeros: {z}, Total: {total_elementos}")
