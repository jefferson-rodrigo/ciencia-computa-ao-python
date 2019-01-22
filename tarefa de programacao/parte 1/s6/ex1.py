def computador_escolhe_jogada(n, m):
    jogada = 1
    while n - jogada >= 0 and (n - jogada) % (m + 1) != 0 and jogada < m:
        jogada = jogada + 1

    print("O computador tirou ",jogada," peça.")
    return jogada

def usuario_escolhe_jogada(n, m):
    jogada = int(input("Quantas peças você vai tirar? "))
    while jogada < 1 or jogada > m:
        print("Oops! Jogada inválida! Tente de novo.")
        jogada = int(input("Quantas peças você vai tirar? "))

    print("Você tirou ",jogada," peça.")
    return jogada

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    if n % (m + 1) != 0:
        print("Computador começa!")
        jogada = computador_escolhe_jogada(n, m)
        n = n - jogada
        if n == 0:
            print("Fim do jogo! O computador ganhou!")
            return 2
        else:
            print("Agora restam ",n," peças no tabuleiro.")
    else:
        print("Voce começa!")

    while n > 0:
        jogada = usuario_escolhe_jogada(n, m)
        n = n - jogada
        if n == 0:
            print("Fim do jogo! Você ganhou!")
            return 1
        else:
            print("Agora restam ",n," peças no tabuleiro.")

        jogada = computador_escolhe_jogada(n, m)
        n = n - jogada
        if n == 0:
            print("Fim do jogo! O computador ganhou!")
            return 2
        else:
            print("Agora restam ",n," peças no tabuleiro.")

    return 0

def campeonato():
    pcomputador = pvoce = 0
    i = 1
    while i <= 3:
        print("**** Rodada ",i," ****")
        if(partida() == 1):
            pvoce = pvoce + 1
        else:
            pcomputador = pcomputador + 1
        i = i +1
    print("**** Final do campeonato! ****")
    print("")
    print("Placar: Você ",pvoce," X ",pcomputador," Computador")

    return



print("Bem-vindo ao jogo do NIM! Escolha:")
print("")
print("1 - para jogar uma partida isolada")
c = int(input("2 - para jogar um campeonato "))
print("")
if c == 1:
    print("Voce escolheu uma partida!")
    partida()

else:
    if c == 2:
        print("Voce escolheu um campeonato!")
        campeonato()

    else:
        print("escolha inválida! ")
