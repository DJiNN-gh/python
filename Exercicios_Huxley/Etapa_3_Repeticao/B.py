"""Descrição
[while] Elabore um programa que recebe valores inteiros até que seja digitado o valor zero. O programa deverá exibir a média aritmética dos valores recebidos. Lembre-se: o valor zero apenas sinaliza o fim da entrada, não deve ser contabilizado.

Obs.: Não existe média sem que pelo menos um valor seja dado antes do zero, portanto neste problema ESTÁ GARANTIDO QUE HÁ MÉDIA.

Formato de entrada

Diversos valores inteiros, um por linha. A entrada é encerrada com a leitura do valor zero.

Formato de saída

A média aritmética dos valores lidos, não considerando o zero que encerra a entrada."""

acc = 0
cont = 0

while True:
    n = int(input())

    if n == 0:
        break
    
    acc += n
    cont += 1

print(f"{(acc / cont):.0f}")