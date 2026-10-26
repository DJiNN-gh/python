"""Descrição
Faça um programa que lê o salário atual de alguém e exibe o novo salário, que é o atual com 25% de aumento.

Formato de entrada

Um número real representando o salário atual.

Formato de saída

Um número real com duas casas decimais, representando o salário atual com o aumento.

NÃO USAR TEXTO NA FUNÇÃO INPUT E PRINT"""

"""def calculaAumento (valor):
    novoValor = (valor + (valor * 0.25))
    return novoValor"""

salario = float(input())

print(f"{salario*1.25:.2f}")
#print(f"O seu salário com o aumento é de R$ {float(input("Seu salário]"))*1.25:.2f}")