"""Descrição
Faça um programa que recebe duas datas distintas e exibe a mais recente, ou seja, aquela que está mais próxima da data atual. Considere apenas datas passadas, isto é, nenhuma das datas representará um momento futuro.

Cada data deve ser fornecida como três valores inteiros, onde o primeiro representa o dia, o segundo o mês e o terceiro o ano. Dica: comece verificando pelo ano, depois pelo mês e, se necessário, por último pelo dia.

Formato de entrada

12 05 2018

11 05 2018

Formato de saída

12 05 2018

"""

# Método de teste: ano, então mês, então ano

# Declaração de variáveis
# Primeira data
dia_a, mes_a, ano_a = map(int, input().split())
# Segunda data
dia_b, mes_b, ano_b = map(int, input().split())

"""
if ano_a > ano_b:
    print(f"{dia_a} {mes_a:02d} {ano_a}")
elif ano_b > ano_a:
    print(f"{dia_b} {mes_b:02d} {ano_b}")
elif mes_a > mes_b:
    print(f"{dia_a} {mes_a:02d} {ano_a}")
elif mes_b > mes_a:
    print(f"{dia_b} {mes_b:02d} {ano_b}")
elif dia_a > dia_b:
    print(f"{dia_a} {mes_a:02d} {ano_a}")
else:
    print(f"{dia_b} {mes_b:02d} {ano_b}")

"""
data_a = (dia_a, mes_a, ano_a)
data_b = (dia_b, mes_b, ano_b)

if data_a > data_b:
    print(f"{dia_a} {mes_a:02d} {ano_a}")
else:
    print(f"{dia_b} {mes_b:02d} {ano_b}")