"""Enunciado: Utilizando duas listas de mesmo tamanho (uma com nomes de alunos e outra com suas notas finais), gere uma lista de frases no formato: "O aluno [nome] obteve a nota [nota]".
Entrada: Duas listas pré-definidas no código.
Saída: Impressão linha a linha das combinações.
Dica Pythonica: Evite o uso de índices manuais como lista[i]. A função zip() é superior porque:
Memória: No Python 3.x, zip é um iterador que gera os pares sob demanda, o que é crucial ao lidar com grandes volumes de dados.
Robustez: Previne erros de "índice fora do intervalo" comuns em travessias manuais.
Clareza: O pareamento é explícito, tornando o código autodocumentado."""

nome_alunos = ["Allan", "Isabella"]
notas_alunos = [9, 4]

alunos = zip(nome_alunos, notas_alunos)

for i, j in alunos:

    print(f"O aluno(a) {i} obteve a nota {j:.2f}")