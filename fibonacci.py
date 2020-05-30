"""
Leia um número positivo do usuário, então, calcule e imprima a sequencia de fibonacci até o primeiro número superior
ao número lido. Exemplo: se o usuário informou o número 30, a sequencia a ser impressa será 0 1 1 2 3 5 8 13 21 34
"""

num = int(input("Digite um número: "))

fibo = 0
ante = 0
aux = 0
while 1:
    print(f"{fibo}", end="\t")
    if fibo > num:
        break
    elif fibo == 0:
        fibo += 1
    elif fibo >= 1:
        aux = fibo
        fibo = fibo + ante
        ante = aux
