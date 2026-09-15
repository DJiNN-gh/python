"""Enunciado: Peça um número inteiro ao usuário (a altura do triângulo). O programa deve imprimir um triângulo de números onde cada linha i contém a sequência de 1 até i.
Exemplo de Saída (para entrada 3):
1
1 2
1 2 3
Entrada: Um número inteiro.
Saída: O padrão numérico triangular.
Dica Pythonica: Aqui, a lógica é dependente: o limite do range() do loop interno (colunas) deve ser definido dinamicamente pelo valor atual do loop externo (linhas). Observe como a hierarquia de execução garante que o interno complete todo o seu ciclo antes que o externo avance para a próxima linha."""

# O primeiro laço imprime as colunas (externo), isto é, quantas linhas são saltadas, enquanto o segundo laço imprime as linhas (interno), isto é, cada coluna presente em uma linha
# O primeiro externo itera apenas quando todo o laço interno conclui um ciclo
# O laço interno é limitado de acordo com o crescimento do laço externo

n = int(input())

for i in range(n):

    for j in range(i + 1):

        print(j + 1, end=" ")

    print()