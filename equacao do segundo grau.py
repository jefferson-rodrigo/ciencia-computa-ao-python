print("Calcular raizes de uma equação de segundo grau  (ax² + bx + c = 0). ")
print("digite os valores!")
a = int(input("digite o valor de 'a': "))
b = int(input("digite o valor de 'b': "))
c = int(input("digite o valor de 'c': "))

import math

delta = (b ** 2) - (4 * a * c)

if delta > 0:
    print("Δ = ",delta)
    print("o delta e maior que 0.")
    print("a equação possui duas raízes reais e distintas.")
    resultado1 = (- b + math.sqrt(delta)) / (2 * a)
    resultado2 = (- b - math.sqrt(delta)) / (2 * a)
    print("x'  = ",resultado1)
    print('x"  = ',resultado2)

if delta == 0:
    print("Δ = ",delta)
    print("o delta e igual a 0.")
    print("a equação possui uma raíze real.")
    resultado1 = (- b + math.sqrt(delta)) / (2 * a)

    print("x  =  ",resultado1)


if delta < 0:
    print("Δ = ",delta)
    print("o delta e menor que 0.")
    print("a equação não possui raízes reais")
