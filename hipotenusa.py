"""Desenvolver um programa que calcule a hipotenusa de um triângulo retângulo qualquer, padronizando a entrada de dados em mm (milímetros) e a saída também em mm (milímetros)"""
INDICE = 2

def calculaHipotenusa (catOp, catAdj):
    quadHip_f = (catOp ** INDICE) + (catAdj ** INDICE)
    return quadHip_f ** (1/INDICE)

catOp_f = float(input("Informe o valor do cateto oposto: "))
catAdj_f = float(input("Informe o valor do cateto adjacente: "))

print(calculaHipotenusa(catOp_f, catAdj_f))