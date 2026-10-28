"""
Descrição
Faça um programa que solicite ao usuário os valores de duas matrizes 6 x 6 e que exibe a matriz resultante da soma dessas matrizes.

Formato de entrada

Para cada uma das 6 primeiras linhas, 6 valores inteiros separados por um espaço, simbolizando os itens da primeira matriz; para cada uma das 6 próximas linhas, 6 valores inteiros separados por um espaço, simbolizando os itens da segunda matriz.

Formato de saída

Seis linhas, cada uma com seis colunas com as respectivas somas separadas por um espaço. Obs.: Não há espaço após o último item de cada linha.
"""

lista = []
matriz_a = []
matriz_b = []

for _ in range(6):

    lista.append(int(input()))

    matriz_a.extend(lista)[_]