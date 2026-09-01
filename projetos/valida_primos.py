"""Elaborar um programa que recebe um determinado valor informado é primo ou não.
Deve-se considerar a entrada do valor, pois apenas números do conjunto dos natuarais podem ser primos.
"""

# O método serve para calcular se um dado número natural é primo. Caso seja, o retorno é 1, do contrário, o retorno é 0.
def validaPrimo (valor):
    cont_i = valor - 1

    if valor == 2:
        return True
    elif valor == 0 or valor == 1:
        return False
    else:
        while cont_i >= 2:
            if valor % cont_i == 0:
                return False
            cont_i -= 1
        return True

val_i = int(input("Informe um número natural: "))

if validaPrimo(val_i) == False:
    print("Não-primo")
else:
    print("Primo")