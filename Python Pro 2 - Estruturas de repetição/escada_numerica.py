"""Enunciado: Peça um número inteiro ao usuário (a altura do triângulo). O programa deve imprimir um triângulo de números onde cada linha i contém a sequência de 1 até i.
Exemplo de Saída (para entrada 3):
1
1 2
1 2 3
Entrada: Um número inteiro.
Saída: O padrão numérico triangular.
Dica Pythonica: Aqui, a lógica é dependente: o limite do range() do loop interno (colunas) deve ser definido dinamicamente pelo valor atual do loop externo (linhas). Observe como a hierarquia de execução garante que o interno complete todo o seu ciclo antes que o externo avance para a próxima linha."""

# Primeiro laço imprime as linhas (externo), segundo laço imprime as colunas (interno)
# O primeiro laço itera apenas quando todo o laço interno conclui
# Estrutura do for: for (chamada) - x (inicializador) - in (complemento da chamada) - y (condição de permanência)

#def imprime_triangulo(valor):

#valor = int(input("Altura do triângulo: "))

cont_a = 1 # primeiro iterador, inicial
cont_b = 3 # segundo iterado, inverso

for cont_1 in cont_b:
    print(cont_a)
    cont_a += 1