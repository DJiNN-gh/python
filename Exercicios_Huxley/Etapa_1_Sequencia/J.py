"""Descrição
Faça um programa que recebe duas notas e exibe a média ponderada dessas notas, considerando peso dois para a primeira e peso três para a segunda.

Formato de entrada

Na primeira linha haverá um número real representando a primeira nota; na linha seguinte haverá um número real representando a segunda nota.

Formato de saída

Deverá ser um valor real com duas casas decimais simbolizando a média ponderada.

NÃO USAR TEXTO NA FUNÇÃO INPUT E PRINT"""

nota1 = float(input())
nota2 = float(input())

print(f"{((((nota1 * 2) + (nota2 * 3)) / (2 + 3))):.2f}")