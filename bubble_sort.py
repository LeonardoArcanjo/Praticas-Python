"""
Title: Bubble sort
Author: Leonardo Arcanjo
input: A string with numbers
output: A string of ordered numbers
"""


def bubble(lista):
    """
    This function runs the bubble sort algorithm in order to organize a list of numbers in ascending order
    :param lista: string
    :return ordem: string
    """
    lista = lista.split(" ")

    for i in range(len(lista)):
        lista[i] = int(lista[i])

    for i in range(len(lista)):
        for j in range(i, len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = troca(lista[i], lista[j])

    ordem = str(lista)
    return ordem


def troca(num1, num2):
    """
    This function change values of two variables integers
    :param num1: integer
    :param num2: integer
    :return num1, num2: 2 integers
    """
    aux = num2
    num2 = num1
    num1 = aux
    return num1, num2


if __name__ == "__main__":
    numeros = "12 04 23 99 1023 1"
    numeros = bubble(numeros)