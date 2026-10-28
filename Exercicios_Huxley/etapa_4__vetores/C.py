"""
Descrição
Faça um programa que preenche um vetor com cinquenta elementos inteiros e altera todo valor negativo para seu oposto positivo, ao final o programa deve exibir o vetor já modificado.

Formato de entrada

Cinquenta números inteiros, um por linha.

Formato de saída

Os cinquenta números inteiros dados na entrada, na mesma sequência, em que todo negativo torna-se positivo.
"""

lista = []

for _ in range(50):

    lista.append(int(input()))

    if lista[_] < 0:
        
        lista.append(lista.pop(_) * -1)

for _ in lista:

    print(_)