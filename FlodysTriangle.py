"""
Escreva um programa que leia um número inteiro positivo 'n' e em seguida imprima 'n' linhas do chamado
Triângulo de Floyd. Para n = 6:
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 20 21
"""
n = int(input("Digite o valor de n: "))
contagem = 1

for i in range(1, n+1):  # loop for para as linhas
    for j in range(1, i+1):
        print(f"{contagem:2d} ", end=' ')
        contagem += 1
    print("")  # serve pra pular uma linha, se colocar "\n" pula duas linhas, porque o print() já tem como argumento
    # '\n' no parâmetro 'end='
