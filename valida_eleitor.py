"""Enunciado: Escreva um programa que receba a idade de um cidadão e verifique se ele se enquadra na faixa de voto obrigatório (entre 18 e 70 anos, inclusive).
Entrada: Um número inteiro.
Saída: "Voto Obrigatório" ou "Voto Não Obrigatório".
Dica Pythonica: Python permite comparações encadeadas (Lutz, Capítulo 5). Em vez de idade >= 18 and idade <= 70, você pode escrever de forma elegante e matemática: if 18 <= idade <= 70:. É o código expressando exatamente o que a lógica pede."""

idade = int(input("Insira sua idade: \n"))

if idade >= 18 and idade <= 70:
    print("Voto obrigatório")
else:
    print("Voto não-obrigatório")