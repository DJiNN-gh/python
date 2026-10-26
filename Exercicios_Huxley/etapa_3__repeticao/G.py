"""Descrição
[for] Faça um programa que lê um número natural e exibe o fatorial desse número. Lembre-se: 5! é 120, porque 5 * 4 * 3 * 2 * 1 = 120. Use um acumulador e um contador dentro de um laço de repetição.

Formato de entrada

Um número natural.

Formato de saída

O fatorial do número dado como entrada."""

acc = 1

n = int(input())

for i in range(n):
    acc *= (i+1)

print(f"{acc}")