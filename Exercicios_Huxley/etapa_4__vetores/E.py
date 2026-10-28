"""
Descrição
Faça um programa que lê um vetor de cinquenta números inteiros e exibe, ao final, o menor valor lido.

Formato de entrada

Cinquenta números inteiros, um por linha.

Formato de saída

O menor valor lido dentre os cinquenta.

"""

lista = []

for _ in range (50):

    lista.append(int(input()))

print(min(lista))