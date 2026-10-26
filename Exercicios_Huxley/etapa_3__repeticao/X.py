"""Descrição
[while] Uma empresa está fazendo uma pesquisa, ligando para telespectadores e perguntando qual canal de televisão (4, 5 ou 9) eles estão assistindo. A cada ligação a resposta é registrada em um software. No final do dia, alguém digita zero e os canais com seus respectivos votos são exibidos em ordem decrescente. Construa esse software. Obs.: Considere que não haverá empate.

Formato de entrada

Diversos números naturais, representando o canal que o telespectador está assistindo.

Formato de saída

Os canais válidos com suas respectivas quantidades de votos, conforme exemplo."""

valor = 0
canal4 = 0
canal5 = 0
canal9 = 0

while True:
    valor = int(input())

    if valor == 4:
        canal4 += 1
    elif valor == 5:
        canal5 += 1
    elif valor == 9:
        canal9 += 1
    elif valor == 0:
        break

if canal4 >= canal5 and canal4 >= canal9:
    print(f"canal 4: {canal4}")
    if canal5 >= canal9:
        print(f"canal 5: {canal5}")
        print(f"canal 9: {canal9}")
    else:
        print(f"canal 9: {canal9}")
        print(f"canal 5: {canal5}")
elif canal5 >= canal4 and canal5 >= canal9:
    print(f"canal 5: {canal5}")
    if canal4 >= canal9:
        print(f"canal 4: {canal4}")
        print(f"canal 9: {canal9}")
    else:
        print(f"canal 9: {canal9}")
        print(f"canal 4: {canal4}")
else:
    print(f"canal 9: {canal9}")
    if canal4 >= canal5:
        print(f"canal 4: {canal4}")
        print(f"canal 5: {canal5}")
    else:
        print(f"canal 5: {canal5}")
        print(f"canal 4: {canal4}")