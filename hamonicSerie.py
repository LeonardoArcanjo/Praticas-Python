"""
Em matemática, o número hamônico designado por H(n) define-se como sendo a soma da serie hamônica:
    H(n) = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n
Faça um programa que leia um valor 'n' inteiro e positivo e apresente o valor de H(n)
"""

n = int(input("Digite o valor de n: "))

h_n = 0
for i in range(1, n+1):  # A interação deve ir até 'n' como na fórmula, assim declara n+1 como valor final em range()
    h_n += 1/i          # formula de iteração, onde H(n) = H(n) + 1/i

print(f"Valor do numero harmonico H(n): {h_n}")
