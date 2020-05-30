"""
Faça um programa que calcule o menor numero dívisivel por cada um dos numeros de 1 a 20?
Ex: 2520 é o menor numero divisivel que pode ser dividido por cada um dos numeros de 1 a 10, sem sobrar resto
"""
i = 0
while 1:
    i += 1
    if i % 1 == 0 and i % 2 == 0 and i % 3 == 0 and i % 4 == 0 and i % 5 == 0 and i % 6 == 0 and i % 7 == 0 \
            and i % 8 == 0 and i % 9 == 0 and i % 10 == 0 and i % 11 == 0 and i % 12 == 0 and i % 13 == 0 \
            and i % 14 == 0 and i % 15 == 0 and i % 16 == 0 and i % 17 == 0 and i % 18 == 0 and i % 19 == 0 \
            and i % 20 == 0:
        break

print(f"Menor numero divisivel pelo numeros de 1 a 20: {i}")
