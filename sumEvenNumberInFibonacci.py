"""
Faça um programa que some os termos pares da sequencia de fibonacci, cujo os valores não ultrapassem 4 milhões
"""

fibo = 0
ante = 0
aux = 0
soma = 0

while 1:
    if fibo == 0:
        fibo += 1
    elif fibo >= 1:
        aux = fibo
        fibo += ante
        ante = aux
        if fibo % 2 == 0 and fibo < 4000000:
            print(f"{fibo}", end="\t")
            soma += fibo
        elif fibo > 4000000:
            break

print(f"Valor total da soma: {soma}")
