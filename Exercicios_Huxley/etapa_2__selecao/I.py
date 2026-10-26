"""Descrição
Faça um programa que recebe o valor de três arestas (número inteiro) e exibe uma mensagem indicando se podem formar um triângulo. Em caso afirmativo, indique se ele é equilátero, isósceles ou escaleno. Lembre-se: Para que um triângulo exista, a medida de qualquer um dos lados deve ser menor que a soma das medidas dos outros dois.

Formato de entrada

3

4

5

Formato de saída

podem formar um triangulo

escaleno"""

lado_a = int(input())
lado_b = int(input())
lado_c = int(input())

#primeiro teste (critico): valida se é um triângulo
if lado_a + lado_b <= lado_c or lado_a + lado_c <= lado_b or lado_b + lado_c <= lado_a:
    print("nao podem formar um triangulo")
#segundo teste (equilátero)
elif lado_a == lado_b and lado_b == lado_c:
    print("podem formar um triangulo")
    print("equilatero")
#terceiro teste (escaleno)
elif lado_a != lado_b and lado_a != lado_c and lado_b != lado_c:
    print("podem formar um triangulo")
    print("escaleno")
else:
    print("podem formar um triangulo")
    print("isosceles")