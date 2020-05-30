"""Faça um programa para converter uma letra maiuscula em minuscula. Use a Tabela ASCII para resolver o problema"""

letra = input("Digite uma letra maiúscula: ")

maiuscula = ord(letra) # converte a string no decimal (inteiro), segundo a tabela ASCII, correspondente

minuscula = maiuscula + 32 # soma com 32, onde começa as letras minusculas

# a funcao chr converte o argumento (inteiro) no seu correspondente na tabela ASCII
print(f"Letra minuscula correspondente: {chr(minuscula)}")

