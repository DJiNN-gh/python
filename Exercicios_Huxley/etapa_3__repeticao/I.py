"""Descrição
[for] Faça um programa que exibe n^m (n elevado a m), considerando n (real) e m (natural) dados pelo usuário. Não usar funções prontas da linguagem para o cálculo de potência.

Formato de entrada

Na primeira linha um número real, simbolizando a base da potência; na linha seguinte um número natural representando o expoente.

Formato de saída

A potência da base pelo expoente, com duas casas depois do ponto.

"""
base = 0
expoente = 0
total = 1

base = float(input())
expoente = int(input())

for _ in range(expoente):
    total *= base

print(f"{total:.2f}")