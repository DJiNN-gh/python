"""Descrição
Faça um programa que mostre um menu com as opções "adição", "subtração", "multiplicação" e "divisão", recebe dois valores reais, a operação escolhida pelo usuário e exibe o resultado da operação sobre os valores.

Formato de entrada

O operador desejado na primeira linha; um número real em outra linha; outro número real em outra linha, conforme modelo de saída.

Formato de saída

1: adicao / 2: subtracao / 3: multiplicacao / 4: divisao

A <nome da operacao> eh: <resultado da operacao>"""

operacao = int(input())
operando_1 = float(input())
operando_2 = float(input())

if operacao == 1:
    print("1: adicao / 2: subtracao / 3: multiplicacao / 4: divisao")
    print(f"A adicao eh: {operando_1 + operando_2:.2f}")
elif operacao == 2:
    print("1: adicao / 2: subtracao / 3: multiplicacao / 4: divisao")
    print(f"A subtracao eh: {operando_1 - operando_2:.2f}")
elif operacao == 3:
    print("1: adicao / 2: subtracao / 3: multiplicacao / 4: divisao")
    print(f"A multiplicacao eh: {operando_1 * operando_2:.2f}")
else:
    print("1: adicao / 2: subtracao / 3: multiplicacao / 4: divisao")
    print(f"A divisao eh: {operando_1 / operando_2:.2f}")