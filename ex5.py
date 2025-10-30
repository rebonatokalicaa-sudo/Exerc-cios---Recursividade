def verificar_estoque(lista, indice=0):
    if indice == len(lista):
        return 0

    produto, qtd = lista[indice]
    print(f"Produto: {produto} → {qtd} unidades")

    return qtd + verificar_estoque(lista, indice + 1)

estoque = [("Teclado", 5), ("Mouse", 3), ("Monitor", 2)]
total = verificar_estoque(estoque)
print("Total:", total)
