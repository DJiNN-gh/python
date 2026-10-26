"""Descrição
Faça um programa que recebe a idade de um nadador e exibe a categoria que ele pertence. Sendo o critério: "infantil" (0 a 10 anos); "junior" (11 a 14 anos); "adolescente" (15 a 20 anos); "jovem" (21 a 35 anos) e; "master" (> 35 anos). 

Formato de entrada

Um número inteiro representando a idade de um nadador.

Formato de saída

A categoria a que o nadador pertence."""

idade = int(input())

if idade > 0 and idade < 11:
    print("infantil")
elif idade > 10 and idade < 15:
    print("junior")
elif idade > 14 and idade < 21:
    print("adolescente")
elif idade > 20 and idade < 36:
    print("jovem")
else:
    print("master")