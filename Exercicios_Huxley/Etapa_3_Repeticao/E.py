"""Descrição
[for] Desenvolva um programa que exibe a tabuada de um número natural escolhido pelo usuário. Os múltiplos apresentados devem ser de 1 a 10.

Formato de entrada

Um número natural.

Formato de saída

A saída deve ser a tabuada do número natural dado como entrada, conforme o formato do exemplo."""

n = int(input())

for i in range(10):
    print(f"{n} x {i + 1} = {n * (i + 1)}")