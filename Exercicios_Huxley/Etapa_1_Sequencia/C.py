"""Descrição
Faça um programa que lê o salário atual de alguém e exibe o novo salário, que é o atual com 25% de aumento.

Formato de entrada

Um número real representando o salário atual.

Formato de saída

Um número real com duas casas decimais, representando o salário atual com o aumento.

NÃO USAR TEXTO NA FUNÇÃO INPUT"""

def calculaAumento (valor):
    novoValor = (valor + (valor * 0.25))
    return novoValor

salario = float(input())

#print("O seu salário com aumento é de R$ ", round(calculaAumento(salario), 2))
print(f"O seu salário com o aumento é de R$ {calculaAumento(salario):.2f}")