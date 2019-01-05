def maior_primo(n):
    while n >= 2:
        if e_primo(n):
            return n
        n = n - 1

def e_primo(n):
    i = 2
    while i < n:
        if (n % i) == 0:
            return False
        i = i + 1
    return True
