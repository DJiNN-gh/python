"""Descrição: Dado um dicionário com produtos e seus respectivos preços, aplique um desconto de 15% em todos os produtos que custem mais de R$ 100,00 e atualize o dicionário diretamente. Em seguida, exiba cada produto e seu novo preço formatado.

Formato de entrada: Leitura de pares de produto e preço até que o nome "fim" seja digitado.

Formato de saída: A relação de produtos e preços atualizados no formato Produto: R$ XX.XX.

Dica Pythonica: Para percorrer e atualizar o dicionário, utilize for produto, preco in dicionario.items(): para desempacotar chave e valor ao mesmo tempo."""

dicio = {}

while True:

    nome = input()

    if nome == "fim":
        break

    preco = float(input())

    dicio.update({nome: preco})

for i, j in dicio:

    if j > 100.00:

        dicio.items(j) = dicio.items(j) * 0.85