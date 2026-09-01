"""Enunciado: Desenvolva um programa que solicite as notas de duas avaliações (AV1 e AV2). Calcule a média aritmética e exiba o resultado formatado.
Entrada: Dois números reais.
Saída: A mensagem "Média: X.X", com exatamente uma casa decimal.
Dica Pythonica: A função input() sempre captura dados como strings (str). Para realizar cálculos com objetos Number, você deve realizar a conversão explícita utilizando float(input())."""

def calcula_media(valor1, valor2):
    return ((valor1 + valor2) / 2)

av1 = float(input("Informe a nota da AV1: \n"))
av2 = float(input("Informe a nota da AV2: \n"))

print(f"A sua média foi {calcula_media(av1, av2):.2f}")