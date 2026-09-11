"""Descrição
[for] Faça um programa que lê cem idades de pacientes e exibe as idades do mais novo e do mais velho.

Formato de entrada

Cem números naturais, simbolizando as idades de pacientes, um por linha.

Formato de saída

Na primeira linha a idade do mais novo; na linha seguinte a idade do mais velho."""

menor = 1000
maior = 0

for i in range(1, 101):

    idade = int(input())

    if idade > maior:
        maior = idade

    if idade < menor:
        menor = idade

print(f"mais novo: {menor}")
print(f"mais velho: {maior}")