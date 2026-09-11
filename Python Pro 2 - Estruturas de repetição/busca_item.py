"""Enunciado: Defina uma lista de produtos fixa (ex: ['caneta', 'lápis', 'borracha']). Peça ao usuário o nome de um item e percorra a lista:
Se encontrar o item, exiba "Item disponível" e interrompa a busca.
Se percorrer toda a lista sem sucesso, utilize a cláusula else do loop para exibir "Item não encontrado".
Entrada: Nome do produto (string).
Saída: Confirmação de presença ou aviso de ausência.
Dica Pythonica: Este padrão substitui o antigo idioma "Search-and-Flag" (comum em C), onde você criaria uma variável como encontrou = False. Ao usar o else do próprio loop, você escreve um código mais eficiente e alinhado à filosofia de Lutz de reduzir o estado mutável do programa."""

# Declaração de uma tupla, onde os objetos estão dispostos em sequência dentro de uma variável e são imutáveis
colecao = "mouse", "teclado", "monitor", "mousepad", "flashdrive", "cartão SD", "microfone", "headphone"

# Imprimindo a tupla em tela para informar as opções ao usuário
print(colecao)

item = input("Informe um item para pesquisar: ")

# Laço que percorre toda a tupla, a partir de um atualizador, que recebe cada elemento da tupla por iteração do laço
for cont in colecao:
    # Caso o valor inserido seja encontrado, isto é, for igual ao elemento da tupla na posição atual da iteração, imprime e encerra o laço
    if item == cont:
        print(cont, end="\n")
        break
# Usa-se uma cláusula else ao final do laço, informando que, ao encerrar o laço e a cláusula if anterior não tenha sido atendida, faça a impressão
else:
    print("Item não encontrado")