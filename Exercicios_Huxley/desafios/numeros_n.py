"""Descrição
Leia uma sequência de 1000 inteiros.

Leia outro inteiro N, e seu programa deve imprimir quantas vezes o inteiro N aparece nos 1000 anteriores.

O programa para quando o primeiro inteiro dos 1000 for igual a -1."""

# Início
# Declaração de variáveis
n = []
aux = 0
acc = 0

for i in range(1000):

    aux = int(input())

    if aux == -1:

        break

    else:

        n.append(aux)

N = int(input())

for j in n:

    if N == j:

        acc += 1

print(f"{N} appeared {acc} times")