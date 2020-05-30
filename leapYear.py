"""
Determine se um determinado ano lido é bissexto. Sendo que um ano é bissexto se for divísível por 400 ou se for
por 4 e não for divisível por 100. Por exemplo: 1988, 1992, 1996
"""

ano = int(input("Digite o ano desejado: "))

if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
    print(f"o ano {ano} é bissexto!")
else:
    print(f"o ano {ano} não é bissexto!")
