"""Descrição
Uma empresa decide presentear seus funcionários com um bônus de Natal. O valor é definido como segue: 

(a) 20% do salário para os funcionários homens com mais de quinze anos de casa;

(b) 25% do salário para as funcionárias mulheres com mais de dez anos de casa;

(c) R$ 200,00 para os demais que não se encaixaram nas categorias anteriores. 

Elabore um programa que recebe o sexo, o tempo de casa e o salário de um funcionário e exibe o valor total que o funcionário receberá no Natal (salário + bônus).

Formato de entrada

h

16

1000.00

Formato de saída

1200.00"""

sexo = input()
tempo = int(input())
salario = float(input())

# Caso A: homem com mais de quinze anos de casa
# Caso B: mulher com mais de dez anos de casa
# Caso C: todos os outros

if sexo == 'h' and tempo >= 15:
    print(f"{salario + (salario * 0.2):.2f}")
elif sexo == 'm' and tempo >= 10:
    print(f"{salario + (salario * 0.25):.2f}")
else:
    print(f"{salario + 200:.2f}")