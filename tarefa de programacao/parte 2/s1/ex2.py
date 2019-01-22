def soma_matrizes(m1, m2):
    matriz = []

    m1i = len(m1)
    m1j = len(m1[0])
    m2i = len(m2)
    m2j = len(m2[0])
    if m1i != m2i or m1j != m2j:
        return False
    for i in range(m1i):
        linha = []
        for j in range(m1j):
            linha.append(m1[i][j] + m2[i][j])
        matriz.append(linha)

    return matriz
