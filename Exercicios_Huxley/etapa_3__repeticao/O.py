"""[while] Faça um programa que recebe valores inteiros positivos até que seja digitado o valor zero, que não deverá ser contabilizado. O programa deverá exibir o maior valor lido.

Formato de entrada

Diversos valores inteiros positivos, um por linha. A entrada é encerrada com a leitura do valor zero (que não deve ser contabilizado).

Formato de saída

O maior valor lido."""

valor = 0
maior = -1

while True:

    valor = int(input())
    
    if valor > maior:
        maior = valor

    if valor == 0:
        break

print(f"{maior}")