def buscar_maior(lista):
    if len(lista) == 1:
        return lista[0]
    maior_restante = buscar_maior(lista[1:])
    print(f"Comparando {lista[0]} e {maior_restante}")
    if lista[0] > maior_restante:
        return lista[0]
    else:
        return maior_restante

print("Maior número:", buscar_maior([5, 9, 3, 12, 7]))
