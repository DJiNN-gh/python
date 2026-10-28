"""
Descrição
Faça um programa que preenche um vetor com 10 números inteiros dados pelo usuário e, ao final, exibe os itens do vetor em ordem contrária à da entrada.

Formato de entrada

Uma sequência de dez números inteiros, um por linha.

Formato de saída

A sequência de números inteiros dada na entrada, um número por linha, por em ordem contrária.

"""

lista = []

for _ in range(10):

    lista.append(int(input()))

lista.reverse()

for _ in lista:

    print(_)