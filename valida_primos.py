"""Elaborar um programa que recebe um determinado valor informado é primo ou não.
Deve-se considerar a entrada do valor, pois apenas números do conjunto dos natuarais podem ser primos.
"""

def validaPrimo (primo):
    cont_i = primo - 1

    if primo == 2:
        return 1
    elif primo == 0 | primo == 1:
        return 0
    else:
        while (cont_i > 2):
            if (primo % 1 == 0):
                return 0
            cont_i -= 1
        return 1

val_i = int(input("Informe um número inteiro: "))

if validaPrimo(val_i) == 0:
    print("Não-primo")
else:
    print("Primo")