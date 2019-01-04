n = int(input())


fatorial = n
if fatorial == 0:
    fatorial = 1
while n > 1:
    n = n - 1
    fatorial = fatorial * n

print(fatorial)
