"""Enunciado: Crie um script que receba um valor decimal representando o saldo de uma conta. O programa deve identificar o estado da conta.
Entrada: Um valor numérico (ex: 150.50 ou -20.00).
Saída: "Saldo Positivo" (para valores >= 0) ou "Saldo Negativo" (para valores < 0).
Dica Pythonica: Lembre-se do uso obrigatório dos dois pontos (:) após o if e o else. A ausência de delimitadores como {} exige que você seja rigoroso com a indentação de 4 espaços para que o interpretador compreenda o fluxo."""

# Recebe saldo inicial, real com sinal

saldo = float(input("Informe o saldo inicial: \n"))

if saldo >= 0:
    print("O seu saldo é positivo")
else:
    print("O seu saldo está zerado")