"""
Descrição
Faça um programa que exibe a média entre o maior e o menor valor de um vetor de inteiros com vinte elementos dados pelo usuário e, ao final, exibe apenas os elementos que são maiores que a média.

Formato de entrada

Vinte números inteiros, um por linha.

Formato de saída

Na primeira linha, a frase "media: #" (sem aspas, em minúsculo, sem acentuação e com # substituído pela média dos números lidos e com duas casas decimais); nas linhas seguintes, os valores dados na entrada que sejam maiores do que a média, na mesma sequência que foram lidos e um por linha.
"""

lista = []

for _ in range(20):

    lista.append(int(input()))

media = (max(lista) + min(lista)) / 2

print(f"media: {media:.2f}")

for _ in lista:

    if _ > media:

        print(_)