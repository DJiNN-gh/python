"""Um professor precisa saber qual a média das notas de uma sala e pediu sua ajuda para construir um programa que permita inserir as notas finais de cada aluno e, ao final, exibir a média da sala. Lembre-se que as notas variam de 0 a 10 e o professor digitará -1 quando quiser encerrar as entradas. Obs.: use variáveis de ponto flutuante de dupla precisão.

Formato de entrada

Diversos valores reais, um por linha, simbolizando as notas finais de cada aluno.

Formato de saída

Um número real, com duas casas decimais, simbolizando a média das notas da sala."""

nota = 0.0
acc_nota = 0.0
acc_laco = 0

while(True):
    nota = float(input())
    if nota == -1:
        break
    acc_nota += nota
    acc_laco += 1

print(f"{(acc_nota / (acc_laco)):.2f}")