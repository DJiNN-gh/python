"""Descrição
Faça um programa que lê o salário base de alguém e exibe o novo salário, considerando 5% de gratificação (mais dinheiro) e 7% de impostos (menos dinheiro) sobre o salário base. Também exiba a gratificação e o imposto.

Formato de entrada

A entrada conterá um valor real representando o salário base.

Formato de saída

A saída deverá conter um valor real com duas casas decimais representando o novo salário; um valor real com duas casas decimais representando a gratificação e; um valor real com duas casas decimais representando o imposto. Apenas um valor por linha.

NÃO USAR TEXTO NA FUNÇÃO INPUT E PRINT"""

"""def calculaSalario (valor):
    gratificacao = (valor + (valor * 0.05))
    imposto = (valor - (valor * 0.07))
    novo_salario = gratificacao - imposto"""

salario = float(input())

gratificacao = (salario * 0.05)
imposto = (salario * 0.07)
novo_salario = ((salario + gratificacao) - imposto)

print(f"novo: {novo_salario:.2f}")
print(f"gratificacao: {gratificacao:.2f}")
print(f"imposto: {imposto:.2f}")