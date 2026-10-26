"""Descrição
Faça um programa que exibe a área de um triângulo retângulo a partir da base e da altura fornecidas pelo usuário.

Formato de entrada

Na primeira linha um número inteiro positivo representando a base; na linha seguinte um número inteiro positivo representando a altura.

Formato de saída

Um número inteiro representando a área do triângulo.

NÃO USAR TEXTO NA FUNÇÃO INPUT E PRINT"""

base = int(input())
altura = int(input())

print(f"{(base * altura) / 2:.0f}")