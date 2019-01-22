l = int(input("digite a largura: "))
a = int(input("digite a altura: "))

y = 1
while y <= a:
    x = 1
    while x < l:
        
        print("#" ,end = "")
        x = x + 1
    print("#" ,end = "\n")
    y = y + 1
