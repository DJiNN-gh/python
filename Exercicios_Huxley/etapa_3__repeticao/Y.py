"""Descrição
[while] Certa pessoa (A) possui R$ 10.000,00 e tem sua fortuna crescendo em R$ 100,00 por mês. Outra pessoa (B) tem sua fortuna crescendo em R$ 300,00 ao mês e possui R$ 5.000,00. Faça um programa que exibe, mês a mês, a diferença das duas fortunas até que a pessoa (B) tenha mais dinheiro do que a pessoa (A).

Formato de entrada

Esse programa não possui entrada de dados.

Formato de saída

Em cada linha a diferença da fortuna da pessoa (A) em relação à pessoa (B). Vide exemplo."""

fort_a = 10000.00
fort_b = 5000.00

while fort_a >= fort_b:
    print(f"{(fort_a - fort_b):.2f}")
    fort_a += 100
    fort_b += 300