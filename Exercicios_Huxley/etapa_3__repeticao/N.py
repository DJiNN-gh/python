"""Descrição
[for] Sendo H = 1 + (1/2) + (1/3) + (1/4) + (1/5) + ... + (1/n), faça um programa que exibe o valor de H após ler n (n > 0). Observação: use uma variável de ponto flutuante de precisão dupla (double).

Formato de entrada

Um valor natural simbolizando n.

Formato de saída

Um valor real, com duas casas decimais, simbolizando H."""

n = int(input())

H = 0

for i in range(1, n+1):

    H += (1 / i)

print(f"{H:.2f}")