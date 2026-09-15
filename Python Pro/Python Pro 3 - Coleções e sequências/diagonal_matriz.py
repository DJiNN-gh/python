"""Descrição: Escreva um programa que leia a dimensão N de uma matriz quadrada N x N e os seus elementos. Em seguida, extraia os elementos da diagonal principal da matriz para uma lista e exiba a soma desses elementos.

Formato de entrada: Um inteiro N seguido dos elementos da matriz linha por linha.

Formato de saída: A lista contendo a diagonal principal e a soma total dos seus valores.

Dica Pythonica: Se matriz é uma lista de listas, você pode extrair a diagonal principal de forma sucinta com a expressão [matriz[i][i] for i in range(N)] e calcular o total com sum()."""

n = int(input())

for i in range(n):

    for j in range(n):

        print(j, end=" ")

    print()