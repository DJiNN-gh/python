"""Enunciado: Desenvolva um programa que solicite uma string qualquer ao usuário. O programa deve percorrer cada caractere e calcular a soma total de seus códigos numéricos correspondentes na tabela ASCII.
Entrada: Uma string (ex: "Python").
Saída: Um número inteiro representando a soma total.
Dica Pythonica: Lembre-se que strings são sequências (assim como listas e tuplas). Em vez de usar um contador para acessar cada posição, use o padrão idiomático for char in string:. Para obter o valor ASCII de um caractere, utilize a função embutida ord()."""

string = "Python"

for char in string:
    