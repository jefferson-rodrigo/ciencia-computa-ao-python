def soma_elementos(lista):
    lista.sort()
    i = 0
    for item in lista:
        i = i + item
    return i
