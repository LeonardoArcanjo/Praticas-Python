"""
Faça um programa que calcule o termo pitagórico a, b, c, para o qual a + b + c = 1000. Um termo pitagórico é um conjunto
de três números naturais, para o qual,
    a² + b² = c²
Por exemplo:
    3² + 4² = 9 + 16 = 25 = 5²
"""
i = 2
a = 0
b = 0
c = 0
while True:
    for j in range(1, i):
        for k in (1, j+1):  # loop de verificacao dos divisores dos numeros 'i' e 'j'
            if j % k == 0 and i % k == 0:  # verifica se j e i sao primos entre si (ou seja, apenas 1 é o fator comum
                # entre eles
                print(f"Fator comum entre {i} e {j}: {k}")
                #  Terno Pitagorico Euclidiano
                """
                a = (i**2) - (j**2)
                b = 2*i*j
                c = (i**2) + (j**2)
                if (a**2) + (b**2) == (c**2):
                    print(f"{a}, {b}, {c} é um terno pitagôrico e a soma deles: {a+b+c}")
                """
        if (a + b + c) >= 1000:
            break
    if (a + b + c) >= 1000:
        break
    i += 1
