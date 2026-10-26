"""Descrição
Faça um programa que recebe dois números inteiros distintos e exibe o maior.

Formato de entrada

Um número inteiro na primeira linha; um número inteiro na segunda linha.

Formato de saída

O maior dos números."""

num_1 = int(input())
num_2 = int(input())

# Nenhua solução especial para valores iguais foi estabelecida
if num_1 > num_2:
    print(num_1)
else:
    print(num_2)