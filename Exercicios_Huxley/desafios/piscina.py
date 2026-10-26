"""Descrição
Em um determinado condomínio os moradores decidiram elaborar regras para uso da piscina. Como a procura pela piscina é maior por parte das crianças, o que muitas vezes acaba tumultuando muito o ambiente, foi decidido limitar a quantidade de crianças ao mesmo tempo nesse espaço.

Logo, para cada usuário ou grupo de usuários utilizar a piscina é preciso informar a quantidade de adultos e crianças que desejam acessar o espaço, assim como a quantidade de crianças convidadas (que são outras crianças familiares ou amigos(as) dos residentes).

Para facilitar o acesso, o síndico lhe contratou para desenvolver um programa que ajude os moradores a saberem se poderão acessar à piscina, logo na entrada do espaço.

Então, faça um programa que receba a quantidade máxima de crianças (independentemente se moradoras e/ou convidadas) que será permitido para utilizar a piscina, as quantidades de cada categoria de pessoas (adultos, crianças e convidados) e informe se está liberada a entrada ou não.

Observações:

Uma questão importante é que, para não ficar chato com crianças de fora, se tiver convidados entre as pessoas que desejam usar a piscina, o grupo será liberado para acessar o espaço, mesmo tendo mais crianças do que o limite preestabelecido;
Caso a capacidade máxima de crianças tenha sido alcançada, e chegar um grupo de adultos com crianças, considere que ninguém será liberado para entra no espaço da piscina.
"""

# Início
# Declaração de variáveis
adultos = 0
acc_adultos = 0
criancas = 0
acc_criancas = 0
convidados = 0
acc_convidados = 0

lim_criancas = int(input())

while True:

    adultos = int(input())

    if adultos < 0:

        break

    criancas = int(input())
    convidados = int(input())

    if (acc_criancas + acc_convidados + criancas + convidados) >= lim_criancas and convidados > 0:
        print("Acesso permitido devido a presenca de convidado(s).")
        print(f"Adultos na piscina: {acc_adultos:d}")
        print(f"Criancas na piscina: {(acc_criancas + acc_convidados):d}")
        print("***")
        acc_adultos += adultos
        acc_criancas += criancas
        acc_convidados += convidados

    elif (acc_criancas + acc_convidados + criancas + convidados) >= lim_criancas:
        print("Capacidade maxima de criancas atingida/excedida.")
        print(f"Tem {((acc_criancas + acc_convidados) - lim_criancas):d} crianca(s) a mais do que as {lim_criancas:d} permitidas.")
        print(f"Adultos na piscina: {acc_adultos:d}")
        print(f"Criancas na piscina: {(acc_criancas + acc_convidados):d}")
        print("***")

    else:
        print("Acesso permitido!")
        print(f"Adultos na piscina: {acc_adultos:d}")
        print(f"Criancas na piscina: {(acc_convidados + acc_criancas):d}")
        print("***")
        acc_adultos += adultos
        acc_criancas += criancas
        acc_convidados += convidados