"""
Faça um programa que calcule o maior numero palindromo feito a partir do produto de dois numeros de 3 digitos.
Ex: O maior palíndromo foi feito a partir do produto de dois números de dois digitos é 9009 = 91 * 99
"""
maior = 0
numero = 0
palindro = 0
p1 = 0
p2 = 0
for i in range(100, 1000):  # loop for para varrer todos os números com 3 digitos
    for j in range(100, 1000):  # loop for para multiplicar todos os numeros de 3 digitos
        numero = i * j  # Multiplica os números
        palindro = str(numero)  # converte o numero numa string
        palindro = palindro[::-1]  # Inverte a string
        if str(numero) == palindro:  # compara as strings do numero e do palindro pra ver se são palidromos
            if numero > maior:  # caso numero seja, verifica se ele é maior que o palindromo salvo anteriormente
                maior = numero
                p1 = i
                p2 = j

print(f"O numero palidromo: {maior} = {p1} * {p2}")
