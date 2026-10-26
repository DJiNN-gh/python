"""
Uma Lista é uma coleção de dados que são ordenados por índices e são mutáveis. Permite elementos duplicados.
Uma Tupla é uma coleção de dados que são ordenados por índices e são imutáveis. Permite elementos duplicados.
Um Conjunto é uma coleção de dados que não são ordenados, imutáveis e que não possuem indexação. Não permite elementos duplicados.
Um Dicionário é uma coleção de dados que são ordenados por chaves e são mutáveis. Não permite elementos duplicados.

Elementos de um Conjunto podem ser removidos, assim como novos elementos podem ser adicionados a ele, porém os seus elementos não podem ser alterados.
"""

# Exemplo de list comprehension

# Para declarar uma Lista, usa-se como estrutura da declaração os caracteres colchetes [] para conter os elementos da Lista
# Declarando uma Lista
perifericos = ["mouse", "teclado", "monitor"]

# Copiando a lista, item a item, para uma outra variável/conjunto de dados
lista = [i for i in perifericos]

# Imprimindo toda a lista
print(lista)

# Imprimindo o tamanho da lista
print(len(lista))

# Removendo o último item da lista; o item removido é retornado e pode ser impresso ou atribuído
print(perifericos.pop())

# Imprimindo a lista após a remoção
print(perifericos)

# Imprimindo o tamanho da lista após a remoção
print(len(lista))


# Para declarar uma Tupla, usa-se como estrutura da declaração os caracteres parêntesis () para conter os elementos da Tupla
# Declarando uma Tupla
carros = ("Corolla", "Cobalt", "Civic")

# Inserindo valores de uma tupla em outra
tupla = [j for j in carros]

print(tupla)

print(len(tupla))


# Para declarar um Conjunto, usa-se como estrutura da declaração os caracteres chaves {} para conter os elementos do Conjunto
# Declarando um Conjunto
marcas = {"Apple", "Microsoft", "IBM"}

# Inserindo valores de um conjunto em outro
conjunto = [k for k in marcas]

print(conjunto)

print(len(conjunto))


# Para declarar um Dicionário, usa-se como estrutura da declaração os caracteres chaves {} para conter os elementos do Dicionário, onde cada elemento deve, impreterivelmente, ser associado a uma chave correspondente
# Declarando um Dicionário
caes = {"Labrador":1, "Dachsund":2, "Dálmata":3}

# Inserindo um novo elemento no dicionário
#caes = ["Poodle":4]

# Funções úteis

"""
Para determinar qual é o maior valor de um conjunto de dados, usa-se a função max(), passando como referência o conjunto de dados a ser analisado.

Para determinar qual é o menor valor de um conjunto de dados, usa-se a função min(), passando como referência o conjunto de dados a ser analisado.

Para somar os valores de um conjunto de dados, usa-se a função sum(), passando como referência apenas o conjunto de dados a ser somado (não funciona com tipos string).

Para calcular o tamanho de um conjunto de dados, usa-se a função len(), passando como referência apenas o conjunto de dados a ser medido.

Para adicionar elementos ao final de um conjunto de dados, usa-se a função append(), passando como referência o elemento a ser adicionado, com a função ao final da chamada do conjunto de dados.

Para adicionar um conjunto de dados a um outro conjunto de dados, usa-se a função extend(), passando como referência o conjunto de dados a ser concatenado, com a função ao final da chamada do conjunto de dados original.

Para verificar se um dado elemento está contido em um conjunto de dados, usa-se a função in(), com a estrutura-exemplo 3 in L = [1, 2, 3].

Para ordenar os elementos de um conjunto de dados, usa-se a função sort(), passando como referência o conjunto de dados a ser ordenado.

Para inverter os elementos de um conjunto de dados, usa-se a função reverse(), passando como referência o conjunto de dados a ser invertido.

Para remover um elemento de um conjunto de dados, usa-se a função pop(), passando como referência o conjunto de dados a ser atualizado.

Para criar listas a partir de intervalos, usa-se a função list(), passando como referência a função range(), por exemplo, e atribuindo o resultado a uma variável/conjunto de dados.

deque()

Para remover um item de um dicionário através de uma chave, usa-se a função del(), passando como referência a chave do elemento, ao final do chamada da variável/conjunto de dados.

Para exibir todas as chaves de um dicionário, usa-se a função keys(), passando como referência a variável/conjunto de dados a ser analisado.
"""