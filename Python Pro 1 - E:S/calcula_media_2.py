"""Enunciado: Aprimore o sistema de notas para determinar a situação do aluno seguindo os critérios institucionais:
Aprovado: Média igual ou superior a 7.0.
AVF (Avaliação Final): Média entre 4.0 (inclusive) e 6.9.
Reprovado: Média inferior a 4.0.
Entrada: Notas AV1 e AV2 (reais).
Saída: Média calculada e a situação textual correspondente.
Dica Pythonica: Evite o "efeito escada" de aninhar vários else: if:. Use o elif (Lutz, Capítulo 12) para manter o código linear, eficiente e fácil de ler. É a forma mais "Zen" de tratar múltiplas condições."""

def calcula_media(valor1, valor2):
    return ((valor1 + valor2) / 2)

av1 = float(input("Informe a nota da sua AV1: \n"))
av2 = float(input("Informe a nota da sua AV2: \n"))

resultado = calcula_media(av1, av2)

if resultado > 7:
    print("Aprovado")
elif resultado >= 4:
    print("Avaliação final")
else:
    print("Reprovado")