numero = int(input("digite um numero: "))

soma = 0
temp = 0

while numero != 0:
    soma = soma + numero % 10
    numero = numero // 10


print("a soma dos numeros digitados e: ", soma)
