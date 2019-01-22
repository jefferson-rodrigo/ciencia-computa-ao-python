i = 1
lista = []
while i > 0:
    i = int(input("Digite um número: "))
    lista.append(i)
lista.pop()
while len(lista) > 0:
    print(lista.pop())
