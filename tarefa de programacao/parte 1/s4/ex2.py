n = int(input("Digite o valor de n: "))

x = 1
while n > 0:
    if x % 2 != 0:
        n = n - 1
        print(x)
    x = x + 1
