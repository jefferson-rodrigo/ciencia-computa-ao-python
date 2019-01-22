def remove_repetidos(lista):
    lista.sort()
    i = 0
    while i < len(lista) - 1:
        if lista[i] == lista[i+1]:
            lista.pop(i)
        else:
            i = i + 1
    return lista
