"""Descrição: Crie um programa que leia um número inteiro N e, em seguida, receba N números inteiros do usuário. O programa deve gerar e imprimir uma nova lista contendo apenas os quadrados dos números pares informados.

Formato de entrada: Um inteiro N na primeira linha, seguido de N números inteiros (um por linha).

Formato de saída: A lista resultante com os quadrados dos pares.

Dica Pythonica: Evite criar laços for manuais com .append(). Resolva a filtragem e a elevação ao quadrado em uma única linha utilizando List Comprehension com a cláusula if."""

n = int(input())

# Declaração da coleção, como tupla - parêntesis
numeros = ()

for i in range(n):

    # Aqui, criar uma lista que recebe cada input do usuário, anexando cada novo valor ao final
    numeros = int(input())

# Aqui, iterar através de um laço para percorrer a lista
# Erro de estrutura: o contador está iterando de 0 até a quantidade de elementos em numeros
for j in range(numeros):

    # Aqui, testar se o valor atual é par
    if j % 2 == 0:

        # Aqui, imprime o quadrado do valor atual no laço
        print(j * j)