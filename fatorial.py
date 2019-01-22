def fatorial (n):
    fatorial = 1
    print("o fatorial de: ",n," é: ", end = "")
    while n > 1:
        fatorial = fatorial * n
        n = n - 1

    print(fatorial)

x = 1
while True:
    x = int(input("digite um numero: "))
    if(x < 0):
        print("Não existe fatorial para esse número!")
        break
    fatorial(x)
